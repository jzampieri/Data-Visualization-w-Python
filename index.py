import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv("./Data/Car Sales.xlsx - car_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x : str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]
df_filtered

# work's like a grid layout
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x='Date', y='Price ($)', color='Dealer_Region', title='Monthly Billing')
col1.plotly_chart(fig_date)

fig_pie = px.pie(
    df_filtered,
    names='Company',
    values='Price ($)',
    title='Billing Per Company',
    hole=0.4
)
col2.plotly_chart(fig_pie)

fig_transmission = px.bar(
    df_filtered.groupby("Transmission").size().reset_index(name='Quantidade'),
    x="Transmission",
    y="Quantidade",
    title="Cars Sold by Exchange Type",
    text_auto=True,
    color="Transmission",
    color_change={
        "Automatic": "red",
        "Manual": "blue"
    }
)
col3.plotly_chart(fig_transmission)

