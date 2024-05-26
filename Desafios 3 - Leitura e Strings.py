# Extra

nome = str(input("Nome: "))

print(nome[0:5])
print(nome[:5])
print(nome[2:])
print(nome[2::2])
print(nome[-5])


# Desafio 27

nome = str(input("Nome: ")).upper().strip()

print(nome.split()[0])
print(nome.split()[-1])



# Desafio 26

frase = str(input("Frase: ")).upper().strip()

print(frase.count("A"))
print(frase.find("A") + 1)
print(frase.rfind("A") + 1)
print(frase.rfind("A") - frase.count(" ") + 1)

# Desafio 25

cidade = str(input("Nome: ")).upper().strip()

print("SILVA" in cidade)


# Desafio 24

cidade = str(input("Cidade: ")).upper()

print("SANTO" in cidade)
print(cidade.startswith("SANTO"))


# Desafio 23

numero = str(input("Digite um numero: "))

for i in range(0, len(numero)):
    print(numero[i])

numero = int(input("Digite um numero: "))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(m, c, d, u)



# Desafio 22

nome = str(input("Digite seu nome Completo: ")).strip()

print("\n", nome.upper(), "\n", nome.lower(), "\n", len(nome) - nome.count(" "), "\n", len(nome.split()[0]))

print("\n", nome.upper(), "\n", nome.lower(), "\n", len(nome) - nome.count(" "), "\n", nome.find(" "))