import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Coffee Sales Dashboard", layout="wide")
st.title("Coffee Shop Sales Analysis Dashboard")
st.subheader("ACC102 Track 4 Interactive Data Tool")

df = pd.read_csv("Coffee_sales.csv")

st.subheader("Data Preview")
st.dataframe(df.head(10))

st.subheader("Top Products by Revenue")
product_revenue = df.groupby("coffee_name")["money"].sum().sort_values(ascending=False)
st.bar_chart(product_revenue)

st.subheader("Hourly Sales Trend")
hourly = df.groupby("hour_of_day")["money"].sum()
st.line_chart(hourly)

st.subheader("Total Revenue by Weekday")
weekday = df.groupby("Weekday")["money"].sum()
st.bar_chart(weekday)

st.subheader("Key Insights")
st.write("• Latte is the highest-revenue product.")
st.write("• Peak hour is 10 AM.")
st.write("• Tuesday has the highest sales.")
st.write("• All payments are made by card.")
