import streamlit as st
import yfinance as yf

st.title("Mera Trading Dashboard")

# Stock ka data mangwana
ticker = "RELIANCE.NS"
data = yf.download(ticker, period="1d")

st.write("Data aa gaya:")
st.write(data)
