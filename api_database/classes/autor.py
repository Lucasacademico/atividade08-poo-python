class Autor:
    def __init__(self, nome, livros):
        self.__nome = nome
        self.__livros = livros

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def mostrar_livros(self):
        for livro in self.__livros:
            print(livro)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_livros(self):
        return self.__livros

    def set_livros(self, livros):
        self.__livros = livros




