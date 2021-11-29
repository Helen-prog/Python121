from math import pi

p = pi


class Circle:

    def __init__(self, r):
        self.r = r

    def get_circle_square(self):
        res = p * self.r ** 2
        print(f"Площадь круга: {round(res, 2)}")
        return res

    def get_circle_circumference(self):
        res = 2 * p * self.r
        print(f"Длинна окружности: {round(res, 2)}")
        return res

    def print_circle(self):
        print(f"Радиус: {self.r}")
