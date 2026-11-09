import streamlit as st
import pandas as pd
import altair as alt

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

st.subheader("Visits by chief complaint")
st.bar_chart(selected["chief_complaint"].value_counts())

st.subheader("Distribution of wait times")
histogram = (
    alt.Chart(selected)
    .mark_bar()
    .encode(
        alt.X("wait_minutes:Q", bin=alt.Bin(step=10), title="Wait (minutes)"),
        alt.Y("count()", title="Number of visits")
    )
)
st.altair_chart(histogram, width="stretch")

with st.expander("Show the data"):
    st.dataframe(selected)

st.caption("All data are synthetic. No real patient information is used.")