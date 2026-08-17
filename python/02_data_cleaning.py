import pandas as pd

# Load raw data
file_path = "data/Online Retail.xlsx"

df = pd.read_excel(file_path)

print("Raw dataset loaded successfully!")
print("Original rows:", len(df))

# Remove exact duplicate rows
duplicate_count = df.duplicated().sum()

print("Duplicate rows found:", duplicate_count)

df = df.drop_duplicates()

print("Rows after removing duplicates:", len(df))

# Remove cancelled transactions
cancelled_count = df["InvoiceNo"].astype(str).str.startswith("C").sum()

print("Cancelled rows found:", cancelled_count)

df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

print("Rows after removing cancelled transactions:", len(df))

# Remove negative quantities
negative_quantity_count = (df["Quantity"] < 0).sum()

print("Negative quantity rows found:", negative_quantity_count)

df = df[df["Quantity"] > 0]

print("Rows after removing negative quantities:", len(df))

# Check zero or negative prices
invalid_price_count = (df["UnitPrice"] <= 0).sum()

print("Zero/negative price rows found:", invalid_price_count)

# Remove zero or negative prices
df = df[df["UnitPrice"] > 0]

print("Rows after removing invalid prices:", len(df))

# Check missing product descriptions
missing_description = df["Description"].isnull().sum()

print("Missing descriptions:", missing_description)

print("\nRows with missing descriptions:")
print(df[df["Description"].isnull()].head(10))

# Check missing Customer IDs
missing_customer_id = df["CustomerID"].isnull().sum()

print("\nMissing Customer IDs:", missing_customer_id)

print("Customer IDs available:", df["CustomerID"].notnull().sum())

# Calculate sales amount
df["SalesAmount"] = df["Quantity"] * df["UnitPrice"]

print("\nSales Amount column created successfully!")

print("Total Sales Amount: £{:,.2f}".format(df["SalesAmount"].sum()))

# ==============================
# FINAL DATA QUALITY CHECK
# ==============================

print("\n--- FINAL DATA QUALITY CHECK ---")

print("Total rows:", len(df))
print("Duplicate rows:", df.duplicated().sum())
print("Cancelled invoices:", df["InvoiceNo"].astype(str).str.startswith("C").sum())
print("Negative quantities:", (df["Quantity"] < 0).sum())
print("Zero/negative prices:", (df["UnitPrice"] <= 0).sum())
print("Missing descriptions:", df["Description"].isnull().sum())
print("Missing Customer IDs:", df["CustomerID"].isnull().sum())
print("Missing countries:", df["Country"].isnull().sum())

print("\nSales Amount check:")
print("Minimum Sales Amount: £{:,.2f}".format(df["SalesAmount"].min()))
print("Maximum Sales Amount: £{:,.2f}".format(df["SalesAmount"].max()))
print("Total Sales Amount: £{:,.2f}".format(df["SalesAmount"].sum()))

# Check zero sales amount rows
zero_sales = (df["SalesAmount"] == 0).sum()

print("\nZero Sales Amount Rows:", zero_sales)

if zero_sales > 0:
    print("\nSample zero-sales rows:")
    print(df[df["SalesAmount"] == 0].head(10))

    # Export cleaned data
output_file = "data/cleaned_retail_data.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset exported successfully!")
print("Saved to:", output_file)