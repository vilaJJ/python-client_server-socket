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
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

chave = Fernet.generate_key()
with open(os.getenv("CHAVE_CRIPTOGRAFIA"), "wb") as arquivo_chave:
    arquivo_chave.write(chave)