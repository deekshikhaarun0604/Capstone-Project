def ingest_sensor_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def ingest_medical_logs(file_path):
    with open(file_path, 'r') as f:
        logs = f.read()
    return logs
