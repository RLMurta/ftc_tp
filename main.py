from read_file import ReadFile

cnf_file = ReadFile('cnf_file.cnf')
cnf_file.read()
print(cnf_file.file.splitlines())
