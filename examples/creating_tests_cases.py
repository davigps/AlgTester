import sys
sys.path.append('../')

from pyInputTester.tools.GeneratorInput import GeneratorInput

# If you don't set the input test configuration file name, '.test' file will be set.
# The first argument is the number of random tests cases.
gerador = GeneratorInput(5, 'example.test')

# This method will read the input test configuration and generate random inputs.
# A list with all the tests cases will be returned, so you can use it in Tester class.
inputs = gerador.generate_inputs()

print(inputs)
