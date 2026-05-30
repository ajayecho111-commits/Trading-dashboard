import streamlit as st
import yfinance as yf
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Pro Terminal", layout="wide")

# Teri 30 Assets ki EXACT list
watchlist = {
    "USDT.D": "USDT-D", "TOTAL": "TOTAL", "TOTAL2": "TOTAL2", "TOTAL3": "TOTAL3",
    "BTC.D": "BTC.D", "BTCUSD": "BTC-USD", "ETHUSD": "ETH-USD", "ALTCOIN.P": "ALTCOIN-USD",
    "BNBUSDT": "BNB-USD", "SOLUSDC": "SOL-USD", "GOLD": "GC=F", "XAUTUSDT": "XAUT-USD",
    "PAXGUSDT": "PAXG-USD", "SILVER": "SI=F", "SLVONUSDT": "SLV", "UKOIL": "UK=F",
    "USOIL": "CL=F", "TSLA": "TSLA", "PLTR": "PLTR", "SPX": "^GSPC", "NQ1": "NQ=F",
    "DXY": "DX-Y.NYB", "EURUSD": "EURUSD=X", "NVDA": "NVDA", "AAPL": "AAPL",
    "MSFT": "MSFT", "GOOGL": "GOOGL", "AMZN": "AMZN", "META": "META", "ORCL": "ORCL"
}

with st.sidebar:
    st.title("🎯 Watchlist")
    selected = option_menu("Assets", list(watchlist.keys()))

symbol = watchlist[selected]

st.header(f"📈 Chart: {selected}")

try:
    data = yf.download(symbol, period="1mo", interval="1d")
    if not data.empty:
        st.line_chart(data['Close'])
        st.write("Recent Price Action:")
        st.dataframe(data.tail())
    else:
        st.warning(f"{selected} ka data abhi fetch nahi ho raha (Market/Index limitations).")
except Exception as e:
    st.error("Error loading data.")
