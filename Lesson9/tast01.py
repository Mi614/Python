from time import sleep


class TrafficLight:

    def __init__(self, **colors):
        self.__color = colors
        self.l_c = ['red', 'yellow', 'green']

    def running(self):
        while True:
            for num, val in enumerate(self.__color.items()):
                if val[0] != self.l_c[num]:
                    return print(f'Неправельный порядок !')
                print(val[0])
                sleep(int(val[1]))


run = TrafficLight(red=5, yellow=2, green=7)
run.running()

