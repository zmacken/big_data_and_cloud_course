USE CATALOG supply_chain_in_class;
USE SCHEMA gold;

CREATE OR REFRESH MATERIALIZED VIEW supply_chain_in_class.gold.mart_puerto_rico
COMMENT "Mart Puerto rico   - gold layer" AS
SELECT
  ol.total_amount,
  c.first_name,
  c.last_name,
  c.customer_country,
  p.product_name,
  p.product_price
FROM
  fct_orderlines ol
LEFT JOIN dim_customer c on ol.customer_id = c.customer_id
LEFT JOIN dim_product p on ol.product_id = p.product_id
WHERE c.customer_country = "Puerto Rico";
