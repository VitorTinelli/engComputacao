altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))

imc = peso / (altura**2)

print("O IMC é: {:.2f}".format(imc))