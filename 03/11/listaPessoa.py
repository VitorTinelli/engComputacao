import os
import time
# Cria uma lista de pessoas vazia para armazenar os dicinários com os dados das pessoas
listaPessoas = []	

while(True):
  # Lê o nome da pessoa e caso ela digite X encerra o programa
  nome = input("Digite o nome (ou X para encerrar): ")
  if nome.upper() == "X":
    break

  # Lê a idade e a cidade
  idade = int(input("Digite a idade: "))
  cidade = input("Digite a cidade: ")

  # Cria um dicionário com os dados da pessoa
  pessoa = {"nome": nome, "idade": idade, "cidade": cidade}
  listaPessoas.append(pessoa)
  print("Pessoa cadastrada com sucesso!")
  
  # Apos 1.5 segundos limpa a tela e mostra a lista de pessoas
  time.sleep(1.5)
  os.system('cls')
  print("Lista de pessoas: ")
  print(listaPessoas)

  
