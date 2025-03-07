nome = "Alberto"
idade = 32
profissao = "Engenheiro Eletricista"
linguagem = "Python"
exp = "RRC Power & Energy"

dados = {"nome": "Alberto", "idade": 32}

print("Nome: %s Idade: %d" %(nome, idade))

print("Nome: {} Idade {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome:{1}{1}".format(idade, nome))

print("Nome: {nome} Idade {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade {age} {name} {name} {name}".format(name=nome, age=idade))

print(f"Nome: {nome} Idade: {idade} Ultima Empresa: {exp} ")
