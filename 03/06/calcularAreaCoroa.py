import math

raioInterno = float(input("Digite o raio interno: "))
raioExterno = float(input("Digite o raio externo: "))

areaCoroa = math.pi * (raioExterno**2 - raioInterno**2)
print("A área da coroa é: {:.2f}".format(areaCoroa))