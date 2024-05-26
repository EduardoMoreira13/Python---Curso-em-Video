# Desafio 56

soma = 0
contador = 0
nome_homem = ""

for i in range(1, 5, 1):
    nome = str(input("Digite o seu nome: ")).upper().strip()
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Digite seu sexo: M ou F ?")).upper().strip()
    soma += idade
    print("-"*20)
    if sexo == "F" and idade < 20:
            contador += 1
    if i == 1 and sexo == "M":
        maior = idade
        nome_homem = nome
    if sexo == "M" and idade >= maior:
        maior = idade
        nome_homem = nome


print("A média de idade é de {:.2f} anos para o grupo!" .format(soma / 4))
print("O homem mais velho tem {} anos e se chama {}!" .format(maior, nome_homem))
print("{} mulheres têm menos de 20 anos de idade!" .format(contador))


# Desafio 55

peso = float(input("Digite o 1° peso: "))
maior = peso
menor = peso

for i in range(2, 6, 1):
    peso = float(input("Digite o {}° peso: " .format(i)))
    if peso > maior:
        maior = peso
    else:
        maior = maior
    if peso < menor:
        menor = peso
    else:
        menor = menor

print("{:.2f}Kg é o menor peso e {:.2f}Kg é o maior peso!" .format(menor, maior))


# Desafio 54

from datetime import date

maiores = 0
menores = 0

for i in range(1, 8, 1):
    ano = int(input("Digite o ano de nascimento: "))
    idade = (date.today().year - ano)
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print("{} menores de idade e {} maiores de idade!" .format(menores, maiores))


# Desafio 53

frase = str(input("Digite uma frase: ")).upper().strip().split() # Maiuscula, Trim e Dividir em palavras

frase = "".join(frase)

inverso = ""

for i in range(len(frase) - 1, -1,-1):
    inverso += frase[i]

print(frase)
print(inverso)
print(frase[::-1])

if inverso == frase:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")


# Desafio 52

numero = int(input("Digite um número: "))

for i in range(2, numero, 1):
    if numero % i == 0:
        resultado = "Esse número não é Primo!"
        print("Divisível por {}" .format(i))
        break
    else:
        resultado = "Esse número é Primo!"

print(resultado)

# Desafio 51

numero = int(input("Digite um número: "))
razao = int(input("Digite a razão da PA: "))

for i in range(numero, (razao * 10 + numero) - 1, razao):
    print(i)




# Desafio 50

soma = 0
contador = 0

for indice in range(1,7,1):
    valor = int(input("Digite o {}° número: " .format(indice)))
    if valor % 2 == 0:
        soma += valor
    contador += 1

print("Você digitou {} números e a soma dos pares deu {}" .format(contador,soma))




valores = str(input("Digite 6 números: ")).split(" ")

print(valores)

soma = 0

for i in valores:
    i = int(i)
    if i % 2 == 0:
        soma += i

print(soma)



# Desafio 49

valor = int(input("Digite um número: "))

for i in range(1, 11, 1):
    resultado = valor * i
    print("{} x {:2} = {}" .format(valor, i, resultado))


# Desafio 48

soma = 0

for i in range(3, 500, 3):
    if i % 2 != 0:
        soma += i

print(soma)


# Desafio 47

for i in range(2, 51, 2):
    print(i, end = " ")

valores = []

for i in range(2, 51, 2):
    valores.append(i)

print("\n")
print(valores)
print("\n")
print("Fim!")



# Desafio 46

from time import sleep

for i in range(10,-1,-1):
    sleep(1)
    print(i)

print("Feliz Ano Nono!")