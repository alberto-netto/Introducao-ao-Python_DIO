def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Corsa", 2004, "KPX-7561", marca="Chevrolet", motor="1.6", combustivel="Flex")
#criar_carro(modelo="Corsa", ano=2004, placa="KPX-7561", marca="Chevrolet", motor="1.6", combustivel="Flex")  # inválido