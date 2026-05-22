from pyspark import pipelines as dp

BASE_DIR = "/Volumes/supply_chain_in_class/default/raw"

schema = (
    spark.read.format("csv")
    .options(header=True, inferSchema=True)
    .load(f"{BASE_DIR}/data/DataCoSupplyChainDataset.csv")
    .schema
)

@dp.table(
    name="supply_chain_in_class.bronze.raw_supply_chain_in_class",
    comment="Raw orders data as the silver layer in medallion architecture",
    table_properties={
        "delta.columnMapping.mode": "name",
        "delta.minReaderVersion": "2",
        "delta.minWriterVersion": "5",
    },
)
def raw_supply_chain():
    return (
        spark.readStream.format("csv")
        .options(header="true", inferSchema="true", encoding="UTF-8")
        .schema(schema)
        .load(f"{BASE_DIR}/data")
    )