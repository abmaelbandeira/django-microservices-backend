import pika
from admin.settings import CLOUDAMQP_URL

params = pika.URLParameters(CLOUDAMQP_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
