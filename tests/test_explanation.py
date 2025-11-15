def test_create_explanation():
    from healthwatch_ai.explanation_agent import create_explanation
    explanation = create_explanation(['fever'], None)
    assert "fever" in explanation.lower()
