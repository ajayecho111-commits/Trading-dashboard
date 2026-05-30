import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Pro Trading Terminal", layout="wide")

# Teri 30 Assets ki EXACT list (As per images)
watchlist = {
    "USDT.D": "USDT-D", "TOTAL": "TOTAL", "TOTAL2": "TOTAL2", "TOTAL3": "TOTAL3",
    "BTC.D": "BTC.D", "BTCUSD": "BTC-USD", "ETHUSD": "ETH-USD", "ALTCOIN.P": "ALTCOIN-USD",
    "BNBUSDT": "BNB-USD", "SOLUSDC": "SOL-USD", "GOLD": "GC=F", "XAUTUSDT": "XAUT-USD",
    "PAXGUSDT": "PAXG-USD", "SILVER": "SI=F", "SLVONUSDT": "SLV", "UKOIL": "UKOIL=F",
    "USOIL": "CL=F", "TSLA": "TSLA", "PLTR": "PLTR", "SPX": "^GSPC", "NQ1": "NQ=F",
    "DXY": "DX-Y.NYB", "EURUSD": "EURUSD=X", "NVDA": "NVDA", "AAPL": "AAPL",
    "MSFT": "MSFT", "GOOGL": "GOOGL", "AMZN": "AMZN", "META": "META", "ORCL": "ORCL"
}

st.title("🎯 My Personal Trading Watchlist")

# Watchlist sidebar
selected_name = st.sidebar.selectbox("Select Asset:", list(watchlist.keys()))
symbol = watchlist[selected_name]

try:
    data = yf.download(symbol, period="3mo")
    if not data.empty:
        st.subheader(f"Analysis: {selected_name}")
        st.line_chart(data['Close'])
        st.write(data.tail())
    else:
        st.error("Data abhi load nahi ho raha.")
except:
    st.error("Market Data Error.")
