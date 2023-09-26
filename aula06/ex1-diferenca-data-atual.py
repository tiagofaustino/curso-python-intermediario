#Exercicio 1 Aula 6
#Criar uma função onde vamos receber por parametro o ano, mes e dia separadamente (inteiros)
# que retorne a quantidade de dias para a data atual

from datetime import datetime

def diferenca_dias(ano, mes, dia):
    data_informada = datetime(ano, mes, dia)
    hoje = datetime.now()
    diff = hoje - data_informada
    return diff.days

diferenca_dias(2023, 9, 10)

#Resultado
#15