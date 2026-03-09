import pandas as pd

def create_input_vector(symptoms, selected):

    input_data = pd.DataFrame([[0]*len(symptoms)], columns=symptoms)

    for s in selected:
        input_data[s] = 1

    return input_data


def top5_predictions(model, input_data):

    probs = model.predict_proba(input_data)[0]
    diseases = model.classes_

    df = pd.DataFrame({
        "Disease": diseases,
        "Probability": probs
    })

    return df.sort_values("Probability", ascending=False).head(5)


def detect_symptoms_from_text(text, symptom_list):

    detected = []
    text = text.lower()

    for s in symptom_list:

        if s.replace("_"," ") in text:
            detected.append(s)

    return detected