import streamlit as st
import yfinance as yf

st.title("Simple Dashboard")
ticker = st.selectbox("Select", ["BTC-USD", "AAPL", "NVDA"])
data = yf.download(ticker, period="1mo")
st.line_chart(data['Close'])
