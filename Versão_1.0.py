# Calculadora Científica Simplificada V1.0:
import math

def soma():
    a = float(input("Primeiro Número: "))
    b = float(input("Segundo Número: "))
    resultado = a + b

    historico.append(f"{a} + {b} = {resultado}")

    print(f"O resultado é: {resultado}")


def subtracao():
    a = float(input("Primeiro Número: "))
    b = float(input("Segundo Número: "))
    resultado = a - b

    historico.append(f"{a} - {b} = {resultado}")

    print(f"O resultado é: {resultado}")


def multiplicacao():
    a = float(input("Primeiro Número: "))
    b = float(input("Segundo Número: "))
    resultado = a * b

    historico.append(f"{a} * {b} = {resultado}")

    print(f"O resultado é: {resultado}")


def divisao():
    a = float(input("Primeiro Número: "))
    b = float(input("Segundo Número: "))
    if b != 0:
        resultado = a / b

        historico.append(f"{a} / {b} = {resultado}")

        print(f"O resultado é: {resultado}")
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
    print("Resultado: ", (valor * porcento) / 100)


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


def mostrar_histórico():
    if not historico:
        print("Histórico Vazio.")
        return
    print("\n=== Histórico ===")
    for operacao in historico:
        print(operacao)


menu = {
    "1": ("soma", soma),
    "2": ("subtracao", subtracao),
    "3": ("multiplicacao", multiplicacao),
    "4": ("divisao", divisao),
    "5": ("potencia", potencia),
    "6": ("raiz_quadrada", raiz_quadrada),
    "7": ("seno", seno),
    "8": ("cosseno", cosseno),
    "9": ("fatorial", fatorial),
    "10": ("porcentagem", porcentagem),
    "11": ("logaritmo", logaritmo),
    "12": ("tangente", tangente),
    "13": ("historico", mostrar_histórico)
}

historico = []


def calculadora():
    while True:
        print("\n==== Calculadora Científica ====")

        for chave, (nome, _) in menu.items():
            print(f"{chave} - {nome}")

        print("0 - Sair")

        try:
            opcao = input("Escolha uma opção: ")

            if opcao == "0":
                print("Saindo...")
                break

            elif opcao in menu:
                menu[opcao][1]()

            else:
                print("Opção inválida!")

        except ValueError:
            print("Entrada inválida!")

calculadora()