def soma():
    number1 = float(input("Digite o primeiro numero: "))
    number2 = float(input("Digite o segundo numero: "))
    print("Soma = ",number1+number2)

def subtracao():
    number1 = float(input("Digite o primeiro numero: "))
    number2 = float(input("Digite o segundo numero: "))
    print("Subtração = ",number1-number2)

def multiplicacao():
    number1 = float(input("Digite o primeiro numero: "))
    number2 = float(input("Digite o segundo numero: "))
    print("Multiplicação = ",number1*number2)

def divisao():
    number1 = float(input("Digite o primeiro numero: "))
    number2 = float(input("Digite o segundo numero: "))
    print("Divisão = ",number1/number2)

operacao = 1

while operacao != 0:
    print("Escolha uma operação matemática: ")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão ")
    print("0: Sair")

    operacao = int(input("Operação: "))

    if(operacao==1):
        soma()
    elif(operacao==2):
        subtracao()
    elif(operacao==3):
        multiplicacao()
    elif(operacao==4):
        divisao()
    elif(operacao==0):
        break
    else:
        print("Essa opção não existe!")

print("Calculadora encerrada com sucesso!")