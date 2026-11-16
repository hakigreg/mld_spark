"""Aggregate a small CSV with a real local Spark DataFrame job."""

from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as spark_sum
from pyspark.sql.types import IntegerType, StringType, StructField, StructType


def main() -> None:
    spark = SparkSession.builder.appName("minimum-spark-lab").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    try:
        # An explicit schema keeps column types predictable without an inference pass.
        schema = StructType(
            [
                StructField("order_id", IntegerType(), nullable=False),
                StructField("category", StringType(), nullable=False),
                StructField("amount", IntegerType(), nullable=False),
            ]
        )
        input_path = Path(__file__).resolve().parent / "data" / "sales.csv"
        sales = spark.read.option("header", True).schema(schema).csv(str(input_path))

        # These transformations describe work; the action below executes it.
        totals = (
            sales.groupBy("category")
            .agg(spark_sum("amount").alias("total_amount"))
            .orderBy("category")
        )

        print("PHYSICAL PLAN (look for Exchange around the aggregation):")
        totals.explain(mode="simple")
        print("TOTAL AMOUNT BY CATEGORY:")
        totals.show(truncate=False)
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
