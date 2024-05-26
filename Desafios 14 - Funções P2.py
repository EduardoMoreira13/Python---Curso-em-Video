# Desafio 106

def ajuda(pesquisa):
    help(pesquisa)

while True:
    print("-" * 50)
    print("Sistema de Ajuda Pyhelp")
    print("-" * 50)
    pesquisa = str(input("Função ou Biblioteca > "))
    if pesquisa.upper() != "FIM":
        print()
        ajuda(pesquisa)
    else:
        print("FIM!")
        break
    print("-"*50)


print("\n")



# Desafio 105

def notas(*num, situacao = False):
    from statistics import mean
    dicionario = dict()
    dicionario["Total"] = len(num)
    dicionario["Mínimo"] = min(num)
    dicionario["Máximo"] = max(num)
    dicionario["Média"] = mean(num)
    if situacao == True:
        if dicionario["Média"] < 5:
            dicionario["Situação"] = "Ruim"
        elif dicionario["Média"] >= 7:
            dicionario["Situação"] = "Boa"
        else:
            dicionario["Situação"] = "Razoável"
        return dicionario
    else:
        return dicionario


resp = notas(5.5,2.5,10,6.5, situacao=False)
print(resp)

resp = notas(6,7,8,7, situacao=True)
print(resp)

resp = notas(5.50,6.80, situacao=True)
print(resp)

resp = notas(8.5,9.5,10,8.75, situacao=True)
print(resp)

resp = notas(3,4,2,4, situacao=True)
print(resp)


print("\n")


# Desafio 104

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric() == True:
            valor = int(n)
            ok = True
        else:
            print("ERRO! Digite um número inteiro válido.")
        if ok == True:
            break
    return valor

n = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {n}")




# Desafio 103

nome = str(input("Nome do Jogador: ")).capitalize().strip()
gols = int(input("Número de Gols: "))

def futebol(n = "<Desconhecido>", g = 0):
    print(f"O jogador {n} fez {g} gol(s) no campeonato.")

futebol(nome, gols)
futebol(n = nome)
futebol(g = gols)
futebol()
futebol()

# Desafio 102

def fatorial(numero = 1, show = True):
    valor = 1
    for i in range(numero, 0, -1):
        valor *= i
        if show == True:
            if i != 1:
                print(f"{i} x ", end="")
            else:
                print(f"{i} = ", end="")
    return valor


print(fatorial(6,show = True))
print(fatorial(6,show = False))


print("\n")

def fatorial(numero = 1, show = True):
    valor = 1
    for i in range(numero, 0, -1):
        valor *= i
        if show == True:
            if i != 1:
                print(f"{i} x ", end="")
            else:
                print(f"{i} = {valor}")
        else:
            if i == 1:
                print(f"{valor}")


fatorial(6,show = True)
fatorial(6,show = False)

print("\n")



# Desafio 101

from datetime import datetime

ano = int(input("Em que ano você nasceu? "))

def voto():
    idade = datetime.now().year - ano
    print(f"Com {idade} anos: ", end="")
    if idade >= 18 and idade <= 70:
        print("Voto Obrigatório!")
    elif idade < 16:
        print("Não Vota!")
    else:
        print("Voto Opcional!")

voto()

print("\n")

def voto(age):
    if age >= 18 and age <= 70:
       return "Voto Obrigatório!"
    elif age < 16:
       return "Não Vota!"
    else:
       return "Voto Opcional!"


ano = int(input("Em que ano você nasceu? "))
idade = datetime.now().year - ano
decisao = voto(idade)
print(f"Com {idade} anos: {decisao}")

print("\n")




# Docstrings e Parâmetros Opcionais

def somar(a = 0, b = 0, c = 0):
    """
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: não utilizado
    Função criada por Eduardo Moreira para somar até três valores
    """
    soma = a + b + c
    print(f"A soma entre {a}, {b} e {c} vale {soma}")

somar()
somar(3,2,1)
somar(c=3,a=2,b= 1)
somar(3,2)
somar(b=5)
somar(5)