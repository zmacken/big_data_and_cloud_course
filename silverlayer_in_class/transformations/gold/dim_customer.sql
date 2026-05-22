CREATE OR REFRESH MATERIALIZED VIEW supply_chain_in_class.gold.dim_customer
COMMENT "Dim customer deduplicated  - gold layer" AS
SELECT
  customer_id,
  MAX_BY(customer_first_name, order_date) AS first_name,
  MAX_BY(customer_last_name, order_date) AS last_name,
  MAX_BY(customer_country, order_date) AS customer_country
FROM
  supply_chain_in_class.silver.supply_chain_obt
GROUP BY customer_id
ORDER BY customer_id;