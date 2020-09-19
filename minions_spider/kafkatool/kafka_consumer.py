from kafka import KafkaConsumer

consumer = KafkaConsumer('heros', bootstrap_servers='localhost:9092')


def consumer_msg(topic, server):
    if (not topic is None) and (not server is None):
        consumer = KafkaConsumer(topic, bootstrap_servers=server)

    index = 0
    for msg in consumer:
        index = index + 1
        print(index)
        print(msg)
