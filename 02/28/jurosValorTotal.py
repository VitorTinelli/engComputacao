fv = float(input("Digite o valor final do investimento: "))
n = int(input("Digite o número de meses: "))
i = float(input("Digite a rentabilidade: "))

pv = fv / ((1 + (i / 100 )) ** n)
print("O valor do investimento é: {:.2f}".format(pv))