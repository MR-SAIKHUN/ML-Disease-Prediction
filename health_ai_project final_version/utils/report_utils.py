from reportlab.pdfgen import canvas

def create_pdf(symptoms, disease, confidence):

    file = "medical_report.pdf"

    c = canvas.Canvas(file)

    c.drawString(100,750,"AI Medical Diagnosis Report")
    c.drawString(100,720,f"Disease: {disease}")
    c.drawString(100,700,f"Confidence: {round(confidence*100,2)}%")
    c.drawString(100,680,f"Symptoms: {', '.join(symptoms)}")

    c.save()

    return file