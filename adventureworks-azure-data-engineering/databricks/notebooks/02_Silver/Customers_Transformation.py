from pyspark.sql.functions import col, concat_ws

# Customers is expected to be loaded into the notebook before this cell.

Customers = Customers.withColumn(
    "FullName",
    concat_ws(" ", col("FirstName"), col("LastName"))
)

display(Customers)
