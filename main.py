import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

st.title("Анализ котировок компании Apple")

# Ввод периода данных (например, 1 год)
period = st.selectbox("Выберите период данных:", ["1y", "2y", "5y"], index=0)

# Загрузка данных с yfinance
ticker = "AAPL"
data = yf.download(ticker, period=period)

if data.empty:
    st.error("Не удалось загрузить данные. Проверьте подключение к интернету.")
else:
    # Отображение последних данных
    st.subheader("Последние котировки")
    st.write(data.tail())

    # График цены закрытия
    st.subheader("График цены закрытия")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data.index, data['Close'], label='Цена закрытия')
    ax.set_title("Котировки Apple")
    ax.set_xlabel("Дата")
    ax.set_ylabel("Цена (USD)")
    ax.legend()
    st.pyplot(fig)

    #