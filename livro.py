class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.num_paginas}")
        print("-" * 30)


# Exercício
livros = [
    Livro("Dom Casmurro", "Machado de Assis", 256),
    Livro("O Hobbit", "J.R.R. Tolkien", 310),
    Livro("1984", "George Orwell", 328)
]

for livro in livros:
    livro.detalhes()
