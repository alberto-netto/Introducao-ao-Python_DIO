maior_idade = 18

idade = int(input("Informe a sua idade: "))

if idade >= maior_idade:
    print("Você é maior de Idade e está apto a tirar sua habilitação")

elif idade >= 16:
    print("Você pode dar entrada no processo e fazer as aulas teóricas, mas só poderá tirar a habilitação após completar 18 anos")
else:
    print("Você é menor de idade, não pode tirar sua habilitação")