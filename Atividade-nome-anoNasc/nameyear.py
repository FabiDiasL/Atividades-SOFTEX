
anoNasc = False
while (anoNasc == False):
    try:
        nome = input("Insira seu nome completo: " )
        anoNasc = int(input("Insira seu ano de nascimento: " ))
        if (anoNasc >= 1922 and anoNasc <= 2021):
           anoAtual = 2022
           idade = anoAtual - anoNasc
           anoNasc = True
           print(nome)
           print("Neste ano de 2022 você completa ",idade," anos.")
        else :
           print("Você digitou um ano de nascimento inválido!")
           anoNasc = False
    except:
       print("Caracter inválido, por favor digite o seu nome e ano de nascimento corretamente.")
