import streamlit as st
import pandas as pd

st.title("ED Visit Explorer")
st.write("A small app for exploring synthetic emergency department visits.")

visits = pd.read_csv("data/ed_visits.csv")

age_groups = ["All ages"] + sorted(visits["age_group"].unique())
choice = st.selectbox("Age group", age_groups)

if choice == "All ages":
    selected = visits
else:
    selected = visits[visits["age_group"] == choice]

col1, col2 = st.columns(2)
col1.metric("Number of visits", len(selected))
col2.metric("Median wait (minutes)", selected["wait_minutes"].median())

st.dataframe(selected)