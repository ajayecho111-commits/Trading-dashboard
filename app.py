import streamlit as st
import yfinance as yf
from streamlit_option_menu import option_menu
import pandas as pd

st.set_page_config(page_title="Pro Trading Terminal", layout="wide")

# Custom CSS for Dark Mode
st.markdown("""<style>
    [data-testid="stSidebar"] { background-color: #161a1e; }
    </style>""", unsafe_allow_html=True)

# Watchlist Mapping (Sirf wahi assets jo tune bheje hain)
watchlist = {
    "BTCUSD": "BTC-USD", "ETHUSD": "ETH-USD", "BNBUSDT": "BNB-USD", "SOLUSDC": "SOL-USD",
    "GOLD": "GC=F", "SILVER": "SI=F", "USOIL": "CL=F", "TSLA": "TSLA", "PLTR": "PLTR",
    "SPX": "^GSPC", "NVDA": "NVDA", "AAPL": "AAPL", "MSFT": "MSFT", "GOOGL": "GOOGL",
    "AMZN": "AMZN", "META": "META", "ORCL": "ORCL"
}

with st.sidebar:
    st.title("🎯 Pro Terminal")
    selected = option_menu("Watchlist", list(watchlist.keys()))

symbol = watchlist[selected]

st.header(f"📈 Chart: {selected}")

# Data Fetching with Safety
try:
    data = yf.download(symbol, period="3mo", interval="1d")
    
    if not data.empty:
        # Simple Moving Average (21 days) - Bina extra library ke
        data['SMA_21'] = data['Close'].rolling(window=21).mean()
        
        # Plotting
        st.line_chart(data[['Close', 'SMA_21']])
        
        # Stats Table
        st.write("### Technical Snapshot")
        st.dataframe(data.tail())
    else:
        st.warning("Data load nahi ho pa raha. Market closed ya API error.")
except Exception as e:
    st.error(f"Error: {e}")
