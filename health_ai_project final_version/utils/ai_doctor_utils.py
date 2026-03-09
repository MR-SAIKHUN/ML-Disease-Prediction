def generate_ai_report(symptoms, disease, confidence):

    report = f"""
AI Doctor Diagnostic Report

Detected Symptoms:
{", ".join(symptoms)}

Predicted Disease:
{disease}

Model Confidence:
{round(confidence*100,2)} %

Recommendation:
Please consult a qualified healthcare professional
for a full clinical diagnosis.
"""

    return report