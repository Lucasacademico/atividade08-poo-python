class Biblioteca:
    total_livros = 0  # Variável de classe que armazena o número total de livros

    def __init__(self, nome: str):
        self.nome = nome  # Nome da biblioteca
        self.__livros = []  # Lista de livros disponíveis (privado)
        self.__emprestimos = {}  # Dicionário de empréstimos (privado)

    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        Biblioteca.total_livros += 1  # Incrementa o total de livros
        print(f"O livro '{livro.get_titulo()}' foi adicionado à biblioteca.")

    # Novo método para acessar livros
    def obter_livros(self):
        return self.__livros

    def registrar_emprestimo(self, codigo_livro: str, cliente: str):
        for livro in self.__livros:
            if livro.get_codigo() == codigo_livro:
                if livro.is_disponivel():
                    livro.emprestar()  # Marca o livro como não disponível
                    self.__emprestimos[codigo_livro] = cliente  # Adiciona ao dicionário de empréstimos
                    print(f"Empréstimo registrado: '{livro.get_titulo()}' para o cliente {cliente}.")
                else:
                    print(f"O livro '{livro.get_titulo()}' não está disponível para empréstimo.")
                return
        print("Código do livro não encontrado.")

    def registrar_devolucao(self, codigo_livro: str):
        if codigo_livro in self.__emprestimos:
            for livro in self.__livros:
                if livro.get_codigo() == codigo_livro:
                    livro.devolver()  # Marca o livro como disponível
                    del self.__emprestimos[codigo_livro]  # Remove do dicionário de empréstimos
                    print(f"A devolução do livro '{livro.get_titulo()}' foi registrada.")
                    return
        print("Código do livro não encontrado nos empréstimos.")

    def mostrar_livros_disponiveis(self):
        print("Livros disponíveis para empréstimo:")
        for livro in self.__livros:
            if livro.is_disponivel():
                print(f"- {livro.get_titulo()} (Código: {livro.get_codigo()})")

    @classmethod
    def mostrar_total_livros(cls):
        print(f"Número total de livros na biblioteca: {cls.total_livros}")
