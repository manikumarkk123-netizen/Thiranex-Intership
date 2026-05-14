import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_excel("sales_data.xlsx")

print("Original Dataset")
print(df.head())

# -----------------------------
# REMOVE DUPLICATES
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# HANDLE MISSING SALES VALUES
# -----------------------------
# Replace missing sales with average sales
average_sales = df["Sales"].mean()

df["Sales"] = df["Sales"].fillna(average_sales)

# -----------------------------
# HANDLE MISSING DATES
# -----------------------------
# Replace missing dates with a default date
df["Date"] = df["Date"].fillna("01-01-2026")

# -----------------------------
# FIX DATE FORMAT
# -----------------------------
# Convert Date column into proper datetime format
df["Date"] = pd.to_datetime(
    df["Date"],
    format="%d-%m-%Y",
    errors="coerce"
)

# If any invalid dates still exist
df["Date"] = df["Date"].fillna(pd.Timestamp("2026-01-01"))

# -----------------------------
# STANDARDIZE REGION NAMES
# -----------------------------
# Convert region names properly
df["Region"] = df["Region"].str.strip().str.title()

# -----------------------------
# REMOVE NEGATIVE OR INVALID SALES
# -----------------------------
df = df[df["Sales"] >= 0]

# -----------------------------
# FIX DATA TYPES
# -----------------------------
df["Order_ID"] = df["Order_ID"].astype(int)
df["Customer"] = df["Customer"].astype(str)
df["Sales"] = df["Sales"].astype(float)

# -----------------------------
# CREATE EXTRA COLUMNS FOR POWER BI
# -----------------------------
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()
df["Day"] = df["Date"].dt.day

# -----------------------------
# SORT DATA
# -----------------------------
df = df.sort_values(by="Date")

# -----------------------------
# SAVE CLEANED FILE
# -----------------------------
output_file = "cleaned_sales_data.xlsx"

df.to_excel(output_file, index=False)

# -----------------------------
# SUCCESS MESSAGE
# -----------------------------
print("\nData Cleaning Completed Successfully!")
print(f"Cleaned file saved as: {output_file}")

print("\nCleaned Dataset Preview:")
print(df.head())