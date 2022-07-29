print("Calculadora de dois números")
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
operacao = int(input("Escolha uma das opções de operação entre os números digitados (1. Soma 2. Subtração 3. Multiplicação 4. Divisão): "))
def calculadora(number1, number2, operacao):
    if (operacao == 1): return number1 + number2
    elif (operacao == 2): return number1 - number2
    elif (operacao == 3): return number1 * number2
    elif (operacao == 4): return number1 / number2
    else: return 0

resultado = calculadora(number1, number2, operacao)
print(resultado)