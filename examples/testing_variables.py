import sys
sys.path.append('../')

from pyInputTester.tools.GeneratorInput import GeneratorInput

gerador = GeneratorInput(10, path_to_file='.test_variables')
gerador.search_variables()
print(gerador.variables)