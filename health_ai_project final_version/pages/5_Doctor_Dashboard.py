import streamlit as st
import pandas as pd
import config

st.title("Doctor Dashboard")

try:

    df = pd.read_csv(config.HISTORY_PATH)

    col1,col2,col3 = st.columns(3)

    col1.metric("Patients",len(df))
    col2.metric("Diseases",df["prediction"].nunique())
    col3.metric("Avg Confidence",round(df["confidence"].mean()*100,2))

    st.bar_chart(df["prediction"].value_counts())

except:

    st.warning("No patient data")