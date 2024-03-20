def criarMatriz(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            elemento = int(input("Digite o elemento da linha " + str(i+1) + " e coluna " + str(j+1) + ": "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz
def imprimirMatriz(matriz):
    for linha in matriz:
      print(linha)
def main():
    linha = int(input("Digite o numero de linhas da matriz: "))
    coluna = int(input("Digite o numero de colunas da matriz: "))
    matriz = criarMatriz(linha, coluna)
    imprimirMatriz(matriz)        

main()