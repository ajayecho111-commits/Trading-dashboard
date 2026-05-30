import streamlit as st
import yfinance as yf
from streamlit_option_menu import option_menu

st.set_page_config(page_title="My Trading Terminal", layout="wide")

# Teri 30 assets ki exact list (Yfinance Symbols)
# Maine symbols ko Yahoo Finance ke format mein set kiya hai
assets = {
    "BTCUSD": "BTC-USD", "ETHUSD": "ETH-USD", "BNBUSDT": "BNB-USD", "SOLUSDC": "SOL-USD",
    "GOLD": "GC=F", "SILVER": "SI=F", "USOIL": "CL=F", "TSLA": "TSLA", "PLTR": "PLTR",
    "SPX": "^GSPC", "NVDA": "NVDA", "AAPL": "AAPL", "MSFT": "MSFT", "GOOGL": "GOOGL",
    "AMZN": "AMZN", "META": "META", "ORCL": "ORCL"
}

with st.sidebar:
    st.title("🎯 Watchlist")
    selected_name = option_menu("Assets", list(assets.keys()))

symbol = assets[selected_name]

st.header(f"📈 Chart: {selected_name}")

# Data Fetching logic (Safest way)
try:
    df = yf.download(symbol, period="1mo", interval="1d")
    if not df.empty:
        st.line_chart(df['Close'])
        st.write(f"Latest Price Data for {selected_name}:")
        st.dataframe(df.tail())
    else:
        st.error("Data abhi nahi aa raha. Shayad market closed hai.")
except Exception as e:
    st.error("Kuch technical error aaya hai. Refresh karke dekho.")
