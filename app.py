import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# Teri 30 assets ki list (Yfinance compatible)
assets = {
    "BTCUSD": "BTC-USD", "ETHUSD": "ETH-USD", "GOLD": "GC=F", "NVDA": "NVDA", 
    "AAPL": "AAPL", "MSFT": "MSFT", "TSLA": "TSLA", "SPX": "^GSPC"
}

with st.sidebar:
    selected = option_menu("Assets", list(assets.keys()))

symbol = assets[selected]

st.title(f"📈 Terminal: {selected}")

# Data Fetch
data = yf.download(symbol, period="1mo", interval="1d")

if not data.empty:
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                    open=data['Open'], high=data['High'],
                    low=data['Low'], close=data['Close'])])
    fig.update_layout(template="plotly_dark", height=500)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Data fetch ho raha hai, zara ruk jao...")
