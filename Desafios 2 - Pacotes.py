# Desafio 20

from random import shuffle

alunos = ["Eduardo", "Ana", "Maria", "Davi"]

shuffle(alunos)

print("Alunos: ", alunos)



# Desafio 19

from random import randint, choice

alunos = ["Eduardo", "Ana", "Maria", "Davi"]

numero = randint(0,3)
escolha = choice(alunos)

print("Alunos: ", alunos[0], alunos[1], alunos[2], alunos[3], "\n", "Sorteio: ", numero, alunos[numero])
print("Alunos: ", alunos[0], alunos[1], alunos[2], alunos[3], "\n", "Sorteio: ", escolha)


# Desafio 18

from math import sin, cos, tan, radians

angulo = float(input('Digite um numero: '))
angulo = radians(angulo)
print(sin(angulo),cos(angulo),tan(angulo))



# Desafio 17

from math import sqrt

cateto_op = float(input('Digite um numero: '))
cateto_ad = float(input('Digite um numero: '))

hipotenusa = sqrt(pow(cateto_op,2) + pow(cateto_ad,2))
print("{:.3f}" .format(hipotenusa))

from math import hypot

hipotenusa = hypot(cateto_op, cateto_ad)
print("{:.3f}" .format(hipotenusa))




# Desafio 16

from math import floor

num = float(input('Digite um numero: '))
arredondamento = floor(num)
print("{} {}" .format(num, arredondamento))

# Uso de Modulos

import math

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(raiz)

from math import sqrt, floor

num = int(input('Digite um numero: '))
raiz = sqrt(num)
arredondamento = floor(raiz)
print("{} {}" .format(raiz, arredondamento))