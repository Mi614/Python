class Worker:

    def __init__(self, n, sn, p, w, b):
        self.name = n
        self.surname = sn
        self.position = p
        self._income = {'wage': w, 'bonus': b}


class Position(Worker):

    def get_total_income(self):
        inc = self._income['wage'] + self._income['bonus']
        return inc

    def get_full_name(self):
        return f'{self.name} {self.surname}'


run = Position('John', 'Smith', 'agent', 1000, 500)
print(f'{run.get_full_name()} {run.get_total_income()} USD')
