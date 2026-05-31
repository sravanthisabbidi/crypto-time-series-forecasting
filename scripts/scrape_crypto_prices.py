import yfinance as yf

btc = yf.download(
    "BTC-USD",
    start="2020-01-01",
    end="2026-01-01"
)

btc.to_csv("data/raw/btc_price.csv")

print(btc.head())
print("Data Saved Successfully")