from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_area(self):
        p = self.calcular_perimetro() / 2
        return math.sqrt(p * (p - self.lado1) * (p - self.lado2) * (p - self.lado3))  # Heron


# Exercício
formas = [
    Retangulo(5, 10),
    Retangulo(3, 4),
    Triangulo(3, 4, 5),
    Triangulo(7, 8, 9)
]

for forma in formas:
    print(f"{forma.__class__.__name__}:")
    print(f"Área: {forma.calcular_area():.2f}")
    print(f"Perímetro: {forma.calcular_perimetro():.2f}")
    print("-" * 30)
