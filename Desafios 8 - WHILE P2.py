# Desafio 70

print("-"*50,"\nLOJA SUPER BARATÃO")
print("-"*50)

total = contador_preco = contador = menor = custo = 0
nome = " "

while True:
    produto = str(input("Nome do produto: ")).upper().strip()
    preco = float(input("Preço: R$ "))
    total += preco
    if contador == 0:
        contador += 1
        menor = preco
        nome = produto
        custo = preco
    if preco > 1000:
        contador_preco += 1
    if preco < menor:
        custo = preco
        nome = produto
    escolha = " "
    while escolha not in "SNsn":
        escolha = str(input("Quer continuar ?: [S/N] ")).upper().strip()
    if escolha == "N":
        print("{:-^50}" .format(" FIM DO PROGRAMA "))
        print(f"Total da compra: R$ {total}")
        print(f"Produtos custando mais de R$ 1000.00: {contador_preco}")
        print(f"O Produto mais barato foi {nome} que custa R$ {custo}")
        break




# Desafio 69

soma = contador_idade = contador_homens = contador_mulher = 0

while True:
    print("-"*50,"\nCADASTRE UMA PESSOA")
    print("-"*50)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MFmf":
        sexo = str(input("Sexo: [M/F] ")).upper().strip()
    soma += idade
    if idade > 18:
        contador_idade += 1
    if sexo == "M":
        contador_homens += 1
    if sexo == "F" and idade < 20:
        contador_mulher += 1
    escolha = " "
    while escolha not in "SNsn":
        escolha = str(input("Quer continuar ?: [S/N] ")).upper().strip()
    if escolha == "N":
        print(f"Total de pessoas com mais de 18 anos: {contador_idade}")
        print(f"Total de homens cadastrados: {contador_homens}")
        print(f"Total de mulhers com menos de 20 anos: {contador_mulher}")
        break



# Desafio 68

from random import randint
from time import  sleep

contador = 0

while True:
    print("-" * 50)
    valor = int(input("Digite um número: "))
    escolha = str(input("Par ou Ímpar? [P/I] ")).upper().strip()
    print("-" * 50)
    computador = randint(0, 10)
    soma = valor + computador
    print("Vamos ver quem ganhou?")
    sleep(0.5)
    print("...")
    sleep(0.5)
    if (soma % 2 == 0 and escolha == "I"):
        print("-" * 50)
        print("Você perdeu!!!")
        print(f"Você jogou {valor} e o computador {computador}. O resultado deu {soma} que é PAR")
        print(f"GAME OVER! Você venceu {contador} vezes no total")
        print("-" * 50)
        break
    elif (soma % 2 != 0 and escolha == "P"):
        print("Você perdeu!!!")
        print(f"Você jogou {valor} e o computador {computador}. O resultado deu {soma} que é ÍMPAR")
        print(f"GAME OVER! Você venceu {contador} vezes no total!")
        break
    contador += 1
    print("Você Ganhou!!!")
    print(f"Você jogou {valor} e o computador {computador}. O resultado deu {soma} que é ", end="")
    print("PAR" if escolha == "P" else "ÍMPAR")
    print(f"Vamos jogar de novo? Você venceu {contador} vezes até agora!")





# Desafio 67

while True:
    print("-"*30)
    valor = int(input("Você que ver a tabuada de qual valor? "))
    print("-" * 30)
    if valor < 0:
        print("TABUADA FINALIZADA! \n")
        break
    for i in range(1, 11, 1):
        resultado = valor * i
        print(f"{valor} x {i:2} = {resultado}")



# Desafio 66

valor = contador = 0

numero = int(input("Digite um número [999 para parar]: "))

while True:
    if numero == 999:
        break
    valor += numero
    contador += 1
    numero = int(input("Digite um número [999 para parar]: "))

print(f"Você digitou {contador} números e a soma entre eles foi {valor}.")


valor = contador = 0

while True:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero == 999:
        break
    valor += numero
    contador += 1

print("Você digitou {} números e a soma entre eles foi {}." .format(contador, valor))