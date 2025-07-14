import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import year, month ,col , to_date
from awsglue.context import GlueContext
from awsglue.job import Job

# Boilerplate
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# ------------------------
# Load Raw Data from Glue Catalog
# ------------------------

sales_df = glueContext.create_dynamic_frame.from_catalog(
    database="retail_raw", table_name="sales_sales").toDF()
    
# Ensure 'date' is in date format before extracting year/month
sales_df = sales_df.withColumn("date", to_date(col("date"), "M/d/yyyy"))


sales_df.show(5,truncate=False)

products_df = glueContext.create_dynamic_frame.from_catalog(
    database="retail_raw", table_name="products_products").toDF()
products_df.show(5,truncate=False)

customers_df = glueContext.create_dynamic_frame.from_catalog(
    database="retail_raw", table_name="customers_customers").toDF()
customers_df.show(5,truncate=False)

# ------------------------
# Transformations
# ------------------------


# Join sales with products and customers
sales_enriched_df = sales_df \
    .join(products_df, "product_id", "left") \
    .join(customers_df, "customer_id", "left")

sales_enriched_df.show(5,truncate=False)

# Add year and month for partitioning
sales_enriched_df = sales_enriched_df.withColumn("year", year(sales_enriched_df["date"]))\
                    .withColumn("month", month(sales_enriched_df["date"]))

sales_enriched_df.show(5,truncate=False)
# ------------------------
# Write as Parquet Partitioned
# ------------------------

sales_enriched_df.write \
    .mode("overwrite") \
    .format("parquet") \
    .partitionBy("region", "year", "month") \
    .save("s3://retail-data-poc/processed/sales_enriched/")

job.commit()
