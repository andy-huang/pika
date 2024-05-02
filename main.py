import pika

from setting import url, exchange_name, exchange_type


def on_channel_cancel(frame):
    print(f'channel cancel {frame}')

def on_channel_open(event):
    print(f'connection open - {event}')

parameters = pika.URLParameters(url)
connection = pika.BlockingConnection(
    parameters=parameters)
channel = connection.channel()

channel.exchange_declare(
    exchange=exchange_name,
    exchange_type=exchange_type
)

for i in range(10):
    channel.basic_publish(
        exchange=exchange_name,
        routing_key='',
        body=f'[x] test-{i}'
    )






