# Desafios 45

from random import choice

jogador = str(input("Pedra, Papel ou Tesoura? ")).upper().strip()
computador = choice(["PEDRA","PAPEL","TESOURA"])

if jogador == computador:
    print("Você escolheu {} e o computador também escolheu {}, deu empate!" .format(jogador, computador))
elif jogador == "PEDRA" and computador == "TESOURA":
    print("Você escolheu {} e o computador escolheu {}, você ganhou!" .format(jogador, computador))
elif computador == "PEDRA" and jogador == "TESOURA":
    print("Você escolheu {} e o computador escolheu {}, o computador ganhou!" .format(jogador, computador))
elif jogador == "PAPEL" and computador == "PEDRA":
    print("Você escolheu {} e o computador escolheu {}, você ganhou!" .format(jogador, computador))
elif computador == "PAPEL" and jogador == "PEDRA":
    print("Você escolheu {} e o computador escolheu {}, o computador ganhou!" .format(jogador, computador))
elif jogador == "TESOURA" and computador == "PAPEL":
    print("Você escolheu {} e o computador escolheu {}, você ganhou!" .format(jogador, computador))
elif computador == "TESOURA" and jogador == "PAPEL":
    print("Você escolheu {} e o computador escolheu {}, o computador ganhou!" .format(jogador, computador))
else:
    print("Opção Inválida!")



# Desafios 44

preco = float(input("Digite o preço do produto, R$: "))

print('''Forma de Pagamento:
1 = Dinheiro/Cheque, 
2 = Cartão 1x,
3 = Cartão 2x,
4 = Cartão 3x ou mais''')

pagamento = int(input("Digite a Forma de pagamento:"))

if pagamento == 1:
    print("Preço Inicial = R${:.2f}, Preço Final = R${:.2f}" .format(preco, preco*0.9))
elif pagamento == 2:
    print("Preço Inicial = R${:.2f}, Preço Final = R${:.2f}" .format(preco, preco*0.95))
elif pagamento == 3:
    print("Preço Inicial = R${:.2f}, Preço Final = R${:.2f}, Parcelas = R${:.2f}" .format(preco, preco, preco/2))
elif pagamento == 4:
    parcela = int(input("Quantas parcelas?"))
    print("Preço Inicial = R${:.2f}, Preço Final = R${:.2f}, Parcelas = R${:.2f}" .format(preco, preco*1.2, (preco*1.2)/parcela))
else:
    print("Opção Inválida!")




# Desafios 43

peso = float(input("Digite o seu peso em KG: "))
altura = float(input("Digite a sua altura em Metro(s): "))

imc = peso / (altura ** 2)

print("Seu IMC é de {:.2f}" .format(imc))

if imc < 18.5:
    print("Abaixo do Peso!")
elif imc < 25:
    print("Peso Ideal!")
elif imc < 30:
    print("Sobrepeso!")
elif imc < 40:
    print("Obesidade!")
else:
    print("Obesidade Mórbida!")

# Desafios 42

lado1 = float(input("Digite o comprimento do lado 1: "))
lado2 = float(input("Digite o comprimento do lado 2: "))
lado3 = float(input("Digite o comprimento do lado 3: "))

if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("Não é possível formar um triângulo")
else:
    if lado1 == lado2 == lado3:
        print("É possível formar um triângulo Equilátero")
    elif lado1 != lado2 != lado3 != lado1:
        print("É possível formar um triângulo Escaleno")
    else:
        print("É possível formar um triângulo Isósceles")



# Desafios 41

from datetime import date

ano = int(input("Ano de nascimento: "))
idade = (date.today().year - ano)

if idade <= 9:
    print("Mirim, Idade de {} ano(s)!" .format(idade))
elif idade <= 14:
    print("Infantil, Idade de {} anos!" .format(idade))
elif idade <= 19:
    print("Júnior, Idade de {} anos!" .format(idade))
elif idade <= 25:
    print("Sênior, Idade de {} anos!" .format(idade))
else:
    print("Master, Idade de {} anos!" .format(idade))


# Desafios 40

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("Reprovado! Média de {:.2f} pontos!" .format(media))
elif media >= 5 and media <= 6.9: # 6.9 >= media >=5
    print("Recuperação! Média de {:.2f} pontos!" .format(media))
else:
    print("Aprovado! Média de {:.2f} pontos!" .format(media))



# Desafios 39

from datetime import date

ano = int(input("Ano de nascimento: "))
idade = (date.today().year - ano)

if idade < 18:
    print("Alistamento Futuro! Falta {} ano(s) para o prazo limite!" .format(18 - idade))
elif idade == 18:
    print("Alistamento Imediato! Você precisa se alistar agora!" .format(18 - idade))
else:
    print("Alistamento Atrasaso! Você ultrapassou o prazo limite em {} ano(s)!".format(idade - 18))



# Desafios 38

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))

if numero1 > numero2:
    print("O numero {} é maior que {}" .format(numero1, numero2))
elif numero2 > numero1:
    print("O numero {} é maior que {}" .format(numero2, numero1))
else:
    print("O numero {} é igual ao número {}" .format(numero1, numero2))


# Desafios 37

numero = int(input("Numero: "))
conversao = str(input("Bin, Octal, Hexadecimal: ")).upper().strip()

if conversao == "BIN":
    print("Numero: {}, Bit: {}" . format(numero, bin(numero)[2:]))
elif conversao == "OCTAL":
    print("Numero: {}, Octal: {}" . format(numero, oct(numero)[2:]))
else:
    print("Numero: {}, Hexadecimal: {}" . format(numero, hex(numero)[2:]))



# Desafios 36

casa = float(input("Valor da Casa: "))
salario = float(input("Salário: "))
anos = float(input("Anos: "))

prestacao = casa / (anos * 12)
limite = salario * 0.3

if prestacao > limite:
    print("Empréstimo Negado! A prestação de R${:.2f} ultrapassou o limite de R${:.2f}." .format(prestacao,limite))
else:
    print("O valor da prestacão será de R${:.2f}." .format(prestacao))