import math
diametro = float(input("Digite o diâmetro (cm): "))
velocidade = float(input("Digite a velocidade do fluido (m/s): "))

area = math.pi * (diametro/2)**2 / 10000
fluxo = area * velocidade
vazao = fluxo * 3600

print("A vazão do fluido é: {:.2f}m³/h".format(vazao))