import pandas as pd

# Load the raw Excel file
file_path = "data/Online Retail.xlsx"

df = pd.read_excel(file_path)

# Basic information
print("Dataset loaded successfully!")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Column names
print("\nColumns:")
print(df.columns.tolist())

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Number of cancelled invoices
cancelled_invoices = df["InvoiceNo"].astype(str).str.startswith("C").sum()
print("\nCancelled Invoice Rows:", cancelled_invoices)

# Negative quantity rows
negative_quantity = (df["Quantity"] < 0).sum()
print("Negative Quantity Rows:", negative_quantity)

# Zero or negative price rows
invalid_price = (df["UnitPrice"] <= 0).sum()
print("Zero/Negative Price Rows:", invalid_price)

# Unique customers
unique_customers = df["CustomerID"].nunique()
print("Unique Customers:", unique_customers)

# Unique products
unique_products = df["StockCode"].nunique()
print("Unique Products:", unique_products)

# Unique countries
unique_countries = df["Country"].nunique()
print("Unique Countries:", unique_countries)

# Date range
print("Start Date:", df["InvoiceDate"].min())
print("End Date:", df["InvoiceDate"].max())

# Calculate total sales
df["Sales"] = df["Quantity"] * df["UnitPrice"]

print("Total Sales:", df["Sales"].sum())

# Inspect cancelled transactions

cancelled = df[df["InvoiceNo"].astype(str).str.startswith("C")]

print("\n--- Cancelled Transactions ---")

print("Number of cancelled rows:", len(cancelled))

print("\nSample cancelled transactions:")
print(cancelled.head(10))

print("\nCancelled quantity summary:")
print(cancelled["Quantity"].describe())

print("\nCancelled sales value:")
print(cancelled["Sales"].sum())

# Investigate negative quantities that are not cancelled invoices

negative_not_cancelled = df[
    (df["Quantity"] < 0) &
    (~df["InvoiceNo"].astype(str).str.startswith("C"))
]

print("\n--- Negative Quantity Without Cancelled Invoice ---")

print("Number of rows:", len(negative_not_cancelled))

print("\nSample records:")
print(negative_not_cancelled.head(20))

print("\nTotal negative quantity:")
print(negative_not_cancelled["Quantity"].sum())

print("\nTotal value:")
print(negative_not_cancelled["Sales"].sum())