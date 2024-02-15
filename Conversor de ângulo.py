Opc = int(input("Escolha uma das opções de conversão abaixo\n 1- Rad > Graus \n 2- Graus > Rad"))
if Opc == 1:
    R = float(input("Digite o valor em radianos"))
    G = R * 57.29578
    print(f'O valor de {R} em graus é {G}')
if Opc == 2:
    G = float(input("Digite o valor em graus"))
    R = G * 0.017453
    print(f'O valor de {G} em radianos é {R}')
if Opc >= 3:
    print("Opção inválida, selecione uma opção entre 1 e 2")