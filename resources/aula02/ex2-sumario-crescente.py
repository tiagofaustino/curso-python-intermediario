##### Exercício 2 Aula 2 #####

''' 
Criar um sumário com 5 itens e 6 subitens (incluindo zero), em ordem crescente.
Utilizar estrutura de repetição while
'''

max_item = 3
max_subitem = 5
i = 1

while i <= max_item:
    s = 0
    while s <= max_subitem:
        print(i, '.', s, sep='')
        s = s + 1
    
    i = i + 1