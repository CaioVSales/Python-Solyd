var_verdade = True # Boolean
var_falso = False # Boolean

if var_verdade == True:
    print(var_verdade)
else:
        print(var_falso)

# If e Else são estruturas de decisão e condição
# Ambos verificam algum argumento, e somente um deles poderá ser retornado.
# If e Else utilizam de operadores lógicos, sendo esses:
# == (Igual a ?)
# > (Maior que)
# < (Menor que)
# >= , <= (Maior igual e Menor igual a)
# != (Diferente de)
# and (E)
# or (Ou)
# Ex:

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é de maior, pode passar!')
else:
    print("Infelizmente você é de menor, volte quando completar 18 anos.")