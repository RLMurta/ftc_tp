from read_file import ReadFile
from normal_forms import ChomskyNormalForm, SecondNormalForm
from algorithms import Cyk, ModifiedCyk
import methods
import time

cnf_file = ReadFile('cfg_file.cnf')
rules = methods.copy_dict(cnf_file.rules)

chomsky_normal_form_start_time = time.time()
chomsky_normal_form = ChomskyNormalForm().cfg_to_cnf(rules)
print(Cyk.run(chomsky_normal_form, '(a(a)a)'))
chomsky_normal_form_total_time = time.time() - chomsky_normal_form_start_time
print(chomsky_normal_form)

rules = cnf_file.rules.copy()
second_normal_form_start_time = time.time()
second_normal_form = SecondNormalForm().cfg_to_2nf(rules)
second_normal_form_total_time = time.time() - second_normal_form_start_time
print(second_normal_form)

print('Chomsky Normal Form: ', round(chomsky_normal_form_total_time, 5))
print('Second Normal Form: ', round(second_normal_form_total_time, 5))


