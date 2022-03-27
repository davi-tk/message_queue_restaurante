import pika, sys, os, json

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='pedido')

    def callback(ch, method, properties, body):
        print(f"Novo pedido:\n {json.loads(body)}")

    channel.basic_consume(queue='pedido', on_message_callback=callback, auto_ack=True)

    print('Restaurante aberto, aguardando pedidos')
    channel.start_consuming()


try:
    main()
except KeyboardInterrupt:
        sys.exit(0)