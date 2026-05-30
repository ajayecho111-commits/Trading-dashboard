import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# CSS to fix the sidebar scrolling issue
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        overflow: auto;
        height: 100vh;
    }
    </style>
""", unsafe_allow_html=True)

# Teri Assets List
assets = {
    "BTCUSD": "BTC-USD", "ETHUSD": "ETH-USD", "BNBUSDT": "BNB-USD", "SOLUSDC": "SOL-USD",
    "GOLD": "GC=F", "SILVER": "SI=F", "USOIL": "CL=F", "TSLA": "TSLA", "PLTR": "PLTR",
    "SPX": "^GSPC", "NVDA": "NVDA", "AAPL": "AAPL", "MSFT": "MSFT", "GOOGL": "GOOGL",
    "AMZN": "AMZN", "META": "META", "ORCL": "ORCL"
}

with st.sidebar:
    st.title("🎯 Pro Terminal")
    selected = option_menu("Assets", list(assets.keys()))

symbol = assets[selected]

# Chart Logic
st.header(f"📈 Chart: {selected}")
data = yf.download(symbol, period="1mo", interval="1d")

if not data.empty and 'Close' in data.columns:
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                    open=data['Open'], high=data['High'],
                    low=data['Low'], close=data['Close'])])
    fig.update_layout(template="plotly_dark", height=500)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning(f"Data loading for {selected}... wait a second.")
