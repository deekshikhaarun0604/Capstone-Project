def create_explanation(symptoms, anomalies):
    explanation = f"Detected symptoms: {', '.join(symptoms)}.\n"
    explanation += f"Anomalies found in sensor data: {anomalies.shape[0]} events."
    return explanation
