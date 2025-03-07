saldo = 1000
saque = 200
limite = 100
conta_especial = True

liberar_saque = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(liberar_saque)