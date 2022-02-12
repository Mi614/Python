class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки, {self.title} пишет')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки, {self.title} чертит')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки, {self.title} рисует')


run = Pen('ручка')
run.draw()
run = Pencil('карандаш')
run.draw()
run = Handle('маркер')
run.draw()
