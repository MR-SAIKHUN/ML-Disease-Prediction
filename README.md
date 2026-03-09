# Disease Prediction System Using Random Forest and Symptom Analysis

## Overview
The Disease Prediction System Using Random Forest and Symptom Analysis is a Machine Learning based diagnostic support tool that predicts possible diseases from patient symptoms. The system uses supervised learning algorithms trained on a symptom–disease dataset to assist in preliminary medical analysis.

The platform provides an interactive web interface where users can input symptoms, receive disease predictions, generate AI-based medical reports, and store patient history for further analysis.

The system also includes analytical dashboards for model evaluation and patient data insights.

---

## Objectives

The main objectives of this project are:

- To develop a machine learning model capable of predicting diseases from symptoms.
- To provide an easy-to-use healthcare interface for symptom input and prediction.
- To generate automated AI-based diagnostic reports.
- To track patient history and visualize disease trends.
- To analyze model performance using evaluation metrics and visualization tools.

---

## Key Features

### 1. Patient Data Collection
Users can enter patient information including:
- Name
- Age
- Gender

This information is stored in the system and used during prediction and history tracking.

### 2. Disease Prediction System
The system allows users to:

- Describe symptoms using text input
- Automatically detect symptoms
- Select symptoms manually
- Predict diseases using a trained machine learning model

The system displays:

- Predicted disease
- Model confidence score
- Top 5 possible diseases

### 3. AI Doctor Report
After prediction, the system generates an automated AI diagnostic report containing:

- Detected symptoms
- Predicted disease
- Model confidence level
- Medical recommendation

### 4. Medical Report Generation
The system automatically generates a downloadable medical report in PDF format for patient records.

### 5. Patient History Dashboard
The application stores all predictions in a patient history database and provides features such as:

- Patient search
- Record deletion
- Disease distribution visualization

### 6. Model Analytics Dashboard
The system provides analytics including:

- Model comparison results
- Confusion matrix visualization
- Symptom importance ranking

### 7. Doctor Dashboard
A dashboard designed for medical professionals showing:

- Total patients
- Number of diseases detected
- Average model confidence
- Disease distribution charts

---

## Machine Learning Models Used

The system compares multiple machine learning algorithms:

- Random Forest Classifier
- Decision Tree Classifier
- Naive Bayes Classifier

The best performing model is automatically selected based on accuracy.

---

## Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Programming Language |
| Streamlit | Web Application Framework |
| Scikit-learn | Machine Learning |
| Pandas | Data Processing |
| Matplotlib & Seaborn | Data Visualization |
| Joblib | Model Serialization |
| ReportLab | PDF Report Generation |

---

## Project Structure
```
ML-Disease-Prediction
│
├── app.py
├── config.py
├── train_model.py
│
├── data
│ ├── symptoms_data.csv
│ └── patient_history.csv
│
├── model
│ ├── disease_model.pkl
│ └── symptom_columns.pkl
│
├── utils
│ ├── prediction_utils.py
│ ├── ai_doctor_utils.py
│ └── report_utils.py
│
└── pages
├── Patient_Data.py
├── Disease_Prediction.py
├── Patient_History.py
├── Model_Analytics.py
└── Doctor_Dashboard.py
```

---

## Dataset

The dataset used for training contains symptom indicators and corresponding disease labels. Each row represents a patient case where symptoms are encoded as binary features and the target variable represents the diagnosed disease.

---

## Model Training Process

1. Load symptom dataset
2. Clean dataset and remove unnecessary columns
3. Split data into training and testing sets
4. Train multiple machine learning models
5. Evaluate models using accuracy and F1-score
6. Select the best performing model
7. Save the trained model and symptom features

---

## Evaluation Metrics

The models are evaluated using:

- Accuracy Score
- F1 Score
- Confusion Matrix
- Feature Importance Analysis

---

## How to Run the Project

### Step 1: Install dependencies

pip install -r requirements.txt

### Step 2: Train the model

python train_model.py

### Step 3: Run the application

streamlit run app.py
