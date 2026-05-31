import pandas as pd

df = pd.read_csv("data/raw/btc_price.csv")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df.fillna(method="ffill", inplace=True)

df.to_csv(
    "data/processed/btc_cleaned.csv",
    index=False
)

print("\nCleaned Data Saved")