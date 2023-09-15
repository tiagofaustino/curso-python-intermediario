# Gravar um arquivo com o ano corrente e o ano em que entraram na empresa 
# Depois ler o arquivo, 
# Salvar as informações em 2 variáveis diferentes 
# E calcular a quantidade de anos em que trabalharam na empresa

#inicia o arquivo em modo de escrita
import os
current_dir = os.path.dirname(os.path.realpath('__file__')) #pega o diretório corrente do arquivo
url_ex1 = os.path.join(current_dir, 'exercicio-anos-empresa.txt') #junta as informações de path do arquivo
arquivo_ex1 = open(url_ex1, "w")

#cria as váriaveis
ano_entrada = '2021\n'
ano_atual = '2023'

#escreve os valores no arquivo
arquivo_ex1.write(ano_entrada)
arquivo_ex1.write(ano_atual)
arquivo_ex1.close()

#lê o arquivo
leitura_ex1 = open(url_ex1, 'r')
valor_ano_entrada = int(leitura_ex1.readline().replace('\n', ''))
valor_ano_atual = int(leitura_ex1.readline())
leitura_ex1.close()


#calcula o tempo de empresa
tempo_empresa = valor_ano_atual - valor_ano_entrada
print('Tempo de empresa:', tempo_empresa, 'ano(s)')