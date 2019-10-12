import os
import subprocess

class Tester:

    def __init__(self, arq, testCases):
        self.arq = arq
        self.testCases = testCases

        self.result = {
                "tests": [],
                "errors": []
                }
        self.tests = ""
        self.errors = ""

    def run_tests(self, limit=None):


        for case in self.testCases:

            tempOut = open('temp_out.txt', 'w')
            tempErr = open('temp_err.txt', 'w')

            process = subprocess.run(args=['python3 {}'.format(self.arq)],
                                   input=case, stdout=tempOut,
                                   stderr=tempErr, shell=True,
                                   universal_newlines=True)
            tempOut.close()
            tempErr.close()

            if process.returncode == 0:
                tempOut = open('temp_out.txt', 'r')
                self.result["tests"].append({
                    "input": case,
                    "output": tempOut.read()
                    })
                tempOut.close()
            else:
                tempErr = open('temp_err.txt', 'r')
                self.result["errors"].append({
                    "code": process.returncode,
                    "input": case,
                    "output": tempErr.read()
                    })
                tempErr.close()

        os.remove('temp_out.txt')
        os.remove('temp_err.txt')

        return self.result

    def get_reports(self):

        self.tests = ''
        for i in range(len(self.result["tests"])):
            test = self.result["tests"][i]
            self.tests += '### TEST {} ###\n=-= Input:\n{}=-= Output:\n{}\n'.format(
                    i + 1, test["input"], test["output"]
                    )

        self.errors = ''
        for i in range(len(self.result["errors"])):
            error = self.result["errors"][i]
            self.errors += '### ERROR {} ###\n=-= Input:\n{}=-= Output:\n{}\n'.format(
                    i + 1, error["input"], error["output"]
                    )

        return (self.tests, self.errors)

    def save_reports(self):
        tests, errors = self.get_reports()

        with open('tests.txt', 'w') as arq:
            arq.write(tests)
        with open('errors.txt', 'w') as arq:
            arq.write(errors)

    def print_reports(self):
        print(self.tests)
        print(self.errors)

# You can use this function to make a regular test,
# with some test cases...
def test(arq, cases):
    tester = Tester(arq, cases)
    tester.run_tests()
    tester.save_reports()
    print('tests with "{}" file completed'.format(arq))
    return tester.get_reports()

# Usage Example with ee.py in source code.
if __name__ == "__main__":
    # Two successful tests and one failed test
    testCases = [
            'jose vermelho\nfim\n',
            'clara amarelo\ndavi laranja\ngabriel amarelo\nfim\n',
            'maria azul\nfirmino\nfim\n'
            ]

    # Create the Tester Object
    hospTester = Tester('hospital.py', testCases)

    # Run tests and save in attributes like "errors" or "tests"
    hospTester.run_tests()

    # Get and save result attributes in .txt files
    hospTester.save_report()

    # Print the result attributes
    hospTester.print_reports()
