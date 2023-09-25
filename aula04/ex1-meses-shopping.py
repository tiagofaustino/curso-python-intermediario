#Exercicio 1 Aula 4
# Gerar uma lista com o nome do shopping, sem  a palavra shopping do inicio e o nome do mes por extenso buscando na tupla

tup = ('janeiro','fevreiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
shp = [['shopping grande tijuca',11], ['shopping norte shopping ',12], ['shopping villa lobos',3], ['shopping plaza niteroi',5], ['shopping grande recife',8]]

#resultado = [['grande tijuca', 'novembro'], ['norte shopping', 'dezembro'] ... ]

resultado = []
for s in shp:
    resultado.append([s[0].replace('shopping ', '', 1), tup[s[1]-1]])
print(resultado)

#Resultado
#[['grande tijuca', 'novembro'], ['norte ', 'dezembro'], ['villa lobos', 'março'], ['plaza niteroi', 'maio'], ['grande recife', 'agosto']]