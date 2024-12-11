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
import threading
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("HOST")
porta = int(os.getenv("PORTA"))

with open(os.getenv("CHAVE_CRIPTOGRAFIA"), "rb") as key_file:
    key_bytes = key_file.read()

key = Fernet(key_bytes)

def responder_client(cliente_socket, endereco):
    print(f"Conexão recebida de {endereco}")
    
    while True:
        try:
            mensagem_criptografada = cliente_socket.recv(1024)
            if not mensagem_criptografada:
                break
            
            mensagem_descriptografada = key.decrypt(mensagem_criptografada).decode('utf-8')
            print(f"Mensagem recebida: {mensagem_descriptografada}")

            resposta = "Mensagem recebida e decriptada com sucesso."
            resposta_criptografada = key.encrypt(resposta.encode('utf-8'))
            cliente_socket.send(resposta_criptografada)
        except Exception as erro:
            print(f"Erro: {erro}")
            break

    cliente_socket.close()

def iniciar_servidor():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, porta))
    servidor_socket.listen(5)
    print(f"Servidor escutando em {host}:{porta}")

    while True:
        cliente_socket, client_endereco = servidor_socket.accept()
        cliente_thread = threading.Thread(target=responder_client, args=(cliente_socket, client_endereco))
        cliente_thread.start()

if __name__ == "__main__":
    iniciar_servidor()