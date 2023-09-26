# Exercicio 4 Aula 6
# Criar uma função que recebe o ano, mes e dia separadamente e calcule a diferenca ate o dia de hoje.
# Nao deve ser obrigatorio o mes e o dia
# caso nao venha o mes, colocar como default mes de dezembro.
# e se nao vier o dia, utilizar o ultimo dia do mes

import calendar
from datetime import datetime

def diferenca_dias(ano, mes=12): 
    dia = calendar.monthrange(ano, mes)[1]
    return diferenca_dias1(ano, mes, dia)

def diferenca_dias1(ano, mes, dia):
    return calcula_diferenca(datetime.now(), datetime(ano, mes, dia))

def calcula_diferenca(date_time1, date_time2):
    diff = date_time1 - date_time2
    return diff.days

print(diferenca_dias(2021, 2))
print(diferenca_dias(2021))
print(diferenca_dias1(2021,2,22))

#Resultado
'''
939
633
945
'''