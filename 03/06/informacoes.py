from datetime import date

nome = "Vitor Muneretto Tinelli"
dataNascimento = "20/04/2006"
cidade = "Criciúma"
estado = "Santa Catarina"
data = date.today()
idade = date.today().year - 2006
if (data.month < 4) or (data.month == 4 and data.day < 20):
    idade = idade - 1


print ("Nome: ", nome)
print ("Data de nascimento: ", dataNascimento, "Idade: ", idade, " anos")
print ("Cidade: ", cidade)
print ("Estado: ", estado)