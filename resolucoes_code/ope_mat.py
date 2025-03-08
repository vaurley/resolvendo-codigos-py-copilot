# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def calcular():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    while True:
        operacao = input("Digite a operação desejada (+, -, *, /): ")

        if operacao == "+":
            print("Resultado:", num1 + num2)
            break
        elif operacao == "-":
            print("Resultado:", num1 - num2)
            break
        elif operacao == "*":
            print("Resultado:", num1 * num2)
            break
        elif operacao == "/":
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
            else:
                print("Resultado:", num1 / num2)
            break
        else:
            print("Operação inválida! Tente novamente.")

calcular()
