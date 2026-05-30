import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# Page Config
st.set_page_config(page_title="Pro Terminal", layout="wide")

# Asset list
assets = {"BTCUSD": "BTC-USD", "ETHUSD": "ETH-USD", "GOLD": "GC=F", "NVDA": "NVDA", "AAPL": "AAPL"} 

with st.sidebar:
    selected = option_menu("Assets", list(assets.keys()))

symbol = assets[selected]
data = yf.download(symbol, period="1mo", interval="1d")

st.header(f"📈 Professional Chart: {selected}")

# Plotly Candlestick Chart
fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'], high=data['High'],
                low=data['Low'], close=data['Close'])])

fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_dark", height=500)
st.plotly_chart(fig, use_container_width=True)
