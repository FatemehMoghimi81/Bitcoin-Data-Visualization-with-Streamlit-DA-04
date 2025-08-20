import streamlit as sn
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

# reading data from csv
btc_csv = pd.read_csv(r"D:\DA\DA 04 tamrin\btc.csv")

sn.title("Bitcoin from 2025")

#we put this here so streamlit dont start from begening with every button
if "show_data" not in sn.session_state:
    sn.session_state.show_data = False

if sn.button("Get Data"):
    sn.session_state.show_data = True

# candlestick 
if sn.session_state.show_data:
    sn.write(btc_csv)
    btc_csv["Date"] = btc_csv.index

    sn.plotly_chart(go.Figure(data=[go.Candlestick(
        x=btc_csv["Date"],
        open=btc_csv["Open"],
        high=btc_csv["High"],
        low=btc_csv["Low"],
        close=btc_csv["Close"]
    )]))

    #  geting mean of datas
    if sn.button("MEAN"):
        sn.write("Mean is", btc_csv["Close"].mean())
