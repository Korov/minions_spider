from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)


def on_send_success(*args, **kwargs):
    """
    发送成功的回调函数
    :param args:
    :param kwargs:
    :return:
    """
    return args


def on_send_error(*args, **kwargs):
    """
    发送失败的回调函数
    :param args:
    :param kwargs:
    :return:
    """

    return args


def send_msgs(topic, key, msgs):
    for msg in msgs:
        msg = str(msgs)
        print('topic:{} key:{} msg:{}', str(msg).encode('utf-8'), topic, key)
        producer.send(topic=topic, key=key, value=msg).add_callback(on_send_success).add_errback(on_send_error)


def send_msg(topic, key, msg):
    key = str(key).encode('utf-8')
    msg = str(msg).encode('utf-8')
    print('topic:{} key:{} msg:{}'.format(topic, key, msg))
    producer.send(topic, key=key, value=msg).add_callback(on_send_success).add_errback(
        on_send_error)
