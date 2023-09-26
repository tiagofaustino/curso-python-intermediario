# Exercicio 3 Aula 6
# criar uma função que vai receber o inf_carros como parametro, e vai retornar a quantidade de dias de uso para cada carro 
# de acordo com o seu ano de fabricação
# OBS: Utilizar o ultimo dia do ano para calculo
from datetime import date

dic_dias_uso = {}
def retorna_dias_uso(inf_carros):
    qtd_carros = len(inf_carros[0])
    for i in range(qtd_carros):
        dic_dias_uso[inf_carros[0][i]] = {'dias_uso': (date.today() - date.max.replace(year = inf_carros[1][i])).days}
    return dic_dias_uso

retorna_dias_uso(inf_carros)

#Resultado
'''
{'sandero': {'dias_uso': 9399},
 'gol': {'dias_uso': 5381},
 'uno': {'dias_uso': 15608},
 'fusca': {'dias_uso': 2825},
 'opala': {'dias_uso': 20357}}
'''