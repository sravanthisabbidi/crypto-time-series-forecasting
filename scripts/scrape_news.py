import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.coindesk.com/"

headers = {
    "User-Agent":
    "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

headlines = []

for item in soup.find_all("h3"):

    text = item.get_text(strip=True)

    if len(text) > 20:

        headlines.append(text)

df = pd.DataFrame(
    headlines,
    columns=["Headline"]
)

df.to_csv(
    "data/news/coindesk_news.csv",
    index=False
)

print(df.head())