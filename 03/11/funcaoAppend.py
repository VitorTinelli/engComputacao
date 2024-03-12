import os, time

# Função para inserir elementos em uma lista 
def inserirElementos(lista, elemento):
    try:
        lista.append(elemento)
        print(f"Elemento {elemento}, inserido com sucesso!")
    except:
        print("Erro ao inserir elemento")	

# Função principal
def main():
    # Cria uma lista vazia
    lista = []
    while(True):
        # Menu de opções
        print("\n1 - Inserir Elemento")
        print("2 - Sair")
        op = int(input("Digite a opção: "))
        if op == 1:
            pass
        elif op == 2:
            break
        else:
            print("Opção inválida!")
            continue
        # Lê o elemento a ser inserido e chama a função para inserir o elemento na lista
        elemento = input("Digite o elemento: ")
        inserirElementos(lista, elemento)

        # Apos 1.5 segundos limpa a tela e mostra a lista atual
        time.sleep(1.5)
        os.system('cls')
        print(f"Lista atual: {lista}")

if __name__ == "__main__": # Verifica se o script é o principal
  main() # Chama a função principal