#capa = 24,95
#livraria = 0.35% desconto
#transporte = 3 (primeiro livro) + 0.75 (livros adicionais)

x = int(input("Digite a quantidade de livros: "))
if (x > 1):
  valor = (24.95 * 0.65 * x) + (3 + 0.75*(x-1))
elif (x == 1):
  valor = (24.95 * 0.65) + 3
else:
  print("Valor inválido")
  exit()
print("O valor total é: {:.2f}".format(valor))
