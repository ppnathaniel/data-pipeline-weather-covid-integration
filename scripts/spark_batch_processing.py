from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BatchProcessing").getOrCreate()

weather_df = spark.read.parquet("hdfs:///user/hive/warehouse/weather_data")
covid_df = spark.read.parquet("hdfs:///user/hive/warehouse/covid_data")

weather_df.createOrReplaceTempView("weather")
covid_df.createOrReplaceTempView("covid")

result = spark.sql("""
    SELECT weather.id, weather.temp, covid.cases
    FROM weather
    JOIN covid ON weather.id = covid.id
""")
result.write.parquet("data/combined_data.parquet")
