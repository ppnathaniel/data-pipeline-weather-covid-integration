from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

with open('data/weather_data.json', 'r') as f:
    weather_data = json.load(f)

with open('data/covid_data.json', 'r') as f:
    covid_data = json.load(f)

producer.send('weather_topic', weather_data)
producer.send('covid_topic', covid_data)

producer.flush()
