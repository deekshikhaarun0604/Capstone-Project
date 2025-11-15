def test_classify_symptoms():
    from healthwatch_ai.symptom_classifier_agent import classify_symptoms
    test_text = "Patient complains of fever and headache."
    symptoms = classify_symptoms(test_text)
    assert 'fever' in symptoms
