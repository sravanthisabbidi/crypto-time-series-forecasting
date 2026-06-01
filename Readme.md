# 📈 Cryptocurrency Time Series Forecasting

## Project Overview

This project focuses on forecasting Bitcoin (BTC) prices using Time Series Analysis and Deep Learning techniques. Historical Bitcoin price data was collected and analyzed to understand market trends and predict future prices.

The project compares the performance of three forecasting models:

- ARIMA
- Prophet
- LSTM (Long Short-Term Memory)

The goal is to identify the most accurate model for cryptocurrency price prediction.

---

## Problem Statement

Cryptocurrency prices are highly volatile and influenced by various market factors. Accurate forecasting can help investors and analysts make informed decisions.

This project aims to:

- Analyze historical Bitcoin price trends
- Perform sentiment analysis on cryptocurrency news
- Build forecasting models
- Compare model performance using evaluation metrics

---

## Data Sources

### Bitcoin Historical Prices

Data collected using Yahoo Finance API.

Features:

- Date
- Open
- High
- Low
- Close
- Volume

### Cryptocurrency News

News headlines scraped from CoinDesk.

Used for:

- Sentiment Analysis
- Market trend understanding

---

## Project Workflow

### 1. Data Collection

- Bitcoin historical prices downloaded using Yahoo Finance
- Cryptocurrency news headlines scraped from CoinDesk

### 2. Data Preprocessing

- Removed invalid rows
- Converted data types
- Handled missing values
- Created cleaned dataset

### 3. Exploratory Data Analysis (EDA)

Performed:

- Closing Price Trend Analysis
- Moving Average Analysis
- Daily Returns Distribution
- Volatility Analysis
- Trading Volume Analysis

### 4. Sentiment Analysis

Used TextBlob to calculate sentiment polarity scores for cryptocurrency news headlines.

Sentiment Categories:

- Positive
- Neutral
- Negative

### 5. Feature Engineering

Created additional features:

- Daily Returns
- MA50 (50-Day Moving Average)
- MA200 (200-Day Moving Average)
- Volatility

### 6. Forecasting Models

#### ARIMA

Traditional statistical time series forecasting model.

#### Prophet

Facebook Prophet model for trend forecasting.

#### LSTM

Deep Learning model using TensorFlow/Keras for sequential data prediction.

---

## Model Evaluation

Metrics Used:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

### Results

| Model | MAE | RMSE |
|---------|---------:|---------:|
| ARIMA | 30896.62 | 33437.33 |
| Prophet | 14331.75 | 15959.35 |
| LSTM | 3791.53 | 4677.24 |

---

## Best Performing Model

🏆 **LSTM achieved the best performance with the lowest RMSE and MAE.**

This indicates that deep learning approaches are more effective in capturing complex cryptocurrency market patterns.

---

## Streamlit Dashboard

An interactive dashboard was developed using Streamlit.

Dashboard Features:

- Dataset Preview
- Bitcoin Price Trend Visualization
- Trading Volume Analysis
- Model Performance Comparison
- Best Model Identification

Run locally:

```bash
streamlit run app/app.py
```

---

## Project Structure

```text
Crypto_TimeSeries_Project
│
├── data
│   ├── raw
│   │   └── btc_price.csv
│   │
│   ├── processed
│   │   ├── btc_cleaned.csv
│   │   └── btc_features.csv
│   │
│   └── news
│       └── coindesk_news.csv
│
├── scripts
│   ├── scrape_crypto_prices.py
│   ├── scrape_news.py
│   ├── preprocess_price.py
│   ├── combine_data.py
│   └── check_data.py
│
├── notebooks
│   └── Crypto_Forecasting.ipynb
│
├── app
│   └── app.py
│
├── models
│
├── images
│
├── requirements.txt
│
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- TextBlob
- Statsmodels
- Prophet
- TensorFlow
- Scikit-Learn
- Streamlit

---

## Future Improvements

- Real-time Bitcoin price forecasting
- Integration with live cryptocurrency APIs
- Advanced sentiment analysis using NLP transformers
- Multi-cryptocurrency forecasting
- Hyperparameter optimization

---

## Author

Developed as part of a Cryptocurrency Time Series Forecasting Project using ARIMA, Prophet, and LSTM models.