import methods

left, right = 0, 1
COUNTER = 0
K, V, Productions = [], [], []
VARIABLE = ""

class Gramatica:
    def __init__(self):
        """
        initializa uma instância da classe Grammar.

        Atributos:
        - rules: Lista de regras da gramática.
        - terminals: Lista de terminais da gramática.
        - variables: Lista de variáveis da gramática.
        - initial: Símbolo inicial da gramática.
        """
        self.rules = []
        self.terminals = []
        self.variables = []
        self.initial = ""

    def readGramatica(self, filename):
        """
        Lê uma gramática a partir de um arquivo.

        Parâmetros:
        - filename (str): O nome do arquivo contendo a gramática.

        Retorna:
        None
        """
        self.terminals, self.variables, self.rules = methods.loadModel(filename)

    def print(self):
        """
        Imprime as variáveis, terminals e rules da gramática.

        Retorna:
        None
        """
        print("Variaveis:")
        print(self.variables)

        print("Terminais:")
        print(self.terminals)

        print("Regras:")
        print(methods.structuredForm(self.rules))

def cfgToCnf(gramatica: Gramatica):
    """
    Converte a gramática para a forma normal de Chomsky (CNF).

    Parâmetros:
    - gramatica (Gramatica): A gramática a ser convertida.

    Retorna:
    None
    """
    methods.defineVariable(gramatica.variables)

    gramatica.rules, gramatica.initial = methods.START(gramatica.rules, variables=gramatica.variables)
    gramatica.rules = methods.TERM(gramatica.rules, variables=gramatica.variables, terminals=gramatica.terminals)
    gramatica.rules = methods.BIN(gramatica.rules, variables=gramatica.variables,)
    gramatica.rules = methods.DEL(gramatica.rules)
    gramatica.rules = methods.UNIT(gramatica.rules, variables=gramatica.variables,)
    
    gramatica = methods.startingRuleFirst(gramatica)

def cfgTo2nf(gramatica: Gramatica):
    """
    Converte a gramática para a Segunda Forma Normal (2NF).

    Parâmetros:
    - gramatica (Gramatica): A gramática a ser convertida.

    Retorna:
    None
    """
    methods.defineVariable(gramatica.variables)

    gramatica.rules = methods.BIN(gramatica.rules, variables=gramatica.variables)
