"""
Calculadora
Autor: João Pedro
Função: Fazer contas: Soma / Divisão / Multiplicação / Subtração
"""

print("----CALCULADORA----")
n1 = input("Digite o 1° número: ")
n1 = int(n1)
operador = input("Digite o operador: ")
n2 = input("Digite o 2° número: ")
n2 = int(n2)

if operador == "+":
    operacao = n1 + n2
    print("O resultado da operação é: ", operacao)
elif operador == "-":
    operacao = n1 - n2
    print("O resultado da operação é: ", operacao)
elif operador == "*":
    operacao = n1 * n2
    print("O resultado da operação é: ", operacao)
else:
    operacao = n1 / n2
    print("O resultado da operação é: ", operacao)