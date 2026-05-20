CREATE OR REFRESH STREAMING TABLE supply_chain.bronze.raw_metadata
    COMMENT "Raw metadata - bronze layer" AS
SELECT
  *
FROM
  STREAM read_files(
    "/Volumes/supply_chain/default/raw/metadata",
    format => "csv",
    header => "true",
    inferSchema => "true"
  )