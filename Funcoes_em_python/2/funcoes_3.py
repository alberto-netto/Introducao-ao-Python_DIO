salario = 2000


def salario_bonus(bonus):
    global salario

    lista_aux = lista_aux.copy()
    
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")

    salario += bonus
    return salario

lista = [1]
novo_salario = salario_bonus(500, lista)
print(novo_salario) 
print(lista)