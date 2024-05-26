# Desafios 83

expressao = str(input("Digite sua expressão: "))
lista = []

for letra in expressao:
    if letra in "()":
        lista.append(letra)

print(lista)

print("Expressão Válida" if lista.count('(') == lista.count(')') else "Expressão Inválida")



# Desafios 82

lista = []
continua = " "

while True:
    num = int(input(f"Digite um número: "))
    lista.append(num)
    while continua not in "SN":
        continua = str(input(f"Quer continuar? [S/N]")).upper().strip()
    if continua == "N":
        break
    continua = " "

pares = [x for x in lista if (x % 2) == 0]
impares = [x for x in lista if (x % 2) != 0]

print(f"Lista Completa: {lista}")
print(f"Lista de Pares: {pares}")
print(f"Lista de Ímpares: {impares}")
print("\n")


# Desafios 81

lista = []
continua = " "

while True:
    num = int(input(f"Digite um número: "))
    lista.append(num)
    while continua not in "SN":
        continua = str(input(f"Quer continuar? [S/N]")).upper().strip()
    if continua == "N":
        break
    continua = " "

print(f"Você digitou {len(lista)} elemento(s)!")
print(f"Os valores em ordem decrescente são {sorted(lista, reverse=True)} ")
print("O valor 5 faz parte da lista!" if 5 in lista else "O valor 5 não faz parte da lista!")
print("\n")


# Desafios 80

contador = 0
lista = []

while True:
    num = int(input(f"Digite um valor: "))
    lista.append(num)
    contador += 1
    if contador == 5:
        break

print(lista)

lista2 = []

for i in range(1,6):
    minimo = min(lista)
    lista2.append(minimo)
    lista.remove(minimo)

print(lista2)
print("\n")



# Desafios 79

lista = []
continua = " "

while True:
    num = int(input(f"Digite um número: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso!")
    elif num in lista:
        print("Valor duplicado! Não vou adicionar...")
    while continua not in "SN":
        continua = str(input(f"Quer continuar? [S/N]")).upper().strip()
    if continua == "N":
        break
    continua = " "

print(f"Você digitou os seguintes valores: {sorted(lista)}")
print("\n")


# Desafios 78

contador = 0
lista = []

while True:
    num = int(input(f"Digite um valor para a posição {contador}: "))
    lista.append(num)
    contador += 1
    if contador == 5:
        break

print(f"Você digitou os valores: {lista}")

menor = sorted(lista)[0]
menor = min(lista)
maior = sorted(lista, reverse=True)[0]
maior = max(lista)

print(f"O menor valor digitado foi {menor} na posição {lista.index(menor)}")
print(f"O maior valor digitado foi {maior} na posição {lista.index(maior)}")

indices_menor = [i for i, x in enumerate(lista) if x == menor]
indices_maior = [i for i, x in enumerate(lista) if x == maior]

print(f"O menor valor digitado foi {menor} nas posições {indices_menor}")
print(f"O maior valor digitado foi {maior} na posições {indices_maior}")

print("\n")


# Aula

lista = ["Eduardo", "Ana", "Maria"]
print(lista)

lista.append("Adriana") # adicionar
print(lista)

lista[3] = "Fernando" # substituir
print(lista)

lista.insert(1, "Moreira") # adicionar em um local específico
print(lista)

del lista[4] # deletando por posição
print(lista)

lista.pop(1) # deletando por posição
print(lista)

lista.remove('Ana') # deletando por especificacao do valor
print(lista)