import itertools

left, right = 0, 1
COUNTER = 0
K, V, Productions = [], [], []
VARIABLE = ""

def loadModel(modelPath):
    """
    Carrega um modelo a partir de um arquivo.

    Args:
        modelPath (str): Caminho do arquivo contendo o modelo.

    Returns:
        tuple: Tupla contendo listas para variáveis, terminais e produções.
    """
    file = open(modelPath).read()
    K = (file.split("Variaveis:\n")[0].replace("Terminais:\n", "").replace("\n", ""))
    V = (file.split("Variaveis:\n")[1].split("Producoes:\n")[0].replace("Variables:\n", "").replace("\n", ""))
    P = (file.split("Producoes:\n")[1])

    return cleanAlphabet(K), cleanAlphabet(V), cleanProduction(P)


def cleanProduction(expression):
    """
    Limpa a expressão de produção.

    Args:
        expression (str): Expressão de produção.

    Returns:
        list: Lista de tuplas representando as produções limpas.
    """
    result = []
    rawRules = expression.replace('\n', '').split(';')

    for rule in rawRules:
        leftSide = rule.split(' -> ')[0].replace(' ', '')
        rightTerms = rule.split(' -> ')[1].split(' | ')
        for term in rightTerms:
            result.append((leftSide, term.split(' ')))
    return result


def cleanAlphabet(expression):
    """
    Limpa a expressão de alfabeto.

    Args:
        expression (str): Expressão de alfabeto.

    Returns:
        list: Lista de símbolos limpa.
    """
    return expression.replace('  ', ' ').split(' ')


def seekAndDestroy(target, productions):
    """
    Busca e destrói produções contendo o alvo especificado.

    Args:
        target (str): Alvo a ser buscado nas produções.
        productions (list): Lista de produções.

    Returns:
        tuple: Tupla contendo as produções a serem removidas e as produções restantes.
    """
    trash, erased = [], []
    for production in productions:
        if target in production[right] and len(production[right]) == 1:
            trash.append(production[left])
        else:
            erased.append(production)

    return trash, erased


def setupDict(productions, variables, terms):
    """
    Configura um dicionário com base nas produções, variáveis e terminais.

    Args:
        productions (list): Lista de produções.
        variables (list): Lista de variáveis.
        terms (list): Lista de terminais.

    Returns:
        dict: Dicionário configurado.
    """
    result = {}
    for production in productions:
        if production[left] in variables and production[right][0] in terms and len(production[right]) == 1:
            result[production[right][0]] = production[left]
    return result


def rewrite(target, production):
    """
    Reescreve a produção substituindo o alvo por diferentes combinações.

    Args:
        target (str): Alvo a ser substituído.
        production (tuple): Produção a ser reescrita.

    Returns:
        list: Lista de produções resultantes.
    """
    result = []
    positions = [i for i, x in enumerate(production[right]) if x == target]

    for i in range(len(positions) + 1):
        for element in list(itertools.combinations(positions, i)):
            tadan = [production[right][i] for i in range(len(production[right])) if i not in element]

            if tadan != []:
                result.append((production[left], tadan))
    return result

def structuredForm(rules):
    """
    Retorna uma representação mais bem estruturada visualmente das regras.

    Args:
        rules (list): Lista de regras.

    Returns:
        str: Representação mais estruturada visualmente das regras.
    """
    dictionary = {}
    for rule in rules:
        if rule[left] in dictionary:
            dictionary[rule[left]] += ' | ' + ' '.join(rule[right])
        else:
            dictionary[rule[left]] = ' '.join(rule[right])
    result = ""
    for key in dictionary:
        result += key + " -> " + dictionary[key] + "\n"
    return result


def startingRuleFirst(gramatica):
    """
    Move a regra inicial para o início da lista de regras.

    Args:
        gramatica (Gramatica): A gramática.

    Returns:
        gramatica: Gramática com a regra inicial no início.
    """
    for rule in gramatica.rules:
        if rule[0] == gramatica.initial:
            initial_rule = rule
            gramatica.rules.remove(rule)
            gramatica.rules.insert(0, initial_rule)

    gramatica.variables.remove(gramatica.initial)
    gramatica.variables.insert(0, gramatica.initial)

    return gramatica


