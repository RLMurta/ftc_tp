class ReadFile:
    def __init__(self, file_name):
        """
        Inicializa uma instância da classe ReadFile.

        Args:
            file_name (str): O nome do arquivo a ser lido.
        """
        self.file_name = file_name
        self.__read()
        self.__separate_rules()

    def __read(self):
        """
        Lê o conteúdo do arquivo e armazena na variável de instância 'file'.
        """
        with open(self.file_name) as f:
            self.file = f.read()

    def __separate_rules(self):
        """
        Separa as regras do arquivo e armazena em um dicionário de regras tratadas.
        """
        rules = self.file.splitlines()
        treated_rules = dict()

        for rule in rules:
            variable = rule.split('->')[0].replace(" ", "")
            treated_rules[variable] = rule.split('->')[1].replace(" ", "").split('|')

        self.rules = treated_rules
