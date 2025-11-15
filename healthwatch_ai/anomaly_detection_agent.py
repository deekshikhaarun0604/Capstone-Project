def detect_anomalies(sensor_data):
    anomalies = sensor_data[(sensor_data['heart_rate'] > 100) | (sensor_data['heart_rate'] < 50)]
    return anomalies
