import streamlit as st
import yfinance as yf
from streamlit_option_menu import option_menu
import pandas as pd

st.set_page_config(layout="wide")

# Teri 30 assets ki list (Yfinance compatible)
assets = {
    "BTCUSD": "BTC-USD", "ETHUSD": "ETH-USD", "GOLD": "GC=F", 
    "NVDA": "NVDA", "AAPL": "AAPL", "MSFT": "MSFT"
}

with st.sidebar:
    st.title("🎯 Pro Terminal")
    selected = option_menu("Assets", list(assets.keys()))

symbol = assets[selected]

st.header(f"📈 Chart: {selected}")

# Data Fetching with Safety
try:
    data = yf.download(symbol, period="3mo", interval="1d")
    if not data.empty:
        # Simple Moving Average (21 days) calculation without pandas_ta
        data['SMA_21'] = data['Close'].rolling(window=21).mean()
        st.line_chart(data[['Close', 'SMA_21']])
    else:
        st.warning("Data load nahi ho pa raha. Market closed ho sakta hai.")
except Exception as e:
    st.error(f"Error: {e}")
