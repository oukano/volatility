import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
import pytz

# Define available ticker symbols and their names
ticker_options = {
    "QQQ": "Nasdaq",
    "GLD": "XAU",
    "SPY": "S&P"
}

st.title("CTT - Expected Move Calculator")

# Create a dropdown for selecting the ticker symbol
selected_ticker = st.selectbox("Select Ticker Symbol", options=list(ticker_options.keys()), format_func=lambda x: ticker_options[x])
st.write(f"Selected Ticker: {selected_ticker}")

# Fetch the ticker data
ticker = yf.Ticker(selected_ticker)
print(ticker)

for i in range(1, 4):
    yesterday_close = fetch_stock_data(ticker, days_back=i)
    if yesterday_close:
        print("yesterday_close : " + yesterday_close)
        break
