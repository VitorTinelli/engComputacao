precoProduto = float(input("Digite o preço do produto: "))
desconto = 0.8
precoFinal = precoProduto * desconto

print("O preço final do produto é: {:.2f}".format(precoFinal))
print("O desconto foi de: {:.2f}".format(precoProduto - precoFinal))
print("O preço original do produto era: {:.2f}".format(precoProduto))