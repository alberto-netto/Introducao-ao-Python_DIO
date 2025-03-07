saldo = 2000.00

def saque(valor):
    valor = float(input("Informe o valor do saque:"))
    global saldo
    saldo = saldo - valor
    return saldo
print(f"Obrigado por ser nosso cliente, seu novo saldo é de {saldo}")

def deposito(valor):
    valor = float(input("Informe o valor a ser depositado: "))
    global saldo
    saldo = valor + saldo
    return saldo

menu = int(input("Informe a opção a ser realizada: \n [1] Saque \n [2] Depósito \n [3] Extrato \n"))

if menu == 1:
    if valor > saldo:
        print(f"Não foi possível realizar seu saque, seu saldo é de {saldo}")
    else:
        saque(valor)

elif menu == 2:
    deposito()

elif menu == 3:
    print(f"Seu saldo é de {saldo}")


print("Obrigado por ser nosso cliente")