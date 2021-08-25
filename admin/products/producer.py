import pika
from admin.settings import CLOUDAMQP_URL

params = pika.URLParameters(CLOUDAMQP_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')
