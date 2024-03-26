import time

class PilhaEstatica:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.topo = -1
    self.valores = [None] * self.capacidade

  def pilhaVazia(self):
    print("\n\n\n\n")
    print("Verificando se a Pilha está vazia...")
    time.sleep(1)

    if self.topo == -1:
      return ("A Pilha está vazia")
    return ("A Pilha não está vazia")
  
  def pilhaCheia(self):
    print("\n\n\n\n")
    print("Verificando se a Pilha está cheia...")
    time.sleep(1)
    
    if self.topo == self.capacidade - 1:
      return ("A Pilha está cheia")
    return ("A Pilha não está cheia")
  
  def adicionarElementos(self):
    
    if self.topo == self.capacidade - 1:
      print("\n\n\n\n")
      print("Verificando se a Pilha está cheia...")
      time.sleep(1)
      return("A pilha está cheia")
    else:
      print("\n\n\n\n")
      valor = input("Digite o valor que deseja adicionar: ")
      print("\n\n\n\n")
      print("Adicionando elemento na Pilha...")	
      time.sleep(1)

      self.topo += 1
      self.valores[self.topo] = valor
      return(valor, "adicionado(a) com sucesso")

  def removerElemento(self):
    if self.topo == -1:
      print("\n\n\n\n")
      print("Verificando se a Pilha está cheia...")
      time.sleep(1)
      return ("A Pilha está vazia")
    print("\n\n\n\n")
    print("Removendo elemento da Pilha...")
    time.sleep(1)
    elemento = self.valores[self.topo]
    self.topo -= 1
    return(elemento, "removido(a) com sucesso")

  def imprimirValores(self):
    print("\n\n\n\n")
    print("Verificando se a Pilha está vazia...")
    time.sleep(1)
    if self.topo == -1:
      print("A Pilha está vazia")
    else:
      for i in range(self.topo + 1):
        print(i, "-", self.valores[i])
    print("\n")

  def quantidadeAtualElementos(self):
    print("\n\n\n\n")
    print("Verificando se a Pilha está cheia...")
    time.sleep(1)
    if self.topo == -1:
      return ("A Pilha está vazia")
    return ("Quantidade de elementos na Pilha: ", self.topo + 1)
    
class main:
  capacidade = int(input("Digite a capacidade da Pilha: "))
  pilha = PilhaEstatica(capacidade)
  
  while True:
    print("Menu de opções")
    print("1 - Adicionar elementos")
    print("2 - Remover elementos")
    print("3 - Imprimir elementos")
    print("4 - Verificar se a Pilha está vazia")
    print("5 - Verificar se a Pilha está cheia")
    print("6 - Quantidade de elementos na Pilha")
    print("0 - Sair")

    op = int(input("Digite a opção desejada: "))
    match op:
      case 1:
        print(pilha.adicionarElementos())
      case 2:
        print(pilha.removerElemento())
      case 3:
        pilha.imprimirValores()
      case 4:
        print(pilha.pilhaVazia())
      case 5:
        print(pilha.pilhaCheia())
      case 6:
        print(pilha.quantidadeAtualElementos())
      case 0:
        print("Programa encerrado")
        break
      case default:
        print("Opção inválida")

if __name__ == "__main__":
  main()

  

