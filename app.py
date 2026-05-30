import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Pro Trading Terminal", layout="wide")

# Teri 30 Assets ki list
assets = [
    "SPX", "NQ1!", "DXY", "EURUSD", "NVDA", "AAPL", "MSFT", "GOOGL", "AMZN", "META", 
    "ORCL", "TSLA", "PLTR", "BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "GOLD", 
    "XAUUSD", "PAXG-USD", "SILVER", "SLV", "UKOIL", "USOIL"
] # Baaki assets yahan add hote jayenge

st.title("🚀 Pro Swing Trading Algo-Terminal")

# Dropdown for assets
selected_asset = st.sidebar.selectbox("Select Asset to Analyze", assets)

# Basic Data Fetching
data = yf.download(selected_asset, period="6mo", interval="1d")

# Dashboard Layout
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader(f"Technical Chart: {selected_asset}")
    st.line_chart(data['Close'])

with col2:
    st.metric("Current Price", f"{data['Close'].iloc[-1]:.2f}")
    st.write("### Quick Stats")
    st.write(f"High: {data['High'].iloc[-1]:.2f}")
    st.write(f"Low: {data['Low'].iloc[-1]:.2f}")

st.info("Agla step: Indicators (EMA, RSI, VWAP) add kar rahe hain...")
