import math
raioHexagono = float(input("Digite o valor do raio do hexágono: "))
anguloInterno = 120 #Todo hexagono tem angulos internos de 120 graus

angulosRadianos = math.radians(30)
ladoHexagono = 2 * raioHexagono * math.sin(angulosRadianos)
areaHexagono = (3 * math.sqrt(3) /2 ) * ladoHexagono**2

print("A área do hexágono é: {:.2f}".format(areaHexagono))