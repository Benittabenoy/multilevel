class Editor:
    def functionalities(self):
        self.funcs = ["createnewfile", "execute", "save"]

        return self.funcs

class Pycharm(Editor):
        def functionalities(self):
            funcs = super().functionalities()
            funcs.append(["debug","versioncontrolling"])
            return funcs
pyc=Pycharm()
print(pyc.functionalities())