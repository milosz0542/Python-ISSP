class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

radius = float(input("Podaj promień koła: "))
circle = Circle(radius)
print(f"Pole koła: {circle.area()}")
print(f"Obwód koła: {circle.perimeter()}")