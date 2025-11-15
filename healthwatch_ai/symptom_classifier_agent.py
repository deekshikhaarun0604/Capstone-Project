def classify_symptoms(text):
    symptoms = ['fever', 'cough', 'fatigue']
    detected = [sym for sym in symptoms if sym in text.lower()]
    return detected
