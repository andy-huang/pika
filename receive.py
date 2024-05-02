import pika
from pika.channel import Channel
import os, sys, time


def callback(ch: Channel, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(f" [x] Done")
        # manual ack the message
        ch.basic_ack( delivery_tag = method.delivery_tag)

def main():
    connection = pika.Connection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='default')
    channel.basic_consume(queue='hello',
                        on_message_callback=callback)

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)