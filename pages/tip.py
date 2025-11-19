import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Настройка страницы
st.set_page_config(page_title="Анализ Чаевых (Tips Dataset)", layout="wide")
st.title("Анализ Чаевых в Ресторане")

# Загрузка данных
@st.cache_data
def load_data():
    # Если файл локальный: df = pd.read_csv("/path/to/tips.csv")
    # Иначе используйте встроенный из Seaborn
    df = sns.load_dataset('tips')
    return df

df = load_data()

if df.empty:
    st.error("Данные не загружены.")
else:
    # Отображение данных
    st.subheader("Таблица Данных")
    st.dataframe(df.head(20))  # Первые 20 строк

    # Метрики
    st.subheader("Ключевые Метрики")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Средний чаевых", f"{df['tip'].mean():.2f} USD")
    with col2:
        st.metric("Средний счет", f"{df['total_bill'].mean():.2f} USD")
    with col3:
        st.metric("Процент чаевых от счета", f"{(df['tip'].sum() / df['total_bill'].sum() * 100):.2f}%")

    # Визуализации
    st.subheader("Гистограмма Распределения Чаевых")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['tip'], bins=20, kde=True, ax=ax1, color='green')
    ax1.set_title("Распределение Чаевых")
    ax1.set_xlabel("Чаевые (USD)")
    ax1.set_ylabel("Частота")
    st.pyplot(fig1)

    st.subheader("Зависимость Чаевых от Общего Счета")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=df, x='total_bill', y='tip', hue='smoker', ax=ax2)
    ax2.set_title("Чаевые vs. Общий Счет")
    ax2.set_xlabel("Общий Счет (USD)")
    ax2.set_ylabel("Чаевые (USD)")
    st.pyplot(fig2)

    st.subheader("Boxplot Чаевых по Дням")
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=df, x='day', y='tip', ax=ax3)
    ax3.set_title("Чаевые по Дням Недели")
    ax3.set_xlabel("День")
    ax3.set_ylabel("Чаевые (USD)")
    st.pyplot(fig3)
