### Exercício 2 Aula 3 
# Ler arquivo de numeros e printar a quantidade de numeros pares e numeros impares

# leitura arquivo
import os
current_dir = os.path.dirname(os.path.realpath('__file__')) #pega o diretório corrente do arquivo
url_ex1 = os.path.join(current_dir, 'numeros.txt') #junta as informações de path do arquivo
arquivo_ex1 = open(url_ex1, "r")

pares = 0
impares = 0
for linha in arquivo_ex1:
    if int(linha)%2 == 0:
        pares += 1
    else: impares += 1
print("Quantidade de números pares: {}. Quantidade de números ímpares: {}.".format(pares, impares))

#RESULTADO
#Quantidade de números pares: 9. Quantidade de números ímpares: 9.