def sacar (valor):
    
    saldo = 500
    
    if saldo >= valor:
        print("Valor sacado!")
    else:
        print("Valor indisponível para saque")
    
    print("obrigado por ser nosso cliente, tenha um bom dia")

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"Seu novo saldo é: {saldo}")

sacar(1000)
depositar(200)