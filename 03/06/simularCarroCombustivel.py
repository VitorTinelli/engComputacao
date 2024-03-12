valorCombustivel = 4.95
kmPorLitro = 20
dinheiro = float(input("Digite quanto dinheiro você tem: "))

litros = dinheiro / valorCombustivel
km = litros * kmPorLitro

print("Você pode andar {:.2f}km com os {:.2f}L que podes abastecer".format(km, litros))

