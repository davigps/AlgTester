import sys
sys.path.append('../')

from pyInputTester.tools.GeneratorInput import GeneratorInput

gerador = GeneratorInput(10, 'variables.test')
gerador.search_variables()
print(gerador.variables)