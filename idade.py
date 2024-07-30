nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))
maioridade = 18
if idade >= maioridade:
    print(f'Seja bem vindo {nome}, sua idade é {idade}, portanto você está autorizado')
else:
    print(f'{nome}, seu acesso foi negado, vocẽ precisa de ter mais de 18 anos para entrar')
