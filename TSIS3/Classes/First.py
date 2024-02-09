class String:
    def __init__(self, inp):
        self.inp = inp
    def read(self):
        print("Your email or nickname " + self.inp)
inputt = String(input())
inputt.read()
#__init-инициализация класса
