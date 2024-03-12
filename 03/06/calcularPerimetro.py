import math

raio = float(input("Digite o raio do círculo: "))

perimetro = 2 * math.pi * raio
area = math.pi * raio**2

print("O perímetro do círculo é: {:.2f}".format (perimetro))
print("A área do círculo é: {:.2f}".format(area))