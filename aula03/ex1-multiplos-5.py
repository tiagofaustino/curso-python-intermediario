### Exercício 1 Aula 3 
# printar a soma de todos os multiplos de 5 entre 0 e 100
#usando for

#modo que eu fiz rápido
soma = 0
for n in range(0,101):
    mult = n * 5
    if mult <= 100:
        soma += mult
print(soma)

#depois que o professor explicou o "%"
soma = 0
for n in range(0,101):
    if n%5 == 0:
        soma += n
print(soma)

#forma 3 usando o intervalo do range
soma = 0
for n in range(0,101, 5):
    soma += n
print(soma)

# RESULTADO
'''
1050
1050
1050
'''