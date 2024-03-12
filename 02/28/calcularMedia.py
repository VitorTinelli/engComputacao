notas = input("Digite as notas separadas por virgula: ")
notas = notas.split(",")

for nota in range(notas.__len__()):
  notas[nota] = float(notas[nota])

media = (sum(notas)) / notas.__len__()

print("A média é aritimética das notas é:", media)
if (media >= 6):
  print("Aprovado")
else:
  print("Reprovado")