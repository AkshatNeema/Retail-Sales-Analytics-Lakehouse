# 🏬 Retail Data Lakehouse PoC using AWS Glue, Athena, DynamoDB, and Power BI

This project demonstrates a modular data lakehouse architecture to simulate real-time and batch processing of sales data using AWS.

## 📌 Architecture Overview

- **Data Ingestion**: CSV files uploaded to S3 landing zone
- **ETL Transformation**: AWS Glue (PySpark)
- **Cataloging**: AWS Glue Crawlers + Athena
- **Storage Format**: Partitioned Parquet files
- **Metadata Tracking**: DynamoDB
- **Visualization**: Power BI connected to Athena

## 📂 Project Structure

├── data-samples/ → Sample raw data (sales, customers, products)
├── glue-scripts/ → PySpark script for ETL
├── powerbi-dashboard/ → .pbix Power BI dashboard file
├── dynamodb/ → Sample schemas for job tracking
├── athena/ → Example queries
├── architecture/ → Architecture diagram
└── README.md