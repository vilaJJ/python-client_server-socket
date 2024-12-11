'''
Instituto Federal do Tocantins - Campus Araguaína
11 de dezembro de 2024, quarta-feira.
Estudantes: 
    - Allan Batista do Nascimento
    - Beatriz Coelho dos Santos
    - Juan Felipe Alves Flores
    - Samylla Marinho da Silva Aguiar
    - Sara Ghabrielly de Oliveira Silva
Professor: Luis Henrique Sousa Rodrigues
Disciplina: Redes de Telecomunicações II
Curso: Análise e Desenvolvimento de Sistemas        Período: 4°
'''

import os
import socket
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("HOST")
porta = int(os.getenv("PORTA"))

with open(os.getenv("CHAVE_CRIPTOGRAFIA"), "rb") as key_file:
    key_bytes = key_file.read()

key = Fernet(key_bytes)

def enviar_mensagem(cliente_socket, mensagem):
    mensagem_criptografada = key.encrypt(mensagem.encode('utf-8'))
    cliente_socket.send(mensagem_criptografada)
    resposta = cliente_socket.recv(1024)
    resposta_descriptografada = key.decrypt(resposta).decode('utf-8')
    print(f"Resposta do servidor: {resposta_descriptografada}")

def iniciar_cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        hostname = host
        hostInput = input("Insira o endereço do servidor (apenas ENTER para o padrão): ")

        if len(hostInput) > 0:
            hostname = hostInput
        
        cliente_socket.connect((hostname, porta))
        
        while True:
            print("\n1. Enviar mensagem")
            print("2. Sair")

            escolhaId = input("Escolha uma opção: ")
            
            if escolhaId == "1":
                mensagem = input("Digite a mensagem: ")
                enviar_mensagem(cliente_socket, mensagem)
            elif escolhaId == "2":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
    except Exception as erro:
        print(f"Erro: {erro}")
    
    cliente_socket.close()

if __name__ == "__main__":
    iniciar_cliente()