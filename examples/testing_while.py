import sys

sys.path.append("..")

from pyInputTester.tools.GeneratorInput import GeneratorInput

generator = GeneratorInput(3, "while.test")

cases = generator.generate_inputs()
for case in cases:
    print(case)
