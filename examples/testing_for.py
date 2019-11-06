import sys
sys.path.append('..')

from pyInputTester.tools.GeneratorInput import GeneratorInput

generator = GeneratorInput(1, path_to_file='.test_for')

cases = generator.generate_inputs()
print(cases)