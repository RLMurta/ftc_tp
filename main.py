from normal_forms import Gramatica, cfgToCnf, cfgTo2nf
from algorithms import Cyk, ModifiedCyk
import methods
import time

filename = 'cfg_file'

entrada = "abababababababababababababababab"

# Leitura da gramática a partir do arquivo
grammar = Gramatica()
grammar.readGramatica(filename)

# Impressão da Forma Original da Gramatica
# print('Gramatica de entrada:')
# grammar.print()

# Aplicação da Forma Normal de Chomsky
cyk_start_time = time.time()
cfgToCnf(grammar)
# Verificação se a entrada pertence à gramática usando o algoritmo CYK
isPresent = Cyk.run(grammar, entrada)
cyk_total_time = time.time() - cyk_start_time

if isPresent:
    print(f'Utilizando a Forma de Chomsky Normal a frase de entrada: "{entrada}" pertence à gramática')
else:
    print(f'Utilizando a Forma de Chomsky Normal a frase de entrada: "{entrada}" não pertence à gramática')

# Impressão da Forma Normal de Chomsky
# print('Forma Normal de Chomsky:')
# grammar.print()

# Reinicialização da gramática para aplicação da Segunda Forma Normal de Chomsky
grammar = Gramatica()
grammar.readGramatica(filename)

# Aplicação da Segunda Forma Normal de Chomsky
modified_cyk_start_time = time.time()
cfgTo2nf(grammar)
anulaveis = methods.anulavel(grammar)
isPresent = ModifiedCyk.run(grammar, entrada, anulaveis)
modified_cyk_total_time = time.time() - modified_cyk_start_time

if isPresent:
    print(f'Utilizando a Segunda Forma Normal de Chomsky a frase de entrada: "{entrada}" pertence à gramática')
else:
    print(f'Utilizando a Segunda Forma Normal de Chomsky a frase de entrada: "{entrada}" não pertence à gramática')

# Impressão da Segunda Forma Normal de Chomsky
# print('Segunda Forma normal de Chomsky:')
# grammar.print()

# Exibição dos tempos de execução
print('Tempo de execução da Forma Normal de Chomsky:', round(cyk_total_time, 5))
print('Tempo de execução da segunda Forma normal de Chomsky', round(modified_cyk_total_time, 5))