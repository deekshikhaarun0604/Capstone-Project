def test_ingest_sensor_data():
    from healthwatch_ai.ingestion_agent import ingest_sensor_data
    data = ingest_sensor_data('sample_data/wearable_data.csv')
    assert not data.empty
