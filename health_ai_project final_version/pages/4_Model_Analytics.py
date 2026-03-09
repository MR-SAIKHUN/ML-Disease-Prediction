import streamlit as st
import pandas as pd
import joblib
import config

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

st.title("Model Analytics Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(config.DATA_PATH)

# Remove unnamed columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

disease_labels = sorted(df["prognosis"].unique())

# -----------------------------
# MODEL COMPARISON
# -----------------------------
st.subheader("Model Performance Comparison")

try:
    results = pd.read_csv("data/model_results.csv")

    st.dataframe(results)

    st.subheader("Model Accuracy Comparison")

    st.bar_chart(
        results.set_index("Model")["Accuracy"]
    )

except:
    st.warning("Model comparison results not found.")

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load(config.MODEL_PATH)

# -----------------------------
# CONFUSION MATRIX
# -----------------------------
st.subheader("Confusion Matrix")

try:

    X_test = joblib.load("data/X_test.pkl")
    y_test = joblib.load("data/y_test.pkl")

    preds = model.predict(X_test)

    cm = confusion_matrix(
        y_test,
        preds,
        labels=disease_labels
    )

    fig, ax = plt.subplots(figsize=(12,10))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=disease_labels,
        yticklabels=disease_labels
    )

    plt.xlabel("Predicted Disease")
    plt.ylabel("Actual Disease")
    plt.title("Disease Prediction Confusion Matrix")

    plt.xticks(rotation=90)
    plt.yticks(rotation=0)

    st.pyplot(fig)

except:
    st.warning("Test data not found. Train the model first.")

# -----------------------------
# FEATURE IMPORTANCE
# -----------------------------
st.subheader("Top Symptom Importance")

try:

    symptoms = joblib.load(config.SYMPTOMS_PATH)

    importances = model.feature_importances_

    importance_df = pd.DataFrame({
        "Symptom": symptoms,
        "Importance": importances
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    ).head(20)

    st.bar_chart(
        importance_df.set_index("Symptom")
    )

except:
    st.warning("Feature importance not available.")