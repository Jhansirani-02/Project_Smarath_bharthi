import streamlit as st
from fetch_data import load_local_data
from logic import avg_rainfall_last_n_years, top_m_crops

st.title("Project Samarth — Mini Q&A (Local CSV demo)")

rainfall, crops = load_local_data()

st.write("Data loaded: rainfall rows:", len(rainfall), "crop rows:", len(crops))

qtype = st.selectbox("Choose question type", ["Compare rainfall", "Top crops for state"])

if qtype == "Compare rainfall":
    s1 = st.text_input("State 1", "Andhra Pradesh")
    s2 = st.text_input("State 2", "Tamil Nadu")
    n = st.number_input("Last N years", min_value=1, max_value=10, value=3)
    if st.button("Answer"):
        a1 = avg_rainfall_last_n_years(rainfall, s1, n)
        a2 = avg_rainfall_last_n_years(rainfall, s2, n)
        st.write(f"Average rainfall in last {n} years:")
        st.write(f"{s1}: {a1 if a1 is not None else 'No data'} mm")
        st.write(f"{s2}: {a2 if a2 is not None else 'No data'} mm")

if qtype == "Top crops for state":
    s = st.text_input("State", "Andhra Pradesh")
    n = st.number_input("Last N years", min_value=1, max_value=10, value=3)
    m = st.number_input("Top M crops", min_value=1, max_value=10, value=3)
    if st.button("Answer crops"):
        top = top_m_crops(crops, s, n, m)
        st.write(f"Top {m} crops in {s} for last {n} years (by production):")
        st.dataframe(top)
