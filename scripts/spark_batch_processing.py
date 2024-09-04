from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("BatchProcessing") \
    .getOrCreate()

# Read data from Kafka topics (assuming Kafka topic messages are JSON strings)
weather_df = spark.read.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "weather_topic") \
    .load() \
    .selectExpr("CAST(value AS STRING) as json")

covid_df = spark.read.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "covid_topic") \
    .load() \
    .selectExpr("CAST(value AS STRING) as json")

# Parse the JSON strings into DataFrames
weather_df = spark.read.json(weather_df.rdd.map(lambda x: x.json))
covid_df = spark.read.json(covid_df.rdd.map(lambda x: x.json))

# Perform transformations and join datasets (if applicable)
result_df = weather_df.crossJoin(covid_df)

# Save the processed data as Parquet (or another format) in a mounted directory
result_df.write.parquet("/app/data/combined_data.parquet")
