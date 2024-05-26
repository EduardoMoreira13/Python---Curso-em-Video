# Desafios 77

listagem = ('Lapis', 'Caderno', 'Caneta', 'Borracha', 'Apontador', "Tyr")
vogais = ""

for palavras in listagem:
    for letras in palavras:
        if letras in "aeiou":
            vogais += letras + " "
    print(f"Na palavra {palavras} temos as vogais {vogais}")
    vogais = ""



# Desafios 76

listagem = ("Lápis", 2.00, "Caderno", 10.00, "Caneta", 4.00, "Borracha", 0.50, "Apontador", 5.00)

tupla1 = listagem[0::2]
tupla2 = listagem[1::2]

print(tupla1)
print(tupla2)

for valor in range(0, 5, 1):
    print(f"{tupla1[valor]:10} {"-"*50} R$ {tupla2[valor]:.2f}")

for valor in range(0, 5, 1):
    print(f"{tupla1[valor]:10} {"-"*50} R$ {tupla2[valor]:>5.2f}")


# Desafios 75

contador = 1
tupla = ()

while True:
    num = tuple([input(f"Digite o {contador}° número: ")])
    tupla += num
    contador += 1
    if contador == 5:
        break

tupla = tuple(int(valor) for valor in tupla) # convertendo em inteiros

print(f"Você digitou os valores: {tupla}")
print(f"O 9 apareceu {tupla.count(9)} vezes")
print(f"O {tupla[1]} apareceu na posição 2")
print("Valores pares: ", end="")
for valores in tupla:
    if valores % 2 == 0:
        print(f"{valores} ", end="")

print( "\n", "-"*80, "\n")



# Desafios 74

from random import sample, choices

valores1 = sample(range(1, 101), 5) # AAS sem reposição
valores2 = choices(range(1, 101), k=5) # AAS com reposição

print(f" Valores sorteados: {valores1}")
print(f" Menor valor sorteado: {sorted(valores1)[0]}")
print(f" Maior valor sorteado: {sorted(valores1, reverse=True)[0]} ")

print("-"*80, "\n")

print(f" Valores sorteados: {valores2}")
print(f" Menor valor sorteado: {min(valores2)}")
print(f" Maior valor sorteado: {max(valores2)} ")

print("-"*80, "\n")


# Desafios 73

times = ("Flamengo", "Internacional", "Atlético Mineiro", "São Paulo", "Fluminense", "Grêmio", "Palmeiras",
         "Santos", "Athletico Paranaense", "Red Bull Bragantino", "Ceará", "Corinthians", "Atlético Goianiense",
         "Bahia", "Sport Recife", "Fortaleza", "Vasco da Gama", "Goiás", "Coritiba","Botafogo")

print(f"Times do Brasileirão: {times}")

print(f"G6 para libertadores: {times[0:6]}")

print(f"Rebaixados: {times[-4:]}")

print(f"Ordem Alfabética: {sorted(times)}")

print(f"São Paulo, Posição: {times.index("São Paulo") + 1}")



# Desafios 72

numero = 30

while numero not in range(0,21,1):
    numero = int(input("Digite um número de 0 a 20: "))

valores = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez",
           "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

print(f"Você escolheu o número {numero} ({valores[numero]})!")