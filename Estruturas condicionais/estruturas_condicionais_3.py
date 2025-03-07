conta_normal = False
conta_universitaria = False

saque = float(input("Digite o valor do saque: "))
saldo = 2000
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print(f"Saque de {saque} realizado com sucesso!")
    
    elif saque <= (saldo + cheque_especial):
        print(f"Saque realizado com o uso do cheque especial foram utilizados {saque - saldo} do crédito em cheque especial")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
        
else:
    print("Tipo de conta não reconhecida, entre em contato com o gerente por gentileza")