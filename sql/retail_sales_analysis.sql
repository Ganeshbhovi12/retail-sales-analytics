USE retail_analytics;
SHOW VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = ON;
SHOW VARIABLES LIKE 'local_infile';
TRUNCATE TABLE retail_sales;
SET GLOBAL local_infile = ON;
SHOW VARIABLES LIKE 'local_infile';
LOAD DATA LOCAL INFILE 'D:/Retail_Analytics_Project/data/cleaned_retail_data.csv'
INTO TABLE retail_sales
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    InvoiceNo,
    StockCode,
    Description,
    Quantity,
    InvoiceDate,
    UnitPrice,
    @CustomerID,
    Country,
    SalesAmount
)
SET CustomerID = NULLIF(@CustomerID, '');
USE retail_analytics;

SHOW VARIABLES LIKE 'local_infile';

USE retail_analytics;

TRUNCATE TABLE retail_sales;
LOAD DATA LOCAL INFILE 'D:/Retail_Analytics_Project/data/cleaned_retail_data.csv'
INTO TABLE retail_sales
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    InvoiceNo,
    StockCode,
    Description,
    Quantity,
    InvoiceDate,
    UnitPrice,
    @CustomerID,
    Country,
    SalesAmount
)
SET CustomerID = NULLIF(@CustomerID, '');
SELECT COUNT(*) AS total_rows
FROM retail_sales;

SELECT *
FROM retail_sales
LIMIT 10;

SELECT
    MIN(SalesAmount) AS min_sales,
    MAX(SalesAmount) AS max_sales,
    SUM(SalesAmount) AS total_sales
FROM retail_sales;

SELECT COUNT(*) AS total_rows
FROM retail_sales;

SELECT
    COUNT(*) AS total_transactions,
    COUNT(DISTINCT InvoiceNo) AS total_invoices,
    COUNT(DISTINCT StockCode) AS total_products,
    COUNT(DISTINCT CustomerID) AS total_customers,
    COUNT(DISTINCT Country) AS total_countries
FROM retail_sales;

SELECT
    MIN(InvoiceDate) AS first_transaction,
    MAX(InvoiceDate) AS last_transaction
FROM retail_sales;

SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS sales_month,
    ROUND(SUM(SalesAmount), 2) AS total_sales
FROM retail_sales
GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
ORDER BY sales_month;

SELECT
    StockCode,
    Description,
    ROUND(SUM(Quantity), 0) AS total_quantity,
    ROUND(SUM(SalesAmount), 2) AS total_sales
FROM retail_sales
GROUP BY StockCode, Description
ORDER BY total_sales DESC
LIMIT 10;

SELECT
    Country,
    ROUND(SUM(SalesAmount), 2) AS total_sales,
    COUNT(DISTINCT InvoiceNo) AS total_invoices
FROM retail_sales
GROUP BY Country
ORDER BY total_sales DESC
LIMIT 10;

SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS total_orders,
    ROUND(SUM(SalesAmount), 2) AS total_spent
FROM retail_sales
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY total_spent DESC
LIMIT 10;

SELECT
    COUNT(DISTINCT InvoiceNo) AS total_orders,
    ROUND(SUM(SalesAmount), 2) AS total_revenue,
    ROUND(SUM(SalesAmount) / COUNT(DISTINCT InvoiceNo), 2) AS average_order_value
FROM retail_sales;