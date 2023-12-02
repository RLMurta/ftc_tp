import matplotlib.pyplot as plt
import methods

class Cyk:
    def run(gramatica, entrada):
        """
        Executa o algoritmo CYK para verificar se a gramática gera a entrada fornecida.

        Args:
            gramatica (dict): As regras da gramática.
            entrada (str): A entrada a ser verificada.

        Returns:
            bool: True se a gramática gera a entrada, False caso contrário.
        """
        terminais = methods.findRulesRelatedToTerminals(gramatica)
        vars = methods.findRulesRelatedToVariables(gramatica)

        entrada = entrada.replace(" ", "")
        n = len(entrada)
        table = [[[] for _ in range(n)] for _ in range(n)]

        # Preenche a tabela para o primeiro caractere da entrada
        for i in range(0, n):
            terminal = entrada[i]
            for rule in terminais:
                if terminal in rule[1]:
                    table[i][i].append(rule[0])

        # Preenche a tabela para os caracteres subsequentes
        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                for k in range(i, j):
                    for rule in vars:
                        if len(rule) > 0 and (rule[1][0] in table[i][k] and rule[1][1] in table[k + 1][j]):
                            table[i][j].append(rule[0])

        return gramatica.variables[0] in table[0][n - 1]

class ModifiedCyk:
    def run(gramatica, entrada, anulaveis):
        """
        Executa o algoritmo CYK modificado para verificar se a gramática gera a entrada fornecida, levando em conta
        símbolos nulos.

        Args:
            gramatica (dict): As regras da gramática.
            entrada (str): A entrada a ser verificada.
            anulaveis (set): Conjunto de símbolos nulos.

        Returns:
            bool: True se a gramática gera a entrada, False caso contrário.
        """
        terminais = methods.findRulesRelatedToTerminals(gramatica)

        entrada = entrada.replace(" ", "")
        graph = ModifiedCyk.inverseUnitGraph(gramatica, anulaveis)

        n = len(entrada)
        table = [[[] for _ in range(n)] for _ in range(n)]
        star_table = [[[] for _ in range(n)] for _ in range(n)]

        # Preenche a tabela para substrings de comprimento 1
        for i in range(0, n):
            for rule in terminais:
                reach = ModifiedCyk.discoverReach(graph, [entrada[i]])
                table[i][i] = reach
        #print("tabela para substrings de comprimento 1")
        #ModifiedCyk.print_cyk_table(table)

        # Preenche a tabela para substrings de comprimento maior que 1
        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                for h in range(i, j):
                    for rule in gramatica.rules:
                        if len(rule[1]) >= 2:
                            if(rule[1][0] in table[i][h] and rule[1][1] in table[h + 1][j]):
                                star_table[i][j].append(rule[0])

                table[i][j] = ModifiedCyk.discoverReach(graph, star_table[i][j])
            #print("# Preenche a tabela para substrings de comprimento maior que 1")
            #ModifiedCyk.print_cyk_table(table)
        return gramatica.variables[0] in table[0][n - 1]
    
    def print_cyk_table(table):
        """
        Imprime a tabela CYK durante o preenchimento.

        Args:
            table (list): Tabela CYK preenchida.
        """
        n = len(table[0])

        print("Tabela CYK:")
        for i in range(n):
            for j in range(n - i):
                print(table[j][j + i], end="\t")
            print()

    def inverseUnitGraph(gramatica, anulaveis):
        """
        Cria o grafo invertido para símbolos nulos.

        Args:
            gramatica (dict): As regras da gramática.
            anulaveis (set): Conjunto de símbolos nulos.

        Returns:
            dict: Grafo invertido.
        """
        graph = {}

        for lhs, rhs in gramatica.rules:
            if len(rhs) > 1:
                if rhs[0] in anulaveis:
                    if (graph.get(rhs[1]) == None):
                        graph[rhs[1]] = []
                    graph[rhs[1]].append(lhs)

                if rhs[1] in anulaveis:
                    if (graph.get(rhs[0]) == None):
                        graph[rhs[0]] = []
                    graph[rhs[0]].append(lhs)

            elif rhs[0] != 'ε':
                if (graph.get(rhs[0]) == None):
                    graph[rhs[0]] = []
                graph[rhs[0]].append(lhs)

        return graph

    def discoverReach(graph, word_list):
        """
        Descobre os símbolos alcançáveis em um grafo a partir de uma lista de palavras.

        Args:
            graph (dict): Grafo a ser analisado.
            word_list (list): Lista de palavras.

        Returns:
            list: Lista de símbolos alcançáveis.
        """
        canReach = set()
        for node in word_list:
            visited = ModifiedCyk.dfs(graph, node)
            for i in range(0, len(visited)):
                canReach.add(visited[i])
        

        return list(canReach)

    def dfs(graph, node):
        """
        Realiza uma busca em profundidade (DFS) em um grafo a partir de um nó.

        Args:
            graph (dict): Grafo a ser analisado.
            node (str): Nó inicial.

        Returns:
            list: Lista de nós alcançáveis.
        """
        if graph.get(node) is None:
            return [node]

        visited = [node]
        togo = [node]

        for i in range(0, len(node)):
            togo.append(graph[node][i])
            visited.append(graph[node][i])

        while len(togo) != 0:
            next = togo.pop()
            if graph.get(next) is not None:
                for edge in range(0, len(graph[next])):
                    vertex = graph[next][edge]
                    if vertex not in visited:
                        togo.append(vertex)
                        visited.append(vertex)
        return visited