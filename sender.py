import pika
import json


feijao = ['preto', 'marrom', 'verde']
arroz = ['branco', 'integral']
proteina = ['frango', 'carne', 'peixe']
salada = ['crua', 'cozida']
suco = [True, False]

def select_feijao():
    escolha = int(input(f'Qual tipo de feijão você deseja?\
                        \n1.{feijao[0]}\
                        \n2.{feijao[1]}\
                        \n3.{feijao[2]}\
                        \n'))

    return feijao[escolha - 1]

def select_arroz():
    escolha = int(input(f'Qual tipo de arroz você deseja?\
                        \n1.{arroz[0]}\
                        \n2.{arroz[1]}\
                        \n'))

    return arroz[escolha - 1]

def select_proteina():
    escolha = int(input(f'Qual tipo de proteina você deseja?\
                        \n1.{proteina[0]}\
                        \n2.{proteina[1]}\
                        \n3.{proteina[2]}\
                        \n'))

    return proteina[escolha - 1]

def select_salada():
    escolha = int(input(f'Qual tipo de salada você deseja?\
                        \n1.{salada[0]}\
                        \n2.{salada[1]}\
                        \n'))

    return salada[escolha - 1]

def select_suco():
    escolha = int(input(f'Quer suco para acompanhar?\
                        \n1.Sim\
                        \n2.Não\
                        \n'))

    return suco[escolha - 1]


def criar_pedido():
    pedido = {}
    pedido['feijao'] = select_feijao()
    pedido['arroz'] = select_arroz()
    pedido['proteina'] = select_proteina()
    pedido['salada'] = select_salada()
    pedido['suco'] = select_suco()

    return pedido


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

pedido = criar_pedido()

channel.queue_declare(queue='pedido')

channel.basic_publish(exchange='',
                      routing_key='pedido',
                      body=json.dumps(pedido))

print(f"Seu pedido é: \n{pedido}\n Status -> enviado")

connection.close()
