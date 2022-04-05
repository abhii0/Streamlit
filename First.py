import streamlit as sp
import yfinance as yf
import pandas as pd

sp.write("""
## Simple Stock Price App

Shown are the stock closing price and volume of Google!

"""

)

tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = 'id',start = "2022-01-01", end = "2022-04-05")

sp.line_chart(tickerDf.Close)
sp.line_chart(tickerDf.Volume)