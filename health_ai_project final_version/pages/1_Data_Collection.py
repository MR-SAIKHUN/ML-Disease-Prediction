import streamlit as st

st.title("Patient Data Collection")

name = st.text_input("Patient Name")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])

if st.button("Save Patient Info"):

    st.session_state["patient_name"] = name
    st.session_state["patient_age"] = age
    st.session_state["patient_gender"] = gender

    st.success("Patient information saved. Go to Disease Prediction.")