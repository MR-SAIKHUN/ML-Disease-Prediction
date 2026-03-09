import streamlit as st
import pandas as pd
import joblib
import config
import os

from utils.prediction_utils import *
from utils.ai_doctor_utils import generate_ai_report
from utils.report_utils import create_pdf

model = joblib.load(config.MODEL_PATH)
symptoms = joblib.load(config.SYMPTOMS_PATH)

st.title("Disease Prediction")

text = st.text_area("Describe your symptoms")

auto = detect_symptoms_from_text(text, symptoms)

selected = st.multiselect("Detected Symptoms", symptoms, default=auto)

input_data = create_input_vector(symptoms, selected)

if st.button("Predict Disease"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data).max()

    st.success(f"Predicted Disease: {prediction}")

    # Top 5 predictions
    top5 = top5_predictions(model, input_data)

    st.subheader("Top 5 Possible Diseases")
    st.bar_chart(top5.set_index("Disease"))

    # AI doctor report
    report = generate_ai_report(selected, prediction, probability)

    st.subheader("AI Doctor Report")
    st.text_area("", report, height=200)

    # Generate PDF
    pdf = create_pdf(selected, prediction, probability)

    with open(pdf, "rb") as f:
        st.download_button(
            "Download Medical Report",
            f,
            "medical_report.pdf"
        )

    # -------- SAVE HISTORY --------

    name = st.session_state.get("patient_name", "Unknown")
    age = st.session_state.get("patient_age", "Unknown")
    gender = st.session_state.get("patient_gender", "Unknown")

    history_data = {
        "name": name,
        "age": age,
        "gender": gender,
        "symptoms": ", ".join(selected),
        "prediction": prediction,
        "confidence": probability
    }

    df_new = pd.DataFrame([history_data])

    columns = ["name","age","gender","symptoms","prediction","confidence"]

    if os.path.exists(config.HISTORY_PATH):

        df_old = pd.read_csv(config.HISTORY_PATH)

        df_old = df_old.reindex(columns=columns)

        df = pd.concat([df_old, df_new], ignore_index=True)

    else:

        df = df_new

    df = df[columns]

    df.to_csv(config.HISTORY_PATH, index=False)

    st.success("Prediction saved to Patient History")