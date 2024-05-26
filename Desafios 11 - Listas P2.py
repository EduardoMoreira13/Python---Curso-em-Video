# Desafio 89

from statistics import mean

base = list()   # Estrutura de input e controle
lista = list()
continua = " "
contador = 0

while True:
    base.append(str(input(f"Nome: ")).strip().capitalize())
    base.append(float(input(f"Nota 1: ")))
    base.append(float(input(f"Nota 2: ")))
    lista.append(base[:])
    base.clear()
    contador += 1
    while continua not in "SN":
        continua = str(input(f"Quer continuar? [S/N]")).upper().strip()
    if continua == "N":
        break
    continua = " "

print("-"*50)

print(f"{"N°":<3} {"NOME":10} {"MÉDIA":>5}")

for i in range(0, contador, 1):
    media = mean(lista[i][1:])
    print(f"{i:<3} {lista[i][0]:10} {media:>5.2f}")

print("-"*50)

while True:
    num = int(input(f"Mostrar notas de qual aluno? (999 para interromper)"))
    if num == 999:
        break
    print(f"Notas de {lista[num][0]} são {lista[num][1:]}")
    print()


print("-"*50)
print("\n")



# Desafio 88

from random import sample
from time import sleep

print("-"*50, "\n                JOGA NA MEGA SENA")
print("-"*50)

quantidade = int(input(f"Quantos jogos você quer fazer? "))
lista = list()

# for i in range(0, quantidade, 1): # Geração das listas de forma automática
#    lista.append([])

print("Gerando os jogos...")
sleep(2)

for i in range(0, quantidade, 1):
    lista.append(sorted(sample(range(1, 61), 6)))
    print(f"Jogo {i + 1}: {lista[i]}")
    sleep(0.5)

print()
print("-"*10, "< BOA SORTE! >", "-"*10)
print("\n")



# Desafio 87

num1 =[0,0,0,1,1,1,2,2,2]
num2 =[0,1,2,0,1,2,0,1,2]
lista = [[],[],[]]

for intervalo in range(0,9,1):
    valor = int(input(f"Digite um valor para [{num1[intervalo]},{num2[intervalo]}]: "))
    if intervalo in (0,1,2):
        lista[0].append(valor)
    elif intervalo in (3,4,5):
        lista[1].append(valor)
    else:
        lista[2].append(valor)

for inter in range(0,3,1):
    for intervalo in range(0,3,1):
        print(f"{[ lista[inter][intervalo] ]}", end = "")
    print()

soma1 = soma2 = maior = 0

for inter in range(0,3,1):
    for intervalo in range(0,3,1):
        if lista[inter][intervalo] % 2 == 0:
            soma1 += lista[inter][intervalo]
        if intervalo == 2:
            soma2 += lista[inter][intervalo]
        if inter == 1 and lista[inter][intervalo] > maior:
            maior = lista[inter][intervalo]

print(f"soma dos valores pares da matriz: {soma1}")
print(f"soma dos valores da terceira coluna da matriz: {soma2}")
print(f"maior valor da segunda linha: {maior}")
print(f"\n")



# Desafio 86

num1 =[0,0,0,1,1,1,2,2,2]
num2 =[0,1,2,0,1,2,0,1,2]
lista = [[],[],[]]

for intervalo in range(0,9,1):
    valor = int(input(f"Digite um valor para [{num1[intervalo]},{num2[intervalo]}]: "))
    if intervalo in (0,1,2):
        lista[0].append(valor)
    elif intervalo in (3,4,5):
        lista[1].append(valor)
    else:
        lista[2].append(valor)

for inter in range(0,3,1):
    for intervalo in range(0,3,1):
        print(f"{[ lista[inter][intervalo] ]}", end = "")
    print()





# Desafio 85

lista = [list(),list()]
contador = 0

while True:
    num = (int(input(f"Digite o {contador + 1}° número: ")))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
    contador +=1
    if contador == 7:
        break

print(lista)
print(f"Os números pares digitados foram: {lista[0]}")
print(f"Os números ímpares digitados foram: {lista[1]}")



# Desafio 84

base = list()   # Estrutura de input e controle
lista = list()
continua = " "

while True:
    base.append(str(input(f"Nome: ")).strip().capitalize())
    base.append(float(input(f"Peso: ")))
    lista.append(base[:])
    base.clear()
    while continua not in "SN":
        continua = str(input(f"Quer continuar? [S/N]")).upper().strip()
    if continua == "N":
        break
    continua = " "


peso = list()  # Estrutura para obter máximo e mínimo

for valor in range(0, len(lista), 1):
    peso.append(lista[valor][1])


print(f"Você cadastrou {len(lista)} pessoas!") # Estrutura de print do peso e nome
print(f"O maior peso foi de {max(peso)}Kg. Peso de ", end = "")
for valor in range(0, len(lista), 1):
    if lista[valor][1] == max(peso):
        print([lista[valor][0]], end="")
print("\n")
print(f"O menor peso foi de {min(peso)}Kg. Peso de ", end = "")
for valor in range(0, len(lista), 1):
    if lista[valor][1] == min(peso):
        print([lista[valor][0]], end="")
print("\n")