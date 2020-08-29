from kafka import TopicPartition
from kafka import KafkaConsumer

consumer = KafkaConsumer('heros',bootstrap_servers='localhost:9092')

index = 0
for msg in consumer:
    index = index + 1
    print(index)
    print(msg)