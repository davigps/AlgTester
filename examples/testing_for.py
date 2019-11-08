import sys
sys.path.append('..')

from pyInputTester.tools.GeneratorInput import GeneratorInput

generator = GeneratorInput(1, 'for.test')

cases = generator.generate_inputs()
print(cases)
print(cases[0])