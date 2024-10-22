from classes.autor import Autor

class Livro:
    def __init__(self, titulo: str, autor: Autor, codigo: str):
        self.__titulo = titulo         
        self.__autor = autor            # Autor do livro (composição)
        self.__codigo = codigo          
        self.__disponivel = True        

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"O livro '{self.__titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.__titulo}' não está disponível para empréstimo.")

    def devolver(self):
        self.__disponivel = True
        print(f"O livro '{self.__titulo}' foi devolvido e está disponível.")

    def get_titulo(self) -> str:
        return self.__titulo

    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def get_autor(self) -> Autor:
        return self.__autor

    def set_autor(self, autor: Autor):
        self.__autor = autor

    def get_codigo(self) -> str:
        return self.__codigo

    def set_codigo(self, codigo: str):
        self.__codigo = codigo

    def is_disponivel(self) -> bool:
        return self.__disponivel

    # Setter para o atributo disponivel (se necessário)
    def set_disponivel(self, disponivel: bool):
        self.__disponivel = disponivel