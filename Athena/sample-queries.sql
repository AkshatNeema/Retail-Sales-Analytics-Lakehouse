
## 🧠 Technologies Used

- AWS S3, Glue, Lambda, Athena, DynamoDB
- Python, PySpark
- Power BI

## 🧪 Demo Queries (Athena)

-- sql
-- Total sales by category
SELECT category, SUM(total_amount) AS total_sales
FROM sales_enriched
GROUP BY category
ORDER BY total_sales DESC;
