pv = float(input("Digite o valor do investimento: "))
n = int(input("Digite o número de meses: "))
i = float(input("Digite a rentabilidade: "))

fv = pv * ((1 + (i / 100 / 12)) ** n)

print("O valor final do investimento é: {:.2f}".format(fv))
