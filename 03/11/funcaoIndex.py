lista = [1, 2, 7, 3, 27, 12, 94]
print(lista)
elemento = int(input("Digite o numero do elemento: "))

if elemento in lista: # Passa por cada elemento da lista e verifica se o elemento está na lista
  # Retorna a posição do elemento na lista
  print("O elemento", elemento, "está na posição", lista.index(elemento)) 
else:
  print("O elemento", elemento, "não está na lista")

 