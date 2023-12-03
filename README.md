# Projeto de Conversão de Gramáticas Formais

## Descrição do Projeto

Este projeto consiste em um conjunto de classes e métodos para realizar a conversão de gramáticas formais para formas normais específicas, como a Forma Normal de Chomsky e a Segunda Forma Normal. O código está estruturado em módulos e classes para facilitar a manutenção e extensão do sistema.

## Estrutura do Projeto

O projeto é dividido em vários módulos:

- **methods.py:** Inclui funções utilitárias e métodos necessários para habilitar o carregamento do arquivo, tradução e conversão da entrada para a primeira forma normal e segunda forma de Chomsky, e para habilitar a execução dos algoritmos CYK e CYK modificado que usa a tabela invertida.

- **normal_forms.py:** Contém as classes que realizam a conversão para a Forma Normal de Chomsky e a Segunda Forma Normal, respectivamente.

- **algorithms.py:** Apresenta as implementações dos algoritmos CYK e Modified CYK para o processamento de gramáticas convertidas.

## Como Usar

### Leitura de Regras da Gramática

Utilize a função `readGramatica` da classe `Gramatica` para ler as regras de uma gramática a partir de um arquivo.

### Docstrings e Comentários

Docstrings foram utilizadas para documentar as classes e métodos, fornecendo informações claras sobre sua finalidade, argumentos e retorno. Comentários adicionais foram inseridos quando necessário para esclarecer partes específicas do código.

### Nomeação de Variáveis e Métodos

As variáveis e métodos foram nomeados de forma descritiva e seguindo as convenções de estilo de grandes empresas de tecnologia.

## Instruções:
A gramatica é lida diretamente do arquivo cfg_file, e o seguinte exemplo mostra o formato do arquivo:
```
a b #terminais
Variaveis: #variaveis
S A B C D E F G H I J
Producoes: #producoes
S -> A | B;
A -> a E | ε;
B -> a F | b I;
C -> ε;
D -> b J;
E -> a E E | a F G | b C;
F -> a E F | a F H | b D;
G -> b;
H -> b D;
I -> a E F G | b;
J -> a F H | b D
```

Caso queira editar a gramática de entrada é só editar o cfg_file seguindo o modelo acima como exemplo.

Caso queira colocar uma frase de entrada é necessário editar o input_file_(numero) da gramatica especifica ctg_file_(numero), seguindo o exemplo abaixo:

```
aaabbb
aaabbb
aaaaaaaaaaaaaaabbbbbbbbbbbbbbbb
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbb
ab
```

O resultado é mostrado ao rodar o algoritmo diretamente no terminal alem de ser gerado um arquivo relatando os resultados de cada gramatica e cada entrada com nome output

## Método de uso:
- Execute main.py sem nenhum parâmetro

```
python3 main.py

```

Lembre-se de que:
- Caso queira editar a gramática de entrada é só editar o cfg_file seguindo o modelo passado como exemplo.
- Caso queira colocar uma frase de entrada é necessário editar o input_file_(numero) da gramatica especifica ctg_file_(numero).
- O resultado é mostrado ao rodar o algoritmo diretamente no terminal alem de ser gerado um arquivo output com as informaÇões.