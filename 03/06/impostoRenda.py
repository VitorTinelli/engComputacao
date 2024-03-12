remuneracao = float(input("Digite sua renda mensal: "))
inss = float(input("Digite o desconto que tera no INSS: "))
dependentes = int(input("Digite o numero de dependentes: "))
deducao = 564.80
deducao_dependentes = dependentes*189.59
deducao_tradicional = deducao_dependentes + inss

valor_base_tradicional = remuneracao - deducao_tradicional
valor_base = remuneracao - deducao

if (valor_base < 2259.20):
    total = valor_base

elif ((valor_base > 2259.20) and (valor_base <= 2826.65)):
    total = (valor_base*0.075) - 169.44

elif ((valor_base > 2826.65) and (valor_base <= 3751.05)):
    total = (valor_base*0.15) - 381.44

elif ((valor_base > 3751.05) and (valor_base <= 4664.68)):
    total = (valor_base*0.2250) - 662.77

elif ((valor_base > 4664.68) and (valor_base <= 99999.99)):
    total = (valor_base*0.2750) - 896.00

if (valor_base < 2259.20):
    total_tradicional = valor_base_tradicional

elif ((valor_base_tradicional > 2259.20) and (valor_base_tradicional <= 2826.65)):
    total_tradicional = (valor_base_tradicional*0.075) - 169.44

elif ((valor_base_tradicional > 2826.65) and (valor_base_tradicional <= 3751.05)):
    total_tradicional = (valor_base_tradicional*0.15) - 381.44

elif ((valor_base > 3751.05) and (valor_base_tradicional <= 4664.68)):
    total_tradicional = (valor_base_tradicional*0.2250) - 662.77

elif ((valor_base_tradicional > 4664.68) and (valor_base_tradicional <= 99999.99)):
    total_tradicional = (valor_base_tradicional*0.2750) - 896.00

print (f"O total qual tera que pagar de Imposo de Renda simplificado sera de: {total:,.2f}")
print (f"O total qual tera que pagar de Imposo de Renda tradicional sera de: {total_tradicional:,.2f}")

if (total == total_tradicional):
    print("Mesmo preço para imposto tradicional ou simplificado")

elif (total > total_tradicional):
    print("O imposto tradicional sai por um valor menor")
else:
    print("O imposto simplificado sai por um valor menor")