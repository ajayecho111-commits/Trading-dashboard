import streamlit as st

# Page setup
st.set_page_config(page_title="Pro Trading Dashboard", layout="wide")

# Custom CSS for Dark Look
st.markdown("""
    <style>
    .main { background-color: #1e1e1e; }
    h1 { color: #00FF9D; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 Swing Trading Pro")
st.write("Professional market analysis at your fingertips.")

# Side bar
st.sidebar.header("Filter Settings")
symbol = st.sidebar.text_input("Enter Stock Symbol", "RELIANCE")
timeframe = st.sidebar.selectbox("Select Timeframe", ["15m", "1h", "1D"])

# Charts area
col1, col2 = st.columns(2)
col1.metric("Current Price", "₹2,500", "+2.5%")
col2.metric("Volume", "1.2M", "-0.5%")

st.info("Charts loading for: " + symbol)
