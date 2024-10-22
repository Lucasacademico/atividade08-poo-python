# api.py
from classes.autor import Autor
from classes.livro import Livro

# Estruturas de dados em memória
autores = []
livros = []

def obter_autores():
    return autores

def obter_livros():
    return livros

def adicionar_autor(nome, livros_autor):
    novo_autor = Autor(nome, livros_autor)  # Cria uma instância da classe Autor
    autores.append(novo_autor)  # Adiciona o autor à lista

def adicionar_livro(titulo, autor_nome, codigo):
    novo_livro = Livro(titulo, autor_nome, codigo)  # Cria uma instância da classe Livro
    livros.append(novo_livro)  # Adiciona o livro à lista
