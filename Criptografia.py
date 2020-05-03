# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:06:52 2020

@author: Mathews
"""
import json
import sys
import hashlib
import requests

linkOrigem = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=69494b875f6e3c374d4b969409e8354ad22159f8"
linkResposta = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=69494b875f6e3c374d4b969409e8354ad22159f8"
caminho = "C:\\Users\\Mathews\\Downloads\\Acelera Python\\answer.json"
token = "69494b875f6e3c374d4b969409e8354ad22159f8"

#Abre o Arquivo para leitura
with open(caminho, 'r+') as arquivo:
    try:
        dicionario = json.load(arquivo)
    except:
        print('Arquivo json nulo ou vazio!')
        sys.exit(0)
        
    #Valores do dicionario JSON
    dicionario['name'] = "answer"
    dicionario['file'] = "answer"
    dicionario['token'] = token
    dicionario['type'] = "json"
    numCasas = dicionario['numero_casas']
    token = dicionario['token']
    cifra = dicionario['cifrado']
    deci = dicionario['decifrado']
    resumoCrip = dicionario['resumo_criptografico']
    
    #Variável Auxiliar
    solucao=""

    #Decodificação da Cifra
    for caractere in cifra:
        if(caractere != " " and caractere != "," and caractere != "."):
            auxiliar = ord(caractere)-numCasas
            solucao += chr(auxiliar)
        if(caractere == " "):
            solucao += " "
        if(caractere == ","):
            solucao += ","
        if(caractere == "."):
            solucao += "."
            
    dicionario['decifrado'] = solucao
    
    #Mapa Hashing - SHA1
    resumo = hashlib.sha1(solucao.encode()) 
    dicionario['resumo_criptografico'] = resumo.hexdigest()

with open(caminho, 'w') as arquivo2:
    json.dump(dicionario, arquivo2)
    
t = requests.post(linkResposta, files={"answer": open(caminho, "rb")})
print(t)


    
    
    
    
    
    
