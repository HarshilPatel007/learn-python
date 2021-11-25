
import typing


# Duck typing

class VSCode:

    def cmpil(self):
        print("Compiling the code...")

    def run(self):
        print("Running the code...")


class Code:

    def compile_code(self, ide):
        ide.cmpil()

    def run_code(self, ide):
        ide.run()


x = VSCode()

y = Code()
y.compile_code(x)
y.run_code(x)
