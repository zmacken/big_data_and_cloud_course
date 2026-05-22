CREATE OR REFRESH STREAMING TABLE supply_chain_in_class.bronze.raw_metadata_in_class
    COMMENT "Raw metadata - bronze layer" AS
SELECT
  *
FROM
  STREAM read_files(
    "/Volumes/supply_chain_in_class/default/raw/metadata",
    format => "csv",
    header => "true",
    inferSchema => "true"
  )