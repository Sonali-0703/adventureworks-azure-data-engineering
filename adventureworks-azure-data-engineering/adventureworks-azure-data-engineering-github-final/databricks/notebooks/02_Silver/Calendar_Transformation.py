from pyspark.sql.functions import col, month, year

path = "abfss://bronze@dlawstorage.dfs.core.windows.net/AdventureWorks_Calendar"

Calendar = spark.read     .option("header", "true")     .option("inferSchema", "true")     .csv(path)

Calendar = Calendar.withColumn(
    "Month",
    month(col("Date"))
).withColumn(
    "Year",
    year(col("Date"))
)

display(Calendar)

silver_path = "abfss://silver@dlawstorage.dfs.core.windows.net/Adventure_Calendar"

Calendar.write     .format("parquet")     .mode("overwrite")     .save(silver_path)
