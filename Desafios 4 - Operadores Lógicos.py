# Desafio 35

lado1 = float(input("Digite o comprimento do lado 1: "))
lado2 = float(input("Digite o comprimento do lado 2: "))
lado3 = float(input("Digite o comprimento do lado 3: "))

if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("Não é possível formar um triângulo")
else:
    print("É possível formar um triângulo")


# Desafio 34

salario = float(input("Digite seu salário: "))

if salario > 1250.00:
    print("Salário novo: {:.2f}" .format(salario * 1.1))
else:
    print("Salário novo: {:.2f}".format(salario * 1.15))


# Desafio 33

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

menor = num1

if num2 < menor and num2 <= num3:
    menor = num2
if num3 < menor and num3 <= num2:(
    menor) = num3

maior = num1

if num2 > maior and num2 >= num3:
    maior = num2
if num3 > maior and num3 >= num2:
    maior = num3

print("Menor: {}, Maior: {}" .format(menor, maior))



# Desafio 32

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("Ano Bissexto!")
else:
    print("Não é Ano Bissexto")


# Desafio 31

viagem = int(input("Digite a distância de sua viagem: "))

if viagem <= 200:
    print("O valor da passagem é de R${:.2f}!" . format(viagem * 0.5))
else:
    print("O valor da passagem é de R${:.2f}!".format(viagem * 0.45))



# Desafio 30

numero = int(input("Digite um número: "))

if numero % 2  == 0:
    print("O numero {} é Par!" . format(numero))
else:
    print("O numero {} é Ímpar!".format(numero))


# Desafio 29

velocidade = float(input("Digite sua velocidade (KM/H): "))

if velocidade > 80:
    diferenca = velocidade - 80
    print(''' Você foi multado! Sua velocidade foi de {} KM/H, excendendo em {} KM/H acima do permitido. 
    O valor da multa é igual a R$ {:.3f}''' .format(velocidade, diferenca, diferenca * 7))
else:
    print("Tenha um bom dia!")



# Desafio 28

from random import randint
from time import sleep

chute = int(input("Digite um numero entre 0 e 5: "))

numero = randint(0,5)

print("Vamos ver o resultado?")
sleep(2)

if chute == numero:
    print("Você acertou, Parabéns!")
else:
    print("Você errou, Não foi dessa vez! O numero correto era {}" .format(numero))