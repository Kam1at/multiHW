class Vehicle:

    def __init__(self, position):  # position: кортеж (10, 20)
        self.position = position

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    @staticmethod
    def calculate_route(source, to):
        return 0  # to be realized

    def move_along(self, route):
        print("moving")

class Radio:
    def turn_on_radio(self, radio):
        print(f'Playing {radio}')


class Car(Vehicle, Radio):
    pass


class Airplane(Vehicle):
    pass


car = Car((10, 20))
car.turn_on_radio('Moscow FM')