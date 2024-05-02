import pika, sys

msg = ' '.join(sys.argv[1:]) or "hello world"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.basic_qos(prefetch_count=1)
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body=msg)
print('[x] Send msg.')

connection.close()
