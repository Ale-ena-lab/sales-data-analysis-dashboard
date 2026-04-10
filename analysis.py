import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv")

# 1. Check missing values
print("Missing values:\n", df.isnull().sum())

# 2. Remove missing values
df = df.dropna()

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Check column names (IMPORTANT)
print("Columns:\n", df.columns)

# 5. Convert Order Date column
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# 6. Final preview
print("Cleaned Data:\n", df.head())

# 7. Save cleaned file
df.to_csv("cleaned_sales_data.csv", index=False)

print("✅ File saved successfully!")