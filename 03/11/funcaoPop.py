lista = [1, 2, 7, 3, 27, 12, 94]
print(lista)
posicao = int(input("Digite o numero da posicao: "))

try:
  # Remove o elemento da lista
  lista.pop(posicao)
  print("O elemento na posição", posicao, "foi removido da lista")
  print(lista)
except:
  print("A posição", posicao, "não está na lista")
