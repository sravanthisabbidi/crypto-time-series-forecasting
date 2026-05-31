import pandas as pd

price = pd.read_csv(
    "data/raw/btc_price.csv"
)

news = pd.read_csv(
    "data/news/coindesk_news.csv"
)

print(price.shape)
print(news.shape)