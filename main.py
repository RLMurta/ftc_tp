from normal_forms import Gramatica, cfgToCnf, cfgTo2nf
from algorithms import Cyk, ModifiedCyk
import methods
import time

filename = 'gramaticas/cfg_file_2'

entrada = "(t)"

# Leitura da gramática a partir do arquivo
grammar = Gramatica()
grammar.readGramatica(filename)

# Impressão da Forma Original da Gramatica
print('Gramatica de entrada:')
grammar.print()

# Aplicação da Forma Normal de Chomsky
chomsky_normal_form_start_time = time.time()
cfgToCnf(grammar)
chomsky_normal_form_total_time = time.time() - chomsky_normal_form_start_time

# Verificação se a entrada pertence à gramática usando o algoritmo CYK
isPresent = Cyk.run(grammar, entrada)

if isPresent:
    print(f'Utilizando a Forma de Chomsky Normal a frase de entrada: "{entrada}" pertence à gramática')
else:
    print(f'Utilizando a Forma de Chomsky Normal a frase de entrada: "{entrada}" não pertence à gramática')

# Impressão da Forma Normal de Chomsky
print('Forma Normal de Chomsky:')
grammar.print()

# Reinicialização da gramática para aplicação da Segunda Forma Normal de Chomsky
grammar2 = Gramatica()
grammar2.readGramatica(filename)

# Aplicação da Segunda Forma Normal de Chomsky
second_normal_form_start_time = time.time()
cfgTo2nf(grammar2)
anulaveis = methods.anulavel(grammar2)
isPresent2 = ModifiedCyk.run(grammar2, entrada, anulaveis)
second_normal_form_total_time = time.time() - second_normal_form_start_time

if isPresent2:
    print(f'Utilizando a Segunda Forma Normal de Chomsky a frase de entrada: "{entrada}" pertence à gramática')
else:
    print(f'Utilizando a Segunda Forma Normal de Chomsky a frase de entrada: "{entrada}" não pertence à gramática')

# Impressão da Segunda Forma Normal de Chomsky
print('Segunda Forma normal de Chomsky:')
grammar2.print()

# Exibição dos tempos de execução
print('Tempo de execução da Forma Normal de Chomsky:', round(chomsky_normal_form_total_time, 5))
print('Tempo de execução da segunda Forma normal de Chomsky', round(second_normal_form_total_time, 5))