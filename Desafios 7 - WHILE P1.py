# Desafios 65

numero = int(input("Digite um número: "))
continua = str(input("Você quer continuar? [S/N] ")).upper().strip()
contador = 1
soma = maior = menor = numero

while continua == "S":
    numero = int(input("Digite um número: "))
    continua = str(input("Você quer continuar? [S/N] ")).upper().strip()
    soma += numero
    contador += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("Você digitou {} números e a media entre eles foi de {}." .format(contador, soma / contador))
print("O maior valor foi {} e o menor foi {}." .format(maior, menor))

# Desafios 64

valor = contador = numero = 0

numero = int(input("Digite um número [999 para parar]: "))

while numero != 999:
    valor += numero
    contador += 1
    numero = int(input("Digite um número [999 para parar]: "))



print("Você digitou {} números e a soma entre eles foi {}." .format(contador, valor))



numero = int(input("Digite um número [999 para parar]: "))

if numero == 999:
    valor = 0
    contador = 0
else:
    valor = numero
    contador = 1

while numero != 999:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero == 999:
        break
    valor += numero
    contador += 1

print("Você digitou {} números e a soma entre eles foi {}." .format(contador, valor))



# Desafios 63

numero = int(input("Qual o tamanho da sequência de Fibonacci? "))

termo1 = 0
termo2 = 1

print("{} -> {}" .format(termo1,termo2), end="")

contador = 3
termo = 0

while contador <= numero:
    termo = termo1 + termo2
    print(" -> {}" .format(termo), end="")
    termo1 = termo2
    termo2 = termo
    contador += 1

print(" -> Fim \n")


# Desafios 62

numero = int(input("Digite um número: "))
razao = int(input("Digite a razão da PA: "))

contador = 1
vezes = 10
soma = 0

while vezes != 0:
    soma += vezes
    contador = 1
    while contador <= vezes:
        print(numero,"-> ", end = "")
        contador += 1
        numero += razao
    print("Pausa \n")
    vezes = int(input("Quantos termos você quer mostrar a mais? "))

print("Processo finalizado com {} termos mostrados!" .format(soma))


# Desafios 61

numero = int(input("Digite um número: "))
razao = int(input("Digite a razão da PA: "))

contador = 1

while contador <= 10:
    print(numero)
    contador += 1
    numero += razao



# Desafios 60

from math import factorial

numero = int(input("Digite um número inteiro e positivo: "))
contagem = numero

print("Calculando {}! = ".format(numero), end="")

while contagem > 1:
    print("{} x " .format(contagem), end="")
    contagem += -1

print("1 = {}" .format(factorial(numero)))

contagem = numero
fatorial = 1

print("Calculando {}! = ".format(numero), end="")

while contagem > 0:
    print("{}" .format(contagem), end="")
    print(" x " if contagem > 1 else " = ", end="")
    fatorial *= contagem
    contagem += -1

print("{}" .format(fatorial), "\n")


# Desafios 59

num1 = int(input("Escolha um número inteiro: "))
num2 = int(input("Escolha outro número inteiro: "))

frase = '''Tarefa:
[1] Somar,
[2] Multiplicar,
[3] Maior,
[4] Novos Números,
[5] Sair do Programa
'''

escolha = 1

while escolha in range(1,6,1):
    print(frase)
    escolha = int(input("Escolha uma das 5 opções acima: "))
    if escolha == 1:
        soma = num1 + num2
        print("A soma é igual a {}" .format(soma))
    elif escolha == 2:
        mult = num1 * num2
        print("A multiplicação é igual a {}" .format(mult))
    elif escolha == 3:
        maximo = max(num1, num2)
        print("O máximo é igual a {}".format(maximo))
    elif escolha == 4:
        num1 = int(input("Escolha um número inteiro: "))
        num2 = int(input("Escolha outro número inteiro: "))
    elif escolha == 5:
        print("Obrigado por testar o programa!")
        break
    else:
        print("Opção Inválida! Tente novamente")
        escolha = 1



# Desafios 58

from random import randint

computador = randint(0, 10)
chute = int(input("Escolha um número de 0 a 10: "))

while chute != computador:
    if chute > computador:
        print("Menos! Tente outra vez... \n")
        chute = int(input("Escolha um número: "))
    else:
        print("Mais! Tente outra vez... \n")
        chute = int(input("Escolha um número: "))

print("Isso. O número exato é igual a {}" .format(computador))



# Desafios 57

sexo = str(input("Digite o seu sexo [M/F]: ")).upper().strip()

while sexo not in ["M","F"]:
    print("Opção Inválida. Tente novamente digitando M ou F, por favor! \n")
    sexo = str(input("Digite o seu sexo [M/F]: ")).upper().strip()

if sexo == "M":
    print("O sexo selecionado foi o Masculino!")
else:
    print("O sexo selecionado foi o Feminino!")