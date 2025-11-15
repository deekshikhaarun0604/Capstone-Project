def test_check_compliance():
    from healthwatch_ai.compliance_agent import check_compliance
    result = check_compliance()
    assert "complies" in result.lower()