def findRulesRelatedToTerminals(gramatica):
    """
    Encontra regras relacionadas aos terminais na gramática.

    Args:
        gramatica (Gramatica): A gramática.

    Returns:
        list: Lista de regras relacionadas aos terminais.
    """
    X = []
    for lhs, rhs in gramatica.rules:
        for x in rhs:
            if len(x) == 1:
                if x in gramatica.terminals:
                    X.append((lhs, rhs))
    return X


def findRulesRelatedToVariables(gramatica):
    """
    Encontra regras relacionadas às variáveis na gramática.

    Args:
        gramatica (Gramatica): A gramática.

    Returns:
        list: Lista de regras relacionadas às variáveis.
    """
    X = []
    for lhs, rhs in gramatica.rules:

        if rhs[0] in gramatica.variables:
            if len(rhs) > 1:
                if rhs[0] in gramatica.variables or rhs[1] in gramatica.variables:
                    X.append((lhs, rhs))
            else:
                X.append((lhs, rhs))
        elif len(rhs) > 1:
            if rhs[1] in gramatica.variables:
                if rhs[0] in gramatica.variables or rhs[1] in gramatica.variables:
                    X.append((lhs, rhs))

    return X


def isUnitary(rule, variables):
    """
    Verifica se uma regra é unitária.

    Args:
        rule (tuple): A regra.
        variables (list): Lista de variáveis.

    Returns:
        bool: True se a regra for unitária, False caso contrário.
    """
    if rule[left] in variables and rule[right][0] in variables and len(rule[right]) == 1:
        return True
    return False


def isSimple(rule, variables, terminals):
    """
    Verifica se uma regra é simples.

    Args:
        rule (tuple): A regra.
        variables (list): Lista de variáveis.
        terminals (list): Lista de terminais.

    Returns:
        bool: True se a regra for simples, False caso contrário.
    """
    if rule[left] in variables and rule[right][0] in terminals and len(rule[right]) == 1:
        return True
    return False


def defineVariable(V):
    """
    Define uma variável para a gramática.

    Args:
        V (list): Lista de variáveis.

    Returns:
        None
    """
    variablesJar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "W", "X", "Y", "Z"]
    for nonTerminal in V:
        if nonTerminal in variablesJar:
            variablesJar.remove(nonTerminal)
    if len(variablesJar) > 0:
        VARIABLE = variablesJar.pop()


def getNewVar():
    """
    Gera uma nova variável.

    Returns:
        str: Nova variável.
    """
    global COUNTER
    newVar = str(VARIABLE) + "_" + str(COUNTER)
    COUNTER += 1
    return newVar


def START(productions, variables):
    """
    Adiciona uma nova regra inicial à gramática.

    Args:
        productions (list): Lista de produções.
        variables (list): Lista de variáveis.

    Returns:
        tuple: Lista de produções atualizada e a nova regra inicial.
    """
    variables.append(variables[0]+'_0')
    return [(variables[0]+'_0', [variables[0]])] + productions, variables[0] + '_0'


def TERM(productions, variables, terminals):
    """
    Substitui regras que contêm terminais.

    Args:
        productions (list): Lista de produções.
        variables (list): Lista de variáveis.
        terminals (list): Lista de terminais.

    Returns:
        list: Lista de produções atualizada.
    """
    newProductions = []
    dictionary = setupDict(productions, variables, terms=terminals)
    for production in productions:
        if isSimple(production, variables, terminals):
            newProductions.append(production)
        else:
            for term in terminals:
                for index, value in enumerate(production[right]):
                    if term == value and not term in dictionary:
                        dictionary[term] = getNewVar()
                        variables.append(dictionary[term])
                        newProductions.append((dictionary[term], [term]))
                        production[right][index] = dictionary[term]
                    elif term == value:
                        production[right][index] = dictionary[term]
            newProductions.append((production[left], production[right]))

    return newProductions

