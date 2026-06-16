# Calculadora Científica Simplificada:
import math


def soma():
    a = float(input("Primeiro Número: "))
    b = float(input("Segundo Número: "))
    print(f"O resultado é: {a + b}")


def subtracao():
    a = float(input("Primeiro Número: "))
    b = float(input("Segundo Número: "))
    print(f"O resultado é: {a - b}")


def multiplicacao():
    a = float(input("Primeiro Número: "))
    b = float(input("Segundo Número: "))
    print(f"O resultado é: {a * b}")


def divisao():
    a = float(input("Primeiro Número: "))
    b = float(input("Segundo Número: "))
    if b != 0:
        print(f"O resultado é: {a / b}")
    else:
        print("Não é possivel dividir por zero!")


def potencia():
    base = float(input("Base: "))
    expoente = float(input("Expoente: "))
    print("O resultado é:", math.pow(base, expoente))


def raiz_quadrada():
    num = float(input("Número: "))
    if num >= 0:
        print("Raiz Quadrada: ", math.sqrt(num))
    else:
        print("Não existe raiz quadrada real de número negativo.")


def seno():
    angulo = float(input("Ângulo em graus: "))
    radianos = math.radians(angulo)
    print("Resultado: ", math.sin(radianos))


def cosseno():
    angulo = float(input("Ângulo em graus:"))
    radiano = math.radians(angulo)
    print("Resultado: ", math.cos(radiano))


def fatorial():
    num = int(input("Número inteiro: "))
    if num >= 0:
        print("Resultado:", math.factorial(num))
    else:
        print("Fatorial não existe para negativos.")


def porcentagem():
    valor = float(input("Valor: "))
    porcento = float(input("Porcentagem: "))
    print("Resultado: ", (valor / porcento) * 100)


def logaritmo():
    num = float(input("Número: "))
    if num > 0:
        print("Resultado: ", math.log10(num))
    else:
        print("Logaritmos só existem para números positivos!")


def tangente():
    angulo = float(input("Ângulo em graus: "))
    radianos = math.radians(angulo)
    print("Resultado: ", math.tan(radianos))


def calculadora():
    while True:
        print("\n==== Calculadora Científica ====")
        print("1- Soma")
        print("2- Subtração")
        print("3- Multiplicação")
        print("4- Divisão")
        print("5- Potência")
        print("6- Raiz Quadrada")
        print("7- Seno")
        print("8- Cosseno")
        print("9- Fatorial")
        print("0- Sair")

        try:
            opcao = input("Escolha uma opção: ")

            if opcao == "0":
                print("Saindo...")
                break

            elif opcao == "1":
                soma()

            elif opcao == "2":
                subtracao()

            elif opcao == "3":
                multiplicacao()

            elif opcao == "4":
                divisao()

            elif opcao == "5":
                potencia()

            elif opcao == "6":
                raiz_quadrada()

            elif opcao == "7":
                seno()

            elif opcao == "8":
                cosseno()

            elif opcao == "9":
                fatorial()

            else:
                print("Opção Inválida!")

        except ValueError:
            print("Entrada Inválida!")


calculadora()
