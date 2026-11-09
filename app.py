import streamlit as st
import pandas as pd

st.title("ED Visit Explorer")
st.write("A small app for exploring synthetic emergency department visits.")

visits = pd.read_csv("data/ed_visits.csv")

st.metric("Number of visits", len(visits))
st.metric("Median wait (minutes)", visits["wait_minutes"].median())

st.dataframe(visits)