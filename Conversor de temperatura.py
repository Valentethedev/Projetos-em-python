opc = int(input("Selecione uma das opções de conversão abaixo\n 1- Fahrenheit-Celsius\n 2- Fahrenheit-Kelvin\n 3- Celsius-Farhenheit\n 4- Celsius-Kelvin\n 5- Kelvin-Fahrenheit\n 6- Kelvin-Celsius "))
if opc == 1:
    TF = int(input("Digite a temperatura em fahrenheit"))
    TC = (TF-32)/1.8
    print(f'{TF} em fahrenheit são {TC} graus celsius')
if opc == 2:
    TF = int(input("Digite a temperatura em fahrenheit"))
    TK = (TF+459.67)/1.8
    print(f'{TF} em fahrenheit são {TK} graus kelvin')
if opc == 3:
    TC = int(input("Digite a temperatura em celsius"))
    TF = TC * 1.8 + 32
    print(f'{TC} em celsius são {TF} graus fahrenheit')
if opc == 4:
    TC = int(input("Digite a temperatura em celsius"))
    TK = TC + 273.15
    print(f'{TC} em celsius são {TK} graus kelvin')
if opc == 5:
    TK = int(input("Digite a temperatura em kelvin"))
    TF = TK * 1.8 - 459.67
    print(f'{TK} em celsius são {TF} graus fahrenheit')
if opc == 6:
    TK = int(input("Digite a temnperatura em kelvin"))
    TC = TK - 273.15
    print(f'{TK} em celsius são {TC} graus celsius')
else:
    print("Opção inválida, selecione entre 1 e 6")