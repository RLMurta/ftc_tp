class ChomskyNormalForm:
    def __init__(self, rules):
        # ASCII code for A-Z
        self.available_variables = [chr(i) for i in range(65, 91)]
        self.rules = rules
        self.__remove_used_variables_from_available_variables()
        self.starting_symbol = list(self.rules.keys())[0]

    def cfg_to_cnf(self):
        new_rules = self.__new_starting_symbol(self.rules)
        print(new_rules)
        new_rules = self.__remove_rules_with_non_solitary_terminals(new_rules)
        print(new_rules)
        while self.__is_there_rules_with_more_than_two_non_terminals(new_rules):
            new_rules = self.__remove_rules_with_more_than_two_non_terminals(new_rules)
        print(new_rules)
        new_rules = self.__remove_epsilon_rules(new_rules)
        print(new_rules)
        while self.__is_there_unitary_variable_rules(new_rules):
            new_rules = self.__remove_unitary_variable_rules(new_rules)
        print(new_rules)
        new_rules = self.__remove_initial_rule(new_rules)
        print(new_rules)
        return new_rules
    
    def __remove_used_variables_from_available_variables(self):
        for variable in self.rules:
            if variable in self.available_variables:
                self.available_variables.remove(variable)

    def __get_a_variable(self):
        if len(self.available_variables) > 0:
            variable = self.available_variables[0]
            self.available_variables.remove(variable)
            return variable
        else:
            return None

    def __new_starting_symbol(self, rules):
        new_starting_symbol = 'S0'
        new_rules = {new_starting_symbol: [self.starting_symbol]}
        new_rules.update(rules)
        return new_rules

    def __remove_rules_with_non_solitary_terminals(self, rules):
        new_rules = dict()
        for variable in rules:
            new_rules[variable] = rules[variable]
            for rule in rules[variable]:
                if len(rule) > 1 and ((rule.islower() is False and rule.isupper() is False) or (rule.isalpha() is False) or (rule.islower())):
                    new_rules[variable].remove(rule)
                    new_rule = ''
                    for i in range(len(rule)):
                        if rule[i].isupper() is False:
                            new_variable = self.__get_a_variable()
                            new_rules[new_variable] = [rule[i]]
                            new_rule += new_variable
                        else:
                            new_rule += rule[i]
                    new_rules[variable].append(new_rule)
        return new_rules
    
    def __is_there_rules_with_more_than_two_non_terminals(self, rules):
        for variable in rules:
            for rule in rules[variable]:
                if len(rule) > 2 and rule.isupper():
                    return True
        return False
    
    def __remove_rules_with_more_than_two_non_terminals(self, rules):
        new_rules = dict()
        for variable in rules:
            new_rules[variable] = rules[variable]
            for rule in rules[variable]:
                if len(rule) > 2 and rule.isupper():
                    new_rules[variable].remove(rule)
                    new_rule = ''
                    new_rule += rule[0]
                    new_variable = self.__get_a_variable()
                    new_rule += new_variable
                    new_rules[variable].append(new_rule)
                    new_variable_rule = ''
                    for i in range(1,len(rule)):
                        new_variable_rule += rule[i]
                    new_rules[new_variable] = [new_variable_rule]
        return new_rules

    def __remove_epsilon_rules(self, rules):
        new_rules = rules
        for variable in rules:
            for rule in rules[variable]:
                if rule == 'ε':
                    new_rules[variable].remove(rule)
                    for variable2 in rules:
                        for rule2 in rules[variable2]:
                            if variable in rule2:
                                if variable2 in new_rules:
                                    new_rules[variable2].append(rule2.replace(variable, ''))
                                else:
                                    new_rules[variable2] = [rule2.replace(variable, '')]
        return new_rules

    def __is_there_unitary_variable_rules(self, rules):
        for variable in rules:
            for rule in rules[variable]:
                if len(rule) == 1 and rule.isupper():
                    return True
        return False

    def __remove_unitary_variable_rules(self, rules):
        new_rules = rules
        for variable in rules:
            for rule in rules[variable]:
                if len(rule) == 1 and rule.isupper():
                    new_rules[variable].remove(rule)
                    for variable2 in rules:
                        if variable2 == rule:
                            for rule2 in rules[variable2]:
                                new_rules[variable].append(rule2)
        return new_rules
    
    def __remove_initial_rule(self, rules):
        new_rules = rules
        if rules[self.starting_symbol] == rules['S0']:
            new_rules.pop('S0')
        return new_rules


class SecondNormalForm:
    def __init__(self, rules):
        self.rules = rules

    def cfg_to_2nf(self):
        pass
