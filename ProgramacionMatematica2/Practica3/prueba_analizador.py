from analizador import Analizador, File_reading, File_writing
import sys
import re

name = sys.argv[1]

t = File_reading().lectura(name)
x = Analizador().analizar(t)
print(x)

d = File_writing().escritura(x)
'''
print(t)

palabra = 'turing'
for p in t:
    print(re.search(palabra,p))
'''
