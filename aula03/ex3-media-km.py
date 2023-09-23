# Exercicio 3 Aula 3
'''
Ler a lista de informação de carros, gerar uma nova lista dentro de inf_carros com a quilometragem_media de cada carro
Lista chama media -> quilometragem media = quilometragem(km) / (ano atual - ano fabricacao)
Ex: round(11111 / (2023 - 1997), 2)
'''

media_km = []

for i in range(len(inf_carros[0])):
    km = round(inf_carros[2][i] / (2023 - inf_carros[1][i]),2)
    media_km.append(km)
inf_carros.append(media_km)

print(inf_carros)

#RESULTADO
#[['Uno', 'Monza', 'BMW', 'Fusca', 'Opala'], [2000, 2010, 2020, 1990, 1980], [12500, 50000, 100, 343434, 7777], [543.48, 3846.15, 33.33, 10407.09, 180.86]]