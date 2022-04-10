from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[4]").appName("crypto-analysis").getOrCreate()
df = spark.read.options(header='True', inferSchema='True').csv("dataset/bitcoin_historical_data.csv")
df.show()
