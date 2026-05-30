import streamlit as st
import yfinance as yf
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Pro Terminal", layout="wide")

# Custom CSS for that dark "Pro" look
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #161a1e; }
    </style>
""", unsafe_allow_html=True)

# Teri 30 Assets ki list
watchlist = {
    "USDT.D": "USDT-D", "TOTAL": "TOTAL", "TOTAL2": "TOTAL2", "TOTAL3": "TOTAL3",
    "BTC.D": "BTC.D", "BTCUSD": "BTC-USD", "ETHUSD": "ETH-USD", "ALTCOIN.P": "ALTCOIN-USD",
    "BNBUSDT": "BNB-USD", "SOLUSDC": "SOL-USD", "GOLD": "GC=F", "XAUTUSDT": "XAUT-USD",
    "PAXGUSDT": "PAXG-USD", "SILVER": "SI=F", "SLVONUSDT": "SLV", "UKOIL": "UKOIL=F",
    "USOIL": "CL=F", "TSLA": "TSLA", "PLTR": "PLTR", "SPX": "^GSPC", "NQ1": "NQ=F",
    "DXY": "DX-Y.NYB", "EURUSD": "EURUSD=X", "NVDA": "NVDA", "AAPL": "AAPL",
    "MSFT": "MSFT", "GOOGL": "GOOGL", "AMZN": "AMZN", "META": "META", "ORCL": "ORCL"
}

# Sidebar Watchlist
with st.sidebar:
    st.title("🎯 Watchlist")
    selected = option_menu("Assets", list(watchlist.keys()), 
                           icons=['currency-exchange'] * 30, menu_icon="cast", default_index=0)

# Main Logic
symbol = watchlist[selected]
st.header(f"Chart: {selected}")

try:
    data = yf.download(symbol, period="3mo")
    if not data.empty:
        st.line_chart(data['Close'])
    else:
        st.error("Data load nahi ho raha, market shayad closed hai.")
except:
    st.error("Error fetching data.")
