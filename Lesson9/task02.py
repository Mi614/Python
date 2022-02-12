class Road:

    def __init__(self, l, w, d=5):
        self._length = l
        self._width = w
        self._depth = d

    def calc(self):
        mass = self._length * self._width * 0.025 * self._depth
        return mass


run = Road(5000, 20, 4)
print(f'{run.calc()} т')
