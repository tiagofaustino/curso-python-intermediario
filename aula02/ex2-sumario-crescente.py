##### Exercício 2 Aula 2 #####

''' 
Criar um sumário com 5 itens e 6 subitens (incluindo zero), em ordem crescente.
Utilizar estrutura de repetição while
'''

max_item = 5
max_subitem = 6
i = 1

while i <= max_item:
    s = 0
    while s <= max_subitem:
        print(i, '.', s, sep='')
        s = s + 1
    
    i = i + 1

# RESULTADO
'''
1.0
1.1
1.2
1.3
1.4
1.5
1.6
2.0
2.1
2.2
2.3
2.4
2.5
2.6
3.0
3.1
3.2
3.3
3.4
3.5
3.6
4.0
4.1
4.2
4.3
4.4
4.5
4.6
5.0
5.1
5.2
5.3
5.4
5.5
5.6
'''