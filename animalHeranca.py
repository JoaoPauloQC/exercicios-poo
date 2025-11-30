class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico de animal.")


class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

    def latir(self):
        print("Woof woof!")


class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

    def miar(self):
        print("Meow meow!")


# Exercício
dog = Cachorro("Rex")
cat = Gato("Mingau")

dog.emitir_som()
dog.latir()

cat.emitir_som()
cat.miar()

# Polimorfismo
animais = [dog, cat]

print("\nDemonstração de polimorfismo:")
for animal in animais:
    animal.emitir_som()
