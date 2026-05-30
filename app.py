import streamlit as st
import yfinance as yf
import pandas_ta as ta # Indicators ke liye

st.set_page_config(page_title="Pro Swing Algo-Terminal", layout="wide")

# Teri 30 assets ki list (Mapping)
watchlist = {
    "BTCUSD": "BTC-USD", "ETHUSD": "ETH-USD", "BNBUSDT": "BNB-USD", "SOLUSDC": "SOL-USD",
    "GOLD": "GC=F", "SILVER": "SI=F", "USOIL": "CL=F", "TSLA": "TSLA", "PLTR": "PLTR",
    "SPX": "^GSPC", "NVDA": "NVDA", "AAPL": "AAPL", "MSFT": "MSFT", "GOOGL": "GOOGL",
    "AMZN": "AMZN", "META": "META", "ORCL": "ORCL" 
    # Baaki assets bhi aise hi map ho jayenge
}

st.sidebar.title("🎯 My Watchlist")
selected = st.sidebar.selectbox("Select Asset", list(watchlist.keys()))

# Data Fetching
symbol = watchlist[selected]
data = yf.download(symbol, period="6mo", interval="1d")

if not data.empty:
    # Indicators Calculation
    data['EMA21'] = ta.ema(data['Close'], length=21)
    data['RSI'] = ta.rsi(data['Close'], length=14)
    
    st.header(f"📈 Chart: {selected}")
    
    # Chart plotting
    st.line_chart(data[['Close', 'EMA21']])
    
    # Analysis Table
    st.write("### Technical Snapshot")
    st.dataframe(data.tail())
else:
    st.error("Is asset ka data yfinance par nahi hai. Hum doosra source use karenge.")

st.info("System Ready: Agle step mein hum VWAP, MACD aur AI Analysis add karenge.")
