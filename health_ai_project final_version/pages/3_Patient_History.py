import streamlit as st
import pandas as pd
import config
import os

st.title("Patient History Dashboard")

if os.path.exists(config.HISTORY_PATH):

    df = pd.read_csv(config.HISTORY_PATH)

    # -------- SEARCH --------
    search = st.text_input("Search Patient Name")

    if search:
        df = df[df["name"].str.contains(search, case=False, na=False)]

    # -------- ADD CHECKBOX COLUMN --------
    df_display = df.copy()
    df_display.insert(0, "Select", False)

    edited_df = st.data_editor(
        df_display,
        use_container_width=True,
        num_rows="fixed"
    )

    # -------- DELETE BUTTON --------
    if st.button("Delete Selected Rows"):

        rows_to_delete = edited_df[edited_df["Select"] == True].index

        df = df.drop(rows_to_delete)

        df.to_csv(config.HISTORY_PATH, index=False)

        st.success("Selected rows deleted")

        st.rerun()

    # -------- CHART --------
    if "prediction" in df.columns:

        st.subheader("Disease Distribution")

        st.bar_chart(df["prediction"].value_counts())

else:

    st.warning("No patient history found.")