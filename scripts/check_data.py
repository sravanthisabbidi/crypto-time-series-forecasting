import pandas as pd

df = pd.read_csv("data/processed/btc_cleaned.csv")

print(df.head())
print(df.info())
