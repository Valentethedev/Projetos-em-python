n1 = int(input("Digite o número 1"))
n2 = int(input("Digite o número 2"))
opc = int(input("Digite uma opção \n 1- Adição \n 2- Subtração \n 3- Mutiplicação \n 4- Divisão \n"))
def adicao():
    adicao = n1 + n2
    print(f'A soma é {adicao}')
def subtração():
    subtração = n1 - n2
    print(f'A diferença é {subtração}')
def mutiplicação():
    mutiplicação = n1 * n2
    print(f"O produto é {mutiplicação}")
def divisao():
    divisao = n1/n2
    print(f"O quociente é {divisao}")
if opc == 1:
    adicao()
elif opc == 2:
    subtracao()
elif opc == 3:
    mutiplicação()
elif opc == 4:
    divisao()
else:
    print("Opção inválida")
