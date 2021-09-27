idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))


if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Você tem os requisitos necessários para entrar no Exército.')
else:
    print('Infelizmente você não tem os requisitos necessários para entrar no Exército.')

