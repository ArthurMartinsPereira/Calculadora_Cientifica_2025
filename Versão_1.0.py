# Calculadora Científica Simplificada V1.0:
import math

def pedir_dois_numeros():
    a = float(input("Primeiro Número: "))
    b = float(input("Segundo Número: "))
    return a, b


def soma():
    a, b = pedir_dois_numeros()
    resultado = a + b

    historico.append(f"{a} + {b} = {resultado}")

    print(f"O resultado é: {resultado}")


def subtracao():
    a, b = pedir_dois_numeros()
    resultado = a - b

    historico.append(f"{a} - {b} = {resultado}")

    print(f"O resultado é: {resultado}")


def multiplicacao():
    a, b = pedir_dois_numeros()
    resultado = a * b

    historico.append(f"{a} * {b} = {resultado}")

    print(f"O resultado é: {resultado}")


def divisao():
    a, b = pedir_dois_numeros()
    if b != 0:
        resultado = a / b

        historico.append(f"{a} / {b} = {resultado}")

        print(f"O resultado é: {resultado}")
    else:
        print("Não é possivel dividir por zero!")


def potencia():
    base = float(input("Base: "))
    expoente = float(input("Expoente: "))
    resultado = math.pow(base, expoente)

    historico.append(f"{base}^{expoente} = {resultado}")

    print(f"O resultado é: {resultado}")


def raiz_quadrada():
    num = float(input("Número: "))
    if num >= 0:
        resultado = math.sqrt(num)
        historico.append(f"√{num} = {resultado}")

        print(f"Raiz Quadrada: {resultado}")
    else:
        print("Não existe raiz quadrada real de número negativo.")


def seno():
    angulo = float(input("Ângulo em graus: "))
    radianos = math.radians(angulo)
    resultado = math.sin(radianos)
    historico.append(f"sen({angulo}) = {resultado}")

    print(f"Resultado: {resultado}")


def cosseno():
    angulo = float(input("Ângulo em graus:"))
    radiano = math.radians(angulo)
    resultado = math.cos(radiano)

    historico.append(f"cos({angulo}) = {resultado}")

    print(f"Resultado: {resultado}")


def fatorial():
    num = int(input("Número inteiro: "))
    if num >= 0:
        resultado =  math.factorial(num)
        historico.append(f"{num}! = {resultado}")

        print(f"Resultado: {resultado}")
    else:
        print("Fatorial não existe para negativos.")


def porcentagem():
    valor = float(input("Valor: "))
    porcento = float(input("Porcentagem: "))
    resultado = (valor * porcento) / 100

    historico.append( f"{porcento}% de {valor} = {resultado}")

    print(f"Resultado: {resultado}")


def logaritmo():
    num = float(input("Número: "))
    if num > 0:
        resultado = math.log10(num)
        historico.append(f"log({num}) = {resultado}")

        print(f"Resultado: {resultado}")
    else:
        print("Logaritmos só existem para números positivos!")


def tangente():
    angulo = float(input("Ângulo em graus: "))
    radianos = math.radians(angulo)
    resultado = math.tan(radianos)
    historico.append(f"tan({angulo}) = {resultado}")

    print(f"Resultado: {resultado}")


def mostrar_historico():
    if not historico:
        print("Histórico Vazio.")
        return
    print("\n=== Histórico ===")
    for operacao in historico:
        print(operacao)

def limpar_historico():
    historico.clear()
    print("Histórico Apagado.")


menu = {
    "1": ("Soma", soma),
    "2": ("Subtração", subtracao),
    "3": ("Multiplicação", multiplicacao),
    "4": ("Divisão", divisao),
    "5": ("Potencia", potencia),
    "6": ("Raiz Quadrada", raiz_quadrada),
    "7": ("Seno", seno),
    "8": ("Cosseno", cosseno),
    "9": ("Fatorial", fatorial),
    "10": ("Percentage", porcentagem),
    "11": ("Logaritmo", logaritmo),
    "12": ("Tangente", tangente),
    "13": ("Histórico", mostrar_historico),
    "14": ("Limpar Histórico", limpar_historico)
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