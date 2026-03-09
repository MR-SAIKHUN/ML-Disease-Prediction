import streamlit as st

st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🩺",
    layout="wide"
)

st.title("AI Healthcare Diagnosis System")

st.markdown("""
Welcome to the **AI Medical Diagnosis Dashboard**

Features:

• Disease prediction AI  
• Patient history tracking  
• Model analytics  
• Doctor dashboard  
• AI medical report generation
""")

st.sidebar.success("Select a module")