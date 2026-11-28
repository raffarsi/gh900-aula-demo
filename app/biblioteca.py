"""Biblioteca escolar: lista livros."""

LIVROS = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890},
    {"titulo": "Vidas Secas", "autor": "Graciliano Ramos", "ano": 1938},
]


def listar():
    for livro in LIVROS:
        print(f"{livro['titulo']} ({livro['ano']}), de {livro['autor']}")


def buscar_por_autor(autor):
    termo = autor.casefold()
    return [livro for livro in LIVROS if termo in livro["autor"].casefold()]


if __name__ == "__main__":
    listar()
