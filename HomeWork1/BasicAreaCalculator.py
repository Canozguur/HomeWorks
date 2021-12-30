import math


class Area:
    length =0
    width =0
    @staticmethod
    def rectangle(length, width):
        return length * width
    @staticmethod
    def triangle(a, b, c):
        s = (a + b + c)/2

        return math.sqrt(s*(s - a)*(s - b)*(s - c))
    @staticmethod
    def trapezoid(a, b, height):
        return ((a + b) / 2) * height

    @staticmethod
    def circle(r):
        return math.pi * r

    @staticmethod
    def sector(radius, angle):
        return (angle / 360) * math.pi * radius * radius

    @staticmethod
    def ellipse(a, b):
        return math.pi * a * b

    @staticmethod
    def parallelogram(base, height):
        return base * height

print(f"LENGTH = 30 WIDTH=20 Rectangle Area is {Area.rectangle(30,20)}")
print(f"A=30 B=45 C=50 TRIANGLE Area is {Area.triangle(30,45,50)}")
print(f"A=30 B=45 HEIGHT = 20 Area is {Area.trapezoid(30,45,20)}")
print(f"Radius(r) = 30 CIRCLE Area is {Area.circle(30)}")
print(f"Radius(r) = 30 ANGLE = 90 SECTOR Area is {Area.sector(30,90)}")
print(f"A= 30 B =20 ELLIPSE Area is {Area.ellipse(30,20)}")
print(f"Base = 30 HEIGHT= 20 PARALLELOGRAM Area is {Area.parallelogram(30,20)}")

