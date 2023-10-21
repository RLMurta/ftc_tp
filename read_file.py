from normal_forms import ChomskyNormalForm, SecondNormalForm

class ReadFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name) as f:
            self.file = f.read()

    def read_cnf(self):
        pass
    
    def read_2nf(self):
        pass
