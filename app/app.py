import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Page Configuration
st.set_page_config(
    page_title="Bitcoin Price Forecasting Dashboard",
    layout="wide"
)

# Title
st.title("📈 Bitcoin Price Forecasting Dashboard")

# -----------------------------
# Load Data
# -----------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

file_path = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "btc_cleaned.csv"
)

df = pd.read_csv(file_path)

# Convert Date Column
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# Dataset Preview
# -----------------------------

st.subheader("Dataset Preview")

st.dataframe(df.head())

# -----------------------------
# Dataset Information
# -----------------------------

st.subheader("Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Records",
        len(df)
    )

with col2:
    st.metric(
        "Maximum Price",
        f"${df['Close'].max():,.2f}"
    )

with col3:
    st.metric(
        "Minimum Price",
        f"${df['Close'].min():,.2f}"
    )

# -----------------------------
# Bitcoin Price Trend
# -----------------------------

st.subheader("Bitcoin Closing Price Trend")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    df["Date"],
    df["Close"]
)

ax.set_title("Bitcoin Closing Price")

ax.set_xlabel("Date")

ax.set_ylabel("Price (USD)")

st.pyplot(fig)

# -----------------------------
# Trading Volume Trend
# -----------------------------

st.subheader("Bitcoin Trading Volume")

fig2, ax2 = plt.subplots(figsize=(12, 5))

ax2.plot(
    df["Date"],
    df["Volume"]
)

ax2.set_title("Trading Volume")

ax2.set_xlabel("Date")

ax2.set_ylabel("Volume")

st.pyplot(fig2)

# -----------------------------
# Model Comparison
# -----------------------------

st.subheader("Model Performance Comparison")

results = pd.DataFrame({
    "Model": ["ARIMA", "Prophet", "LSTM"],
    "RMSE": [
        33437.33,
        15959.35,
        5215.98
    ]
})

st.dataframe(results)

# RMSE Chart

fig3, ax3 = plt.subplots(figsize=(8, 4))

ax3.bar(
    results["Model"],
    results["RMSE"]
)

ax3.set_title("RMSE Comparison")

ax3.set_xlabel("Model")

ax3.set_ylabel("RMSE")

st.pyplot(fig3)

# -----------------------------
# Best Model
# -----------------------------

st.success(
    "🏆 LSTM achieved the best forecasting performance with the lowest RMSE."
)

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.markdown(
    "Developed as part of a Cryptocurrency Time Series Forecasting Project using ARIMA, Prophet and LSTM models."
)