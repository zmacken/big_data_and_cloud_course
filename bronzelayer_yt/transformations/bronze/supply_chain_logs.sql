CREATE OR REFRESH STREAMING TABLE supply_chain.bronze.raw_access_logs
    COMMENT "Raw access logs - bronze layer" AS
SELECT
  *
FROM
  STREAM read_files(
    "/Volumes/supply_chain/default/raw/logs",
    format => "csv",
    header => "true",
    inferSchema => "true"
  )