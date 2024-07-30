nome = input("Digite seu nome")
anodenascimento = int(input("Digite o ano que você nasceu"))
anoatual = 2024
idade = anoatual - anodenascimento
if idade >= 18:
    print(f'{nome}, sua idade é {idade} e você é maior de idade')
else:
    print(f'{nome}, sua idade é {idade} e você é menor de idade')