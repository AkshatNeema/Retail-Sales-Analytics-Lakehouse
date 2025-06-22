-- SQL to create Redshift tables
CREATE TABLE sales_data (
    order_id INT,
    customer_id VARCHAR,
    product_id VARCHAR,
    quantity INT,
    price FLOAT,
    date DATE
);