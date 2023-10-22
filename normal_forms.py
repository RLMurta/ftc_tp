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
        new_rules = self.__remove_non_solitary_terminals(new_rules)
        print(new_rules)
        while self.__there_is_rules_whith_more_than_two_non_terminals(new_rules):
            new_rules = self.__remove_more_than_two_non_terminals(new_rules)
        print(new_rules)
        # new_rules = self.__remove_epsilon(new_rules)
        # print(new_rules)
        # new_rules = self.__remove_unitary(new_rules)
        # print(new_rules)
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

    def __remove_non_solitary_terminals(self, rules):
        new_rules = dict()
        for variable in rules:
            new_rules[variable] = rules[variable]
            for rule in rules[variable]:
                if len(rule) > 1 and rule.islower() is False and rule.isupper() is False:
                    new_rules[variable].remove(rule)
                    new_rule = ''
                    for i in range(len(rule)):
                        if rule[i].islower():
                            new_variable = self.__get_a_variable()
                            new_rules[new_variable] = [rule[i]]
                            new_rule += new_variable
                        else:
                            new_rule += rule[i]
                    new_rules[variable].append(new_rule)
        return new_rules
    
    def __there_is_rules_whith_more_than_two_non_terminals(self, rules):
        for variable in rules:
            for rule in rules[variable]:
                if len(rule) > 2 and rule.isupper():
                    return True
        return False
    
    def __remove_more_than_two_non_terminals(self, rules):
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

    def __remove_epsilon(self, rules):
        pass

    def __remove_unitary(self, rules):
        pass


class SecondNormalForm:
    def __init__(self, rules):
        self.rules = rules

    def cfg_to_2nf(self):
        pass
