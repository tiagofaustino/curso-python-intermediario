#Exercicio 2 Aula 3
#Converter inf_carros para um dicionário, onde o nome do carro seja a chave dicionario e as demais informacoes sejam um outro dicionario
#dicionario = {'sandero': {'ano': 1997, 'kilometragem': 125000, 'km_media': 4807.69}}

inf_carros = [['sandero', 'gol', 'uno', 'fusca', 'opala'],
    [1997, 2008, 1980, 2015, 1967],
    [125000, 57000, 32900, 415000, 20000],
    [4807.69, 3800.0, 765.12, 51875.0, 357.14]]

dic_inf_carros = {}
qtd_carros = len(inf_carros[0])

for i in range(qtd_carros):
    dic_inf_carros[inf_carros[0][i]] = {'ano': inf_carros[1][i], 'kilometragem': inf_carros[2][i], 'km_media': inf_carros[3][i]}

dic_inf_carros

'''
Resultado
{'sandero': {'ano': 1997, 'kilometragem': 125000, 'km_media': 4807.69},
 'gol': {'ano': 2008, 'kilometragem': 57000, 'km_media': 3800.0},
 'uno': {'ano': 1980, 'kilometragem': 32900, 'km_media': 765.12},
 'fusca': {'ano': 2015, 'kilometragem': 415000, 'km_media': 51875.0},
 'opala': {'ano': 1967, 'kilometragem': 20000, 'km_media': 357.14}}
'''