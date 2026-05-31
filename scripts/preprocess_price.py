import pandas as pd

df = pd.read_csv("data/raw/btc_price.csv")

# Remove unwanted rows
df = df.iloc[2:].copy()

# Rename first column
df.rename(columns={"Price": "Date"}, inplace=True)

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Numeric conversion
numeric_cols = ["Close", "High", "Low", "Open", "Volume"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col])

df.reset_index(drop=True, inplace=True)

df.to_csv(
    "data/processed/btc_cleaned.csv",
    index=False
)

print(df.head())
print("Cleaned data saved.")