def BIN(productions, variables):
    """
    Aplica a transformação BIN a produções gramaticais.

    Args:
        productions (list): Lista de produções da gramática.
        variables (list): Lista de variáveis da gramática.

    Returns:
        list: Lista de produções após a transformação BIN.
    """
    result = []
    for production in productions:
        k = len(production[right])
        if k <= 2:
            result.append(production)
        else:
            newVar = getNewVar()
            variables.append(newVar)
            result.append((production[left], [production[right][0]] + [newVar]))
            for i in range(1, k - 2):
                var, var2 = newVar + str(i), newVar + str(i + 1)
                variables.append(var2)
                result.append((var, [production[right][i], var2]))
            result.append((newVar, production[right][k - 2:k]))
    return result


def DEL(productions):
    """
    Remove regras não-terminais vazias da gramática.

    Args:
        productions (list): Lista de produções da gramática.

    Returns:
        list: Lista de produções após a remoção de regras não-terminais vazias.
    """
    newSet = []
    outlaws, productions = seekAndDestroy(target='ε', productions=productions)
    for outlaw in outlaws:
        for production in productions + [e for e in newSet if e not in productions]:
            if outlaw in production[right]:
                newSet = newSet + [e for e in rewrite(outlaw, production) if e not in newSet]
    return newSet + ([productions[i] for i in range(len(productions)) if productions[i] not in newSet])

def unit_routine(rules, variables):
    """
    Remove regras unitárias da lista de regras de uma gramática.

    Args:
        rules (list): Lista de regras da gramática.
        variables (list): Lista de variáveis da gramática.

    Returns:
        list: Lista de regras após a remoção de regras unitárias.
    """
    unitaries, result = [], []

    for aRule in rules:
        if isUnitary(aRule, variables):
            unitaries.append((aRule[left], aRule[right][0]))
        else:
            result.append(aRule)

    for uni in unitaries:
        for rule in rules:
            if uni[right] == rule[left] and uni[left] != rule[left]:
                result.append((uni[left], rule[right]))

    return result

def UNIT(productions, variables):
    """
    Remove regras unitárias da gramática.

    Args:
        productions (list): Lista de produções da gramática.
        variables (list): Lista de variáveis da gramática.

    Returns:
        list: Lista de produções após a remoção de regras unitárias.
    """
    i = 0
    result = unit_routine(productions, variables)
    tmp = unit_routine(result, variables)
    while result != tmp and i < 1000:
        result = unit_routine(tmp, variables)
        tmp = unit_routine(result, variables)
        i += 1
    return result


def anulavel(gramatica):
    """
    Identifica variáveis anuláveis na gramática.

    Args:
        gramatica (Gramatica): A gramática.

    Returns:
        list: Lista de variáveis anuláveis.
    """
    null = []
    todo = []
    vars = findRulesRelatedToVariables(gramatica)
    oneVar = []
    twoVar = []
    occurs = {}

    for var in gramatica.variables:
        occurs[var] = []

    for lhs, rhs in vars:
        if len(rhs) == 1 and rhs[0] in gramatica.variables:
            oneVar.append((lhs[0], rhs[0]))
        elif len(rhs) == 2 and rhs[0] in gramatica.variables and rhs[1] in gramatica.variables:
            twoVar.append((lhs[0], rhs))

    for lhs, rhs in oneVar:
        occurs[rhs].append(lhs)

    for lhs, rhs in twoVar:
        occurs[rhs[0]].append((lhs, rhs[1]))
        occurs[rhs[1]].append((lhs, rhs[0]))

    for lhs, rhs in gramatica.rules:
        if rhs[0] == "ε":
            null.append(lhs)
            todo.append(lhs)

    while len(todo) > 0:
        B = todo.pop()
        X = occurs[B]
        foundTuples = []
        for rules in X:
            if type(rules) is tuple:
                foundTuples.append(rules)
            for tuples in foundTuples:
                if tuples[0] in X:
                    null.append(tuples[0])
                    todo.append([tuples[0]])
    return null