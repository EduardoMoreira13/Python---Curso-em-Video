# Desafio 100

from random import sample

lista = list(range(0,101,1))

def sorteio(list, numeros):
    valores = sample(list, k=5)
    print("Sorteando 5 valores da lista: ", end = "")
    for i in valores:
        numeros.append(i)
        print(i, end=" ")
    print("Pronto!")

def pares(list):
    soma = 0
    for i in list:
        if i % 2 == 0:
            soma += i
    print(f"Sorteando os valores pares de {numeros}, temos {soma}.")

numeros = list()
sorteio(lista, numeros)
pares(numeros)


print("\n")


# Desafio 99

from time import sleep

def maior(lista): # poderia não colocar como uma lista (def contagem(*valores))
    print("-"*50,"\nAnalisando os valores...")
    for valores in lista:
        print(valores, end = " ")
        sleep(0.5)
    print(f"Foram informados {len(lista)} valores ao todo.")
    print(f"O maior valor informado foi {max(lista)}.")


maior([2,9,4,5,7,1])
maior([4,7,0])
maior([1,2])
maior([6])
maior([0])


def maior(*num):
    print("-"*50,"\nAnalisando os valores...")
    for valores in num:
        print(valores, end = " ")
        sleep(0.5)
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {max(num)}.")


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()



print("\n")



# Desafio 98

def contagem(*cont): # poderia especificar os parâmetros (def contagem(inicio, final, passo))
    print("-"*40)
    print(f"Contagem de {cont[0]} até {cont[1]} de {cont[2]} em {cont[2]}")
    if cont[0] <= cont[1]:
        for i in range(cont[0], cont[1] + 1, cont[2]):
            print(i, end=" ")
        print("Fim!")
    else:
        for i in range(cont[0], cont[1] - 1, - cont[2]):
            print(i, end=" ")
        print("Fim!")


contagem(1, 10, 1)
contagem(10, 0, 2)
print("-"*40, "\nAgora é sua vez de personalizar a contagem!\n")

inicio = int(input("Início: "))
final = int(input("Final: "))
passo = int(input("Passo: "))

contagem(inicio, final, passo)


print("\n")



# Desafio 97

def texto(msg):
    tamanho = len(msg)
    print("-"*(tamanho + 6))
    print(f"   {msg}")
    print("-" * (tamanho + 6))

texto("Eduardo Moreira")
texto("Curso em Vídeo: Python - Mundo 3")
texto("Edu")


# Desafio 96

def area(l, c):
    print(f"A área de um terreno {l}x{c} é de {l*c:.2f}m2")



print("-" * 30, "\nControle de Terrenos")
print("-" * 30)
largura = int(input("Largura (m) = "))
comprimento = int(input("Comprimento (m) = "))
area(largura, comprimento)


def area():
    print("-"*30,"\nControle de Terrenos")
    print("-" * 30)
    largura = int(input("Largura (m) = "))
    comprimento = int(input("Comprimento (m) = "))
    print(f"A área de um terreno {largura}x{comprimento} é de {largura*comprimento:.2f}m2")



area()



def area(largura, comprimento):
    print("-"*30,"\nControle de Terrenos")
    print("-" * 30)
    print(f"A área de um terreno {largura}x{comprimento} é de {largura*comprimento:.2f}m2")



area(10, 5)