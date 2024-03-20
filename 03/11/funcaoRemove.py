lista = [1, 2, 7, 3, 27, 12, 94]
print(lista)
elemento = int(input("Digite o numero do elemento: "))
if elemento in lista:
  # Remove o elemento da lista
  lista.remove(elemento)
  print("O elemento", elemento, "foi removido da lista")
  print(lista)
else:
  print("O elemento", elemento, "não está na lista")
