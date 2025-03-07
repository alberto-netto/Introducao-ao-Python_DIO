def salvar_carro(marca, modelo, ano): #adiciona o carro no banco de dados
    print(f"Carro inserido com sucesso: {marca} / {modelo} / {ano} ")

#salvar_carro("Fiat", "Palio", 2006)
salvar_carro(**{"marca":"Fiat", "modelo" : "Palio", "ano" : 2006})
