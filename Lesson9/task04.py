import random


class Car:

    def __init__(self, s, c, n, p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p

    def show_speed(self):
        return self.speed

    def go(self):
        print(f'{self.color} {self.name} started moving at a speed {self.show_speed()} km/h')

    def stop(self):
        self.speed = 0
        print (f'{self.color} {self.name} is stop')
        return self.show_speed()

    def turn(self):
        direction = ['left', 'right', 'back']
        print(f'{self.color} {self.name} turn {direction[random.randint(0, 2)]} at a speed {self.show_speed()}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60 and self.is_police == False:
            print(f'WARNING! Speed out limit!')
        return self.speed


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40 and self.is_police == False:
            print(f'WARNING! Speed out limit!')
        return self.speed

run = TownCar(61, 'red', 'mazda', False)
run.go()
run.turn()

run = WorkCar(72, 'black', 'ford', True)
run.go()
run.turn()
