from read_file import ReadFile
from normal_forms import ChomskyNormalForm, SecondNormalForm
from algorithms import Cyk, ModifiedCyk

cnf_file = ReadFile('cfg_file.cnf')
chomsky_normal_form = ChomskyNormalForm(cnf_file.rules).cfg_to_cnf()
print(Cyk.run(chomsky_normal_form, '(a(a)a)'))
