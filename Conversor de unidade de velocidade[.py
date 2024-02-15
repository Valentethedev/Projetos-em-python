opc = int(input("Escolha uma das opções de conversão abaixo \n 1- Centímetros por segundo > Milhas por hora \n 2- Centímetros por segundo > Metros por segundo \n 3- Centímetros por segundo > Quilômetros por hora \n 4- Metros por segundo > Centímetros por segundo \n 5- Metros por segundo > Quilômetros por hora \n 6- Metros por segundo > Milhas por hora \n 7- Quilômetros por hora > Metros por segundo \n 8- Quilômetros por hora > Centímetros por segundo0 \n 9- Quilômetros por hora > milhas por hora \n 10- Milhas por hora > centímetros por segundo \n 11- Milhas por hora > Metros por segundo \n 12- Milhas por hora > Quilômetros por hora"))
if opc == 1:
    Cms = int(input("Digite o valor em cm/s"))
    Mph = Cms * 0.022371
    print(f'O valor em mph é {Mph}')
if opc == 2:
    Cms = int(input("Digite o valor em cm/s"))
    Ms = Cms * 0.01
    print(f'O valor em m/s é {Ms}')
if opc == 3:
    Cms = int(input("Digite o valor em cm/s"))
    Kmh = Cms * 0.036
    print(f'O valor em kmh é {Kmh}')
if opc == 4:
    Ms = int(input("Digite o valor em m/s"))
    Cms = Ms * 100
    print(f'O valor em cms é {Cms}')
if opc == 5:
    Ms = int(input("Digite o valor em m/s"))
    Kmh = Ms * 3.6
    print(f'O valor em km/h é {Kmh}')
if opc == 6:
    Ms = int(input("Digite o valor em m/s"))
    Mph = Ms * 2.273136
    print(f'O valor em mph é {Mph}')
if opc == 7:
    Kmh = int(input("Digite o valor em Km/h"))
    Ms = Kmh * 0.277778
    print(f'O valor em m/s é {Ms}')
if opc == 8:
    Kmh = int(input("Digite o valor em Km/h"))
    Cms = Kmh * 27.77778
    print(f'O valor em cm/s é {Cms}')
if opc == 9:
    Kmh = int(input("Digite o valor em Km/h"))
    Mph = Kmh * 0.621427
    print(f'O valor em mph é {Mph}')
if opc == 10:
    Mph = int(input("Digite o valor em mph"))
    Cms = Mph * 44.7
    print(f'O valor em cms é {Cms}')
if opc == 11:
    Mph = int(input("Digite o valor em mph"))
    Ms = Mph * 0.447
    print(f'O valor em m/s é {Ms}')
if opc == 12:
    Mph = int(input("Digite o valor em mph"))
    Kmh = Mph * 1.6092
    print(f'O valor em Kmh é {Kmh}')