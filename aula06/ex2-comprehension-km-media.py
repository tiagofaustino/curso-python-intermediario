# Exercicio 2 Aula 6
# criar uma nova lista com a kilometragem media dos carros de inf_carros usando list comprehension

inf_carros = [['sandero', 'gol', 'uno', 'fusca', 'opala'],
    [1997, 2008, 1980, 2015, 1967],
    [125000, 57000, 32900, 415000, 20000]]

km_media = [round(inf_carros[2][i] / (2023 - inf_carros[1][i]),2) for i in range(len(inf_carros[0]))]
inf_carros.append(km_media)
print(inf_carros)

#Resultado
#[['sandero', 'gol', 'uno', 'fusca', 'opala'], [1997, 2008, 1980, 2015, 1967], [125000, 57000, 32900, 415000, 20000], [4807.69, 3800.0, 765.12, 51875.0, 357.14]]