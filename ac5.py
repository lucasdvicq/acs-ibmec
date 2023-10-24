"""
Programação Estruturada

23/10/2023
Ac5
"""

# 1 - Faça um programa para imprimir o texto abaixo, para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir_padrao(n):
    for i in range(1, n + 1):
        print(*range(1, i + 1))

n = int(input("Digite o valor de n: "))
imprimir_padrao(n)

# 2 - Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contar_digitos(numero):
    if numero == 0:
        return 1
    count = 0
    numero = abs(numero) # Exemplo do uso da tag abs

                         # numero = -10
                         # abs_numero = abs(numero)                                   
                         # print(abs_numero)  

                         # Imprimirá 10, que é o valor absoluto de -10
    while numero > 0:
        count += 1
        numero //= 10
    return count

numero = int(input("Digite um número inteiro: "))
quantidade_digitos = contar_digitos(numero)
print(f"O número {numero} tem {quantidade_digitos} dígitos.")

# 3 - Faça um programa que solicite ao usuário 2 números inteiros. A seguir, calcule e mostre a divisão do primeiro pelo segundo. Para resolver este problema, utilize a instrução try-except particularmente analizando as exceções do tipo ValueError e ZeroDivisionError. Inclua uma instrução finally para exibir o resultado da operação.

try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    resultado = num1 / num2
except ValueError: 
    print("Erro: Você não digitou um número inteiro válido.") # ValueError lida com problemas de tipo e ZeroDivisionError lida com divisões por zero.
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"O resultado da divisão de {num1} por {num2} é: {resultado:.2f}")
finally:
    print("Programa encerrado.")