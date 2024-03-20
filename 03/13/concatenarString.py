nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

# lstrip() remove os espacos a esquerda
# rstrip() remove os espacos a direita
nomeCompleto = nome.lstrip().rstrip() + " " + sobrenome.lstrip().rstrip()

print("Seu nome completo é: " + nomeCompleto)