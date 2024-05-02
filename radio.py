import pika
import os, sys, time

from setting import url, exchange_name, exchange_type

def callback(channel, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        # manual ack the message
        # ch.basic_ack( delivery_tag = method.delivery_tag)

def main():
    parameters = pika.URLParameters(url)
    connection = pika.BlockingConnection(
        parameters=parameters)
    channel = connection.channel()
    
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    
    channel.queue_bind(exchange=exchange_name, queue=queue_name)
    print(' [*] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(
         queue=queue_name,
         auto_ack=True,
         on_message_callback=callback
    )
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