#texto = input("informe um texto: \n")
texto = ""
VOGAIS = "AEIOU"

#exemplo utilizando um iterável
for canalha in texto:
    if canalha.upper() in VOGAIS:
        print(canalha, end=" ")

print()

# exemplo da função built-in range
for numero in range(0, 41, 4):
    print(numero, end=" ")

