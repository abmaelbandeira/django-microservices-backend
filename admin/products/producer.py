import pika

params = pika.URLParameters('amqps://chzdnyno:cxtMA_neMNuK_uWNSPOq7j9daGGiG00h@gull.rmq.cloudamqp.com/chzdnyno')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')
