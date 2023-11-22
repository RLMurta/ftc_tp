Projeto de Conversão de Gramáticas Formais
Descrição do Projeto
Este projeto consiste em um conjunto de classes e métodos para realizar a conversão de gramáticas formais para formas normais específicas, como a Forma Normal de Chomsky e a Segunda Forma Normal. O código está estruturado em módulos e classes para facilitar a manutenção e extensão do sistema.

Estrutura do Projeto
O projeto é dividido em vários módulos:

read_file.py: Contém a classe ReadFile, responsável por ler regras de gramáticas de um arquivo.

methods.py: Inclui funções utilitárias, como a função copy_dict para copiar dicionários.

normal_forms.py: Contém as classes ChomskyNormalForm e SecondNormalForm, que realizam a conversão para a Forma Normal de Chomsky e a Segunda Forma Normal, respectivamente.

algorithms.py: Apresenta as implementações dos algoritmos CYK e Modified CYK para processamento de gramáticas convertidas.

Como Usar
Leitura de Regras da Gramática: Utilize a classe ReadFile para ler as regras de uma gramática a partir de um arquivo.

python
Copy code
from read_file import ReadFile

grammar_file = ReadFile('grammar_rules.txt')
rules = grammar_file.rules
Conversão para Forma Normal de Chomsky:

python
Copy code
from normal_forms import ChomskyNormalForm
import methods

cnf_converter = ChomskyNormalForm()
chomsky_rules = cnf_converter.cfg_to_cnf(rules)
Conversão para Segunda Forma Normal:

python
Copy code
from normal_forms import SecondNormalForm
from algorithms import ModifiedCyk

second_normal_converter = SecondNormalForm()
second_normal_rules = second_normal_converter.cfg_to_2nf(rules)
Processamento com Algoritmos CYK e Modified CYK:

python
Copy code
from algorithms import Cyk, ModifiedCyk

cyk_result = Cyk.run(chomsky_rules, 'aba')
modified_cyk_result = ModifiedCyk().run(second_normal_rules, 'aba')
Sobre a Organização do Código
Modularização e Classes: O código está estruturado de forma modular, facilitando a compreensão e manutenção. As funcionalidades são organizadas em classes e métodos específicos.

Docstrings e Comentários: Docstrings foram utilizadas para documentar as classes e métodos, fornecendo informações claras sobre sua finalidade, argumentos e retorno. Comentários adicionais foram inseridos quando necessário para esclarecer partes específicas do código.

Nomeação de Variáveis e Métodos: As variáveis e métodos foram nomeados de forma descritiva e seguindo as convenções de estilo de grandes empresas de tecnologia.

Possíveis Mudanças e Melhorias
1-Testes Unitários: Adicionar testes unitários para garantir a robustez do código e facilitar futuras alterações.

2-Tratamento de Exceções: Implementar tratamento de exceções para lidar com possíveis erros durante a leitura de arquivos e processamento de gramáticas.

3-Melhorias nos Algoritmos: Avaliar a eficiência dos algoritmos CYK e Modified CYK para grandes conjuntos de regras e otimizar conforme necessário.

4-Logging: Adicionar logging para registrar informações relevantes durante a execução do programa.