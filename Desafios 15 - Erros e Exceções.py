# Erros e Exceções

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com o tipo de dado que você digitou!")
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
except KeyboardInterrupt:
    print("O usuário não informou todos os valores solicitados!")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}!")
    print(f"O erro encontrado foi {erro.__class__}!")
else:
    print(f"O resultado é {r:.2f}.")
finally: # vai ser rodado de qualquer forma
    print("Volte sempre, Muito Obrigado!")