import streamlit as st
import pandas as pd

st.title("Qahwa Corner Sales Dashboard")

df = pd.read_csv("cafe_sales.csv")

branch = st.selectbox("Select branch", sorted(df["branch"].unique()))
filtered = df[df["branch"] == branch]

st.metric("Total Revenue (SAR)", int(filtered["total_sar"].sum()))

st.subheader("Revenue by product")
st.bar_chart(filtered.groupby("product")["total_sar"].sum())
