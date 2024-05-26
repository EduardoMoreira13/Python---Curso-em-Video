# Desafio 13

salario = float(input("Digite o Salario: "))
print("Salario Inicial: {}, Aumento: {}, Salario Final: {}" .format(salario, salario * 0.15,salario * 1.15))


# Desafio 12

preco = float(input("Digite o preco: "))
print("Preco Inicial: {}, Desconto: {}, Preco Final: {}" .format(preco, preco * 0.05,preco * 0.95))



# Desafio 11

altura = float(input("Digite a altura: "))
base = float(input("Digite a base: "))

area = altura * base
litros = area / 2

print("Area: {}, Litro(s) de Tinta: {}" .format(area, litros))



# Desafio 10

reais = float(input("Digite um valor em reais: "))

print("Voce pode comprar {} dolares" .format(reais / 3.27))



# Desafio 9

numero = int(input("Digite um numero de 0 a 9: "))

for i in range(0,10,1):
    print("{} x {:2} = {} " .format(numero, i, numero * i))




# Desafio 8

valor = float(input("Digite um numero: "))
print("cm e mm: {:.3f} e {:.3f} " .format(valor * 100, valor * 1000))


# Desafio 7

nota1 = float(input("Digite um numero: "))
nota2 = float(input("Digite um numero: "))
media = (nota1 + nota2) / 2

print("Media: {:.3f} " .format(media))


# Desafio 6

numero = float(input("Digite um numero: "))
print("Dobro, Triplo e Raiz Quadrada: {},{} e {:.2f} " .format(numero * 2, numero * 3,pow(numero, 1/2)))


# Desafio 5

numero = int(input("Digite um numero: "))
print("A antecessor e {} e o sucessor {} " .format(numero - 1, numero + 1, ))


# Desafio 4

nome = str(input("Digite um nome: "))
print(type(nome), nome.isalnum(), nome.isnumeric(), nome.islower())


# Desafio 3

num1 = int(input("Digite um Numero: "))
num2 = int(input("Digite um Numero: "))

print("A soma entre %s e %s e igual a %s" % (num1, num2, num1 + num2))
print("A soma entre {} e {} e igual a {}" .format(num1, num2, num1 + num2))

# Desafio 2

Dia = int(input("Dia = "))
Mes = str(input("Mes = "))
Ano = int(input("Ano = "))

print("Voce nasceu no dia %s de %s de %s. Correto?" % (Dia, Mes, Ano))


# Desafio 1

nome = str(input("Qual e o seu nome? "))

print("Ola %s!, Prazer em te conhecer!" %nome)
print("Ola {}!, Prazer em te conhecer!" .format(nome))
