#Exercicio 2 Aula 5
# Criar uma funcao para receber como parametro um dicionario (inf_carros) e um nome de carro
# e vai retornar as informacoes do carro solicitado por parametro

dic_inf_carros = {'sandero': {'ano': 1997, 'kilometragem': 125000, 'km_media': 4807.69},
 'gol': {'ano': 2008, 'kilometragem': 57000, 'km_media': 3800.0},
 'uno': {'ano': 1980, 'kilometragem': 32900, 'km_media': 765.12},
 'fusca': {'ano': 2015, 'kilometragem': 415000, 'km_media': 51875.0},
 'opala': {'ano': 1967, 'kilometragem': 20000, 'km_media': 357.14}}

def obter_info_carro(dic, nome_carro):
    try:
        return dic[nome_carro]
    except:
        print('carro como nome {} não encontrado'.format(nome_carro))

print(obter_info_carro(dic_inf_carros, 'gol'))
print(obter_info_carro(dic_inf_carros, 'corolla'))

#Resultado
#{'ano': 2008, 'kilometragem': 57000, 'km_media': 3800.0}
#carro como nome corolla não encontrado
#None