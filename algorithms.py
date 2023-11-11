import networkx as nx
import matplotlib.pyplot as plt

class Cyk:
    def run(rules, input):
        input = input.replace(" ", "")
        starting_symbol = list(rules.keys())[0]
        n = len(input)
        table = [[set() for _ in range(n - i)] for i in range(n)]

        for i in range(n):
            for variable in rules:
                for rule in rules[variable]:
                    if input[i] in rule:
                        table[i][0].add(variable)

        for j in range(1, n):
            for i in range(n - j):
                for k in range(j):
                    for variable in rules:
                        for rule in rules[variable]:
                            if rule[0] in table[i][k] and rule[1] in table[i + k + 1][j - k - 1]:
                                table[i][j].add(variable)

        return starting_symbol in table[0][n - 1]
    
class ModifiedCyk:
    def __init__(self):
        pass

    def run(self, rules, input):
        input = input.replace(" ", "")
        starting_symbol = list(rules.keys())[0]
        inverse_unit_graph = self.__inverse_unit_graph(rules)
        n = len(input)
        table = [[set() for _ in range(n)] for i in range(n)]
        star_table = [[set() for _ in range(n)] for i in range(n)]

        for i in range(n):
            table[i][i] = list(nx.dfs_edges(inverse_unit_graph, input[i]))

        for j in range(2, n):
            for i in range(j-1,1,-1):
                table[i][j] = list()
                for h in range(i,j-1):
                    for variable in rules:
                        for rule in rules[variable]:
                            if (len(rule) == 2 and (rule.islower() or rule.isalpha() is False)):
                                if(rule[0] in table[i][h] and rule[1] in table[h+1][j]):
                                    star_table[i][j].append(variable)
                for a in star_table[i][j]:
                    for b in list(nx.dfs_edges(inverse_unit_graph, a)):
                        table[i][j].append(b)
        return starting_symbol in table[0][n - 1]
    
    def __inverse_unit_graph(self, rules):
        graph = nx.Graph()
        for variable in rules:
            graph.add_node(variable)
        for variable in rules:
            for rule in rules[variable]:
                if (len(rule) == 1 and (rule.islower() or rule.isalpha() is False)):
                    graph.add_edge(variable, rule)
                elif(len(rule) == 2 and (rule[0].islower() or rule[0].isalpha() is False)):
                    graph.add_edge(rule[0], variable)
                elif(len(rule) == 2 and (rule[1].islower() or rule[1].isalpha() is False)):
                    graph.add_edge(rule[1], variable)
        return graph
