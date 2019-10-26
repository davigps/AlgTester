import sys
sys.path.append('../')

from pyInputTester.tools import Tester
from random import randint, choice

# You can automatically generate all tests cases, with the GeneratorInput Class.
cases = []
for i in range(randint(10,30)):
    a = randint(-999, 999)
    b = randint(-999, 999)

    # Generating bugs
    if a % 7 == 0:
        a = choice('abfmsefnefn')
    if b % 8 == 0:
        b = choice('abcdefghijk')

    case = '{} {}\n'.format(a, b)
    cases.append(case)

# Testing the example1.py with the generated cases...
tester = Tester('example1.py', cases)

# Run the tests cases
tester.run_tests()

# Only get and print the reports
tester.get_reports()
tester.print_reports()

ans = input('Do you want to save the reports? [Y/n] ')
if ans in 'Yy':
    tester.save_reports()