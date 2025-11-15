import pandas as pd

def test_detect_anomalies():
    from healthwatch_ai.anomaly_detection_agent import detect_anomalies
    data = pd.DataFrame({
        'heart_rate': [72, 110, 68],
        'blood_pressure': ['120/80', '140/90', '115/70']
    })
    anomalies = detect_anomalies(data)
    assert not anomalies.empty
