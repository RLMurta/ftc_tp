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
cyk_start_time = time.time()
cfgToCnf(grammar)
# Verificação se a entrada pertence à gramática usando o algoritmo CYK
isPresent = Cyk.run(grammar, entrada)
cyk_total_time = time.time() - cyk_start_time

if isPresent:
    print(f'Utilizando CYK: "{entrada}" pertence à gramática')
else:
    print(f'Utilizando CYK: "{entrada}" não pertence à gramática')

# Impressão da Forma Normal de Chomsky
# print('Forma Normal de Chomsky:')
# grammar.print()

# Reinicialização da gramática para aplicação da Segunda Forma Normal de Chomsky
grammar2 = Gramatica()
grammar2.readGramatica(filename)

# Aplicação da Segunda Forma Normal de Chomsky
modified_cyk_start_time = time.time()
cfgTo2nf(grammar2)
anulaveis = methods.anulavel(grammar2)
isPresent2 = ModifiedCyk.run(grammar2, entrada, anulaveis)
modified_cyk_total_time = time.time() - modified_cyk_start_time

if isPresent2:
    print(f'Utilizando CYK Modificado: "{entrada}" pertence à gramática')
else:
    print(f'Utilizando CYK Modificado: "{entrada}" não pertence à gramática')

# Impressão da Segunda Forma Normal de Chomsky
# print('Segunda Forma normal de Chomsky:')
# grammar2.print()

# Exibição dos tempos de execução
print('Tempo de execução CYK:', round(cyk_total_time, 5))
print('Tempo de execução CYK Modificado', round(modified_cyk_total_time, 5))