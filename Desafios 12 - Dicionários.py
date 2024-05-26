# Desafio 95

dados = dict()
gols = list()
geral = list()
continua = " "

while True:
    dados["Nome"] = str(input("Nome do Jogador: ")).title().strip()
    dados["Partidas"] = int(input(f"Quantas partidas {dados["Nome"]} jogou? "))
    for iteracao in range(1, dados["Partidas"] + 1, 1):
        gols.append(int(input(f"   Quantos gols na partida {iteracao}? ")))
    dados["Gols"] = gols[:]
    dados["Total"] = sum(gols)
    gols.clear()
    geral.append(dados.copy()) # não precisa dar clear nos dicionarios, apenas nas listas
    while continua not in "SN":
        continua = str(input(f"Quer continuar? [S/N]")).upper().strip()
    if continua == "N":
        break
    continua = " "

print("*"*50)
print(geral)

print("-"*50)
print(f"{"Cod":3} {"Nome":10} {"Gols":20} {"Total":<10}")
print("-"*50)

for i in range(0, len(geral), 1):
    gols = str(geral[i]["Gols"])
    print(f"{i:<3} {geral[i]["Nome"]:<10} {gols:20} {geral[i]["Total"]:<2}")

print("-"*50)


while True:
    num = int(input("Mostrar dados de qual jogador? (999 para interromper!) "))
    if num == 999:
        print("-" * 50)
        break
    print(f"-- Levantamento do jogador {geral[num]["Nome"]}: ")
    for i, v in enumerate(geral[num]["Gols"]):
            print(f"   --> Na partida {i + 1}, fez {v} gols.")
    print("-" * 50)









# Desafio 94

from statistics import mean

base = dict()   # Estrutura de input e controle
lista = list()
continua = " "

while True:
    base["Nome"] = str(input(f"Nome: ")).strip().upper()
    base["Sexo"] = str(input(f"Sexo: [M/F] ")).strip().upper()
    while base["Sexo"] not in "MF":
        print("ERRO! Por favor, digite apenas M ou F.")
        base["Sexo"] = str(input(f"Sexo: [M/F] ")).strip().upper()
    base["Idade"] = float(input(f"Idade: "))
    lista.append(base.copy())
    base.clear()
    continua = str(input(f"Quer continuar? [S/N]")).upper().strip()
    while continua not in "SN":
        print("ERRO! Por favor, digite apenas M ou F.")
        continua = str(input(f"Quer continuar? [S/N]")).upper().strip()
    if continua == "N":
        break

print("\n")

print(f"A) Ao todo temos {len(lista)} pessoas cadastradas.")
valores = []

for i in range (0,len(lista)):
    valores.append(lista[i]["Idade"])

print(f"B) A média de idade é de {mean(valores):.2f} anos.")

# mulheres = []
# acima_media = []

# for i in range (0,len(lista)):
#     if lista[i]["Sexo"] == "F":
#         mulheres.append(lista[i]["Nome"])
#     if lista[i]["Idade"] > mean(valores):
#         acima_media.append(lista[i])

print(f"C) As mulheres cadastradas foram ", end = " ")
for i in range(0, len(lista)):
        if lista[i]["Sexo"] == "F":
            print(f"{lista[i]["Nome"]}; ", end = " ")

print("")
print(f"D) Lista de pessoas acima da média:")
for i in range(0, len(lista)):
    if lista[i]["Idade"] > mean(valores):
        print(f"    Nome = {lista[i]["Nome"]} ; Sexo = {lista[i]["Sexo"]} ; Idade = {lista[i]["Idade"]}")



print("\n")



# Desafio 93

dados = dict()
gols = list()

dados["Nome"] = str(input("Nome do Jogador: ")).title().strip()
partidas = int(input(f"Quantas partidas {dados["Nome"]} jogou? "))

if partidas == 0:
    dados["Gols"] = [0]
    dados["Total"] = 0
else:
    for iteracao in range(1, partidas + 1,1):
        gols.append(int(input(f"   Quantos gols na partida {iteracao}? ")))
    dados["Gols"] = gols[:]
    dados["Total"] = sum(gols)

print("-"*50)
print(dados)


print("-"*50)
for k, v in dados.items():
    print(f"O campo {k} tem o valor {v}")

print("-"*50)
print(f"O jogador {dados["Nome"]} jogou {partidas} partidas:")

for i,v in enumerate(dados["Gols"]):
    if partidas > 0:
        print(f"   --> Na partida {i + 1}, fez {v} gols.")

print(f"Foi um total de {dados["Total"]} gols.")
print("-"*50)


print("\n")


# Desafio 92

from datetime import datetime

dados = dict()
dados["Nome"] = str(input("Nome: ")).title().strip()
dados["Idade"] = datetime.now().year - int(input("Ano de Nascimento: "))
dados["CTPS"] = int(input("Carteira de Trabalho (0 não tem): "))

if dados["CTPS"]  == 0:
    for k, v in dados.items():
        print(f"{k} tem o valor {v}")
else:
    dados["Contratação"] = int(input("Ano de Contratação: "))
    dados["Salário"] = int(input("Salário: R$ "))
    dados["Aposentadoria"] = dados["Idade"] + ((dados["Contratação"] + 35) - datetime.now().year)
    for k, v in dados.items():
        print(f"{k} tem o valor {v}")

print("\n")


# Desafio 91

from time import sleep
from random import randint
from operator import itemgetter

jogador = dict()
ranking = list()
valor = 0

print("Valores sorteados: ")
sleep(0.5)

for iteracao in range(1,5,1):
    jogador[iteracao] = valor = randint(1,6)
   # print(f"Jogador {iteracao} tirou {valor} no dado.")
   # sleep(0.5)

for k,v in jogador.items():
    print(f"Jogador {k} tirou {v} no dado.")
    sleep(0.5)

print(jogador)
ranking = sorted(jogador.items(), key = itemgetter(1), reverse=True) # ordenação de dicionário
          # sorted(jogador.items(), key = lambda item: item[1], reverse=True))
print(ranking)

print("== RANKING DOS JOGADORES ==")
for i,v in enumerate(ranking):
    print(f"{i+1}° lugar: jogador {v[0]} com {v[1]}")



# Desafio 90

dicionario = dict()
dicionario["Nome"] = str(input("Nome: ")).title().strip()
dicionario["Media"] = float(input(f"Média de {dicionario["Nome"]}: "))

if dicionario["Media"] < 5:
    dicionario["Situação"] = "Reprovado"
elif dicionario["Media"] <= 6.9:
    dicionario["Situação"] = "Recuperação"
else:
    dicionario["Situação"] = "Aprovado"


print(dicionario)

for k,v in dicionario.items():
    print(f"{k} é igual a {v}")

print("\n")


# Aula

dicionario = {"Nome":"Eduardo", "Idade":27, "Curso":"Estatística"}
print(dicionario)
print(dicionario.values())
print(dicionario.items())
print(dicionario.keys())
print(dicionario["Nome"])


for k,v in dicionario.items():
    print(f"{k}: {v}")

dicionario["Nome"] = "Carlos" # Alterando variável
print(dicionario["Nome"])
dicionario["Peso"] = 78.3 # Adicionando informação
print(dicionario)
del dicionario["Peso"] # deletando informação
print(dicionario)