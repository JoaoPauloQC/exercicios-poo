import math

class Circulo:
    def __init__(self, raio: float):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio


# Exercício
c1 = Circulo(2)
c2 = Circulo(5)
c3 = Circulo(10)

for c in [c1, c2, c3]:
    print(f"Raio: {c.raio}")
    print(f"Área: {c.calcular_area():.2f}")
    print(f"Perímetro: {c.calcular_perimetro():.2f}")
    print("-" * 30)
