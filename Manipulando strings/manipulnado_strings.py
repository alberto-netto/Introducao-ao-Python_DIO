nome = "AlbertO"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "Olá mundo!      "
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip())
print(texto.lstrip())

menu = "Python"

print("####" + menu + "####")
print(menu.center(14, "#"))
print(menu.center(14))
print("-".join(menu))

nome = "Alberto"
idade = 32
profissao = "Engenheiro Eletricista"
linguagem = "Python"

print(f"Olá, meu nome é {nome}. Tenho {idade} anos, trabalho como {profissao} e estou aprendendo {linguagem}")