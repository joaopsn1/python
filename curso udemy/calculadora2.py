"""
Calculadora
Autor: João Pedro
Função: Fazer contas: Soma / Divisão / Multiplicação / Subtração
"""

sair = False

while sair == False: 
    print("----CALCULADORA 2----")
    n1 = input("Digite o 1° número: ")
    n1 = int(n1)
    operador = input("Digite o operador: ")
    n2 = input("Digite o 2° número: ")
    n2 = int(n2)

    #Soma
    if operador == "+":
        operacao = n1 + n2
        print("O resultado da operação é: ", operacao)
    #Subtração
    elif operador == "-":
        operacao = n1 - n2
        print("O resultado da operação é: ", operacao)
    #Multiplicação
    elif operador == "*":
        operacao = n1 * n2
        print("O resultado da operação é: ", operacao)
    #Divisão
    else:
        operacao = n1 / n2
        print("O resultado da operação é: ", operacao)

    teste = input("Deseja sair? [S/N]: ")
    if teste == "S":
        sair = True
        print("Operação encerrada!")