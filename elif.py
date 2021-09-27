idade = int(input('Digite sua idade: '))

if idade == 18:
    print('Você tem acesso ao Módulo 1')
elif idade > 18 and idade < 30:
    print('Você tem acesso ao Módulo 2')
elif idade >= 30 and idade < 80:
    print('Você tem acesso ao Módulo 3')
elif idade >= 80:
    print('Você tem acesso a todos os Módulos!')
else:
    print("Infelizmente você não tem acesso a nenhum módulo.")

# elif = else if, ao invés de criar vários if, utilizamos o elif para criar mais opções.
