opcao = -1
saldo = 2000

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair \n: "))

    if opcao == 1:
        saque = float(input("Digite o valor a ser sacado:\n"))
        if saque < saldo:
            print("Sacando")
            novo_saldo = saldo - saque
            print(f"Novo Saldo R$ {novo_saldo}")
        else:
            print("Não é possível sacar essa quantia!")
    elif opcao ==2:
        print("Exibindo Extrato")
        print(f"R$ {saldo}")
else: 
    print("Obrigado por utilizar nosso sistema")