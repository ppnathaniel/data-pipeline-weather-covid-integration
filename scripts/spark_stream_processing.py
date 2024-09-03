from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType, FloatType

# Create Spark session
spark = SparkSession.builder \
    .appName("WeatherAndCovidStreamProcessing") \
    .getOrCreate()

# Define schemas for weather and COVID-19 data
weather_schema = StructType() \
    .add("id", StringType()) \
    .add("main", StringType()) \
    .add("description", StringType()) \
    .add("temp", FloatType()) \
    .add("pressure", IntegerType()) \
    .add("humidity", IntegerType())

covid_schema = StructType() \
    .add("cases", IntegerType()) \
    .add("deaths", IntegerType()) \
    .add("recovered", IntegerType())

# Read streaming data from Kafka topics
weather_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "weather_topic") \
    .load()

covid_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "covid_topic") \
    .load()

# Parse the JSON data
weather_df_parsed = weather_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), weather_schema).alias("data")) \
    .select("data.*")

covid_df_parsed = covid_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), covid_schema).alias("data")) \
    .select("data.*")

# Join the weather and COVID-19 data
joined_df = weather_df_parsed.crossJoin(covid_df_parsed)

# Write the processed data to the console (or to storage)
query = joined_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
