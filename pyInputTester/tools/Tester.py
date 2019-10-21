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
        self.testsText = ""
        self.errorsText = ""

    # Run the tests in self.testCases and save it in self.result
    def run_tests(self):


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

    # Get the reports texts and save it on self.testsText and self.errorsText
    def get_reports(self):

        self.testsText = ''
        for i in range(len(self.result["tests"])):
            test = self.result["tests"][i]
            self.testsText += '### TEST {} ###\n=-= Input:\n{}=-= Output:\n{}\n'.format(
                    i + 1, test["input"], test["output"]
                    )

        self.errorsText = ''
        for i in range(len(self.result["errors"])):
            error = self.result["errors"][i]
            self.errorsText += '### ERROR {} ###\n=-= Input:\n{}=-= Output:\n{}\n'.format(
                    i + 1, error["input"], error["output"]
                    )

        return (self.testsText, self.errorsText)

    # Save the reports texts in .txt files
    def save_reports(self):
        tests, errors = self.get_reports()

        with open('tests.txt', 'w') as arq:
            arq.write(tests)
        with open('errors.txt', 'w') as arq:
            arq.write(errors)

    # Get an array with the tests
    def get_tests(self):
        return self.result['tests']

    # Get an array with the errors
    def get_errors(self):
        return self.result['errors']

    # Print the reports texts
    def print_reports(self):
        print(self.testsText)
        print(self.errorsText)

# You can import this function to make a regular test,
# with some test cases...
def test(target_filename, cases):
    tester = Tester(target_filename, cases)
    tester.run_tests()
    tester.save_reports()
    print('tests with "{}" file completed'.format(target_filename))
    return (tester.get_tests(), tester.get_errors())
