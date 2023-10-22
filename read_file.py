from normal_forms import ChomskyNormalForm, SecondNormalForm

class ReadFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.__read()
        self.__separate_rules()
        self.chomsky_normal_form = ChomskyNormalForm(self.rules)
        self.chomsky_normal_form.cfg_to_cnf()

    def __read(self):
        with open(self.file_name) as f:
            self.file = f.read()

    def __separate_rules(self):
        rules = self.file.splitlines()
        treated_rules = dict()
        for rule in rules:
            variable = rule.split('->')[0].replace(" ", "")
            treated_rules[variable] = rule.split('->')[1].replace(" ", "").split('|')
        self.rules = treated_rules
