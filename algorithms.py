class Cyk:
    def run(rules, input):
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
    pass
