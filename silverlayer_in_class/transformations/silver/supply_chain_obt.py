from pyspark import pipelines as dp
from utils.utils import rename_columns_to_snake_case
from pyspark.sql.functions import (
    to_timestamp,
    col,
    coalesce,
    lit,
    when,
    round,
)

@dp.table(
    name="supply_chain_in_class.silver.supply_chain_obt",
    comment="Raw orders data as the silver layer in medallion architecture",
    table_properties={
        "delta.columnMapping.mode": "name",
        "delta.minReaderVersion": "2",
        "delta.minWriterVersion": "5",
    },
)
def cleaned_supply_chain():

    df = spark.sql(
        "FROM STREAM supply_chain_in_class.bronze.raw_supply_chain_in_class"
    )

    df = rename_columns_to_snake_case(df)

    return (
        df.withColumn(
            "shipping_date",
            to_timestamp("shipping_date_(dateorders)", "M/d/yyyy H:mm"),
        )
        .withColumn(
            "order_zipcode",
            coalesce(col("order_zipcode").cast("string"), lit("unknown")),
        )
        .withColumn(
            "customer_zipcode",
            coalesce(col("customer_zipcode").cast("string"), lit("unknown")),
        )
        .withColumn(
            "customer_country",
            when(
                col("customer_country") == "EE. UU.",
                "United States",
            ).otherwise(col("customer_country")),
        )
        .withColumn(
            "order_date",
            to_timestamp("order_date_(dateorders)", "M/d/yyyy H:mm"),
        )
        .withColumn(
            "customer_last_name",
            coalesce(col("customer_lname"), lit("unknown")),
        )
        .withColumn(
            "customer_first_name",
            coalesce(col("customer_fname"), lit("unknown")),
        )
        .withColumn(
            "order_item_product_price",
            round(col("order_item_product_price"), 2),
        )
        .drop(
            "customer_email",
            "customer_password",
            "product_description",
            "shipping_date_(dateorders)",
            "order_date_(dateorders)",
            "customer_lname",
            "customer_fname",
        )
    )