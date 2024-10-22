from flask import Flask, render_template, request, redirect, url_for
from classes.autor import Autor
from classes.livro import Livro
from classes.biblioteca import Biblioteca
from api import obter_autores, obter_livros, adicionar_autor, adicionar_livro

app = Flask(__name__)

# Definindo a biblioteca globalmente
biblioteca = Biblioteca("Minha Biblioteca")

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/adicionar_autor', methods=['GET', 'POST'])
def adicionar_autor():
    if request.method == 'POST':
        nome = request.form['nome']
        livros = request.form.getlist('livros')
        adicionar_autor(nome, livros)  # Adiciona autor à API
        return redirect(url_for('menu'))
    return render_template('adicionar_autor.html')

@app.route('/adicionar_livro', methods=['GET', 'POST'])
def adicionar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor_nome = request.form['autor']
        codigo = request.form['codigo']
        adicionar_livro(titulo, autor_nome, codigo)  # Adiciona livro à API
        return redirect(url_for('menu'))
    return render_template('adicionar_livro.html')

@app.route('/mostrar_livros')
def mostrar_livros():
    livros = obter_livros()  # Obtém livros da API
    return render_template('mostrar_livros.html', livros=livros)

@app.route('/registrar_emprestimo', methods=['GET', 'POST'])
def registrar_emprestimo():
    if request.method == 'POST':
        codigo_livro = request.form['codigo_livro']
        cliente = request.form['cliente']
        
        # Lógica para registrar o empréstimo
        if codigo_livro in biblioteca.livros:
            livro = biblioteca.livros[codigo_livro]
            if livro.disponivel:
                livro.disponivel = False  # Marca o livro como emprestado
                # Aqui você pode adicionar lógica para armazenar o cliente e a data do empréstimo
                return redirect(url_for('menu'))
            else:
                return "Este livro já está emprestado.", 400
        return "Código do livro inválido.", 400
    
    return render_template('registrar_emprestimo.html')

@app.route('/registrar_devolucao', methods=['GET', 'POST'])
def registrar_devolucao():
    if request.method == 'POST':
        codigo_livro = request.form['codigo_livro']
        # Lógica para registrar a devolução do livro
        if codigo_livro in biblioteca.livros:
            livro = biblioteca.livros[codigo_livro]
            if not livro.disponivel:
                livro.disponivel = True  # Marca o livro como disponível
                # Aqui você pode adicionar lógica para remover o cliente e a data da devolução
                return redirect(url_for('menu'))
            else:
                return "Este livro já está disponível.", 400
        return "Código do livro inválido.", 400
    
    return render_template('registrar_devolucao.html')

if __name__ == '__main__':
    app.run(debug=True)
