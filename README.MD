# Sistema de Biblioteca

## Cenário

Você é responsável por desenvolver um sistema para uma biblioteca fictícia. Este sistema deve ser capaz de:

- **Registrar e armazenar** informações sobre livros e autores.
- **Registrar e gerenciar** empréstimos de livros para clientes.
- **Calcular a quantidade total de livros** na biblioteca e gerenciar o número de livros emprestados.

Além disso, é necessário **implementar a automação** de algumas ações de registro de empréstimo em uma interface web usando **BotCity**.

## Funcionalidades do Sistema

### 1. Classe Autor

A classe `Autor` representa o autor de um ou mais livros e deve conter os seguintes atributos e métodos:

#### Atributos:
- `nome`: Nome do autor (privado).
- `livros`: Lista de livros escritos pelo autor (privado).

#### Métodos:
- `adicionar_livro(self, livro)`: Adiciona um livro à lista de livros do autor.
- `mostrar_livros(self)`: Exibe a lista de livros do autor.
- **Getters e Setters**: Para acessar e modificar os atributos `nome` e `livros`.

### 2. Classe Livro

A classe `Livro` representa os livros da biblioteca e deve conter os seguintes atributos e métodos:

#### Atributos:
- `titulo`: Título do livro (privado).
- `autor`: Autor do livro, representado por uma instância da classe `Autor` (composição).
- `codigo`: Código do livro, utilizado para identificá-lo na biblioteca.
- `disponivel`: Indica se o livro está disponível para empréstimo (privado).

#### Métodos:
- `emprestar(self)`: Marca o livro como não disponível.
- `devolver(self)`: Marca o livro como disponível.
- **Getters e Setters**: Para acessar e modificar os atributos `titulo`, `codigo`, e `disponivel`.

### 3. Classe Biblioteca

A classe `Biblioteca` gerencia os livros e empréstimos. Seus principais atributos e métodos são:

#### Atributos:
- `nome`: Nome da biblioteca.
- `livros`: Lista de livros disponíveis na biblioteca (privado).
- `emprestimos`: Dicionário que associa o código de um livro ao nome do cliente que fez o empréstimo (privado).
- `total_livros`: Variável de classe que armazena o número total de livros na biblioteca.

#### Métodos:
- `adicionar_livro(self, livro)`: Adiciona um livro à lista de livros e incrementa o `total_livros`.
- `registrar_emprestimo(self, codigo_livro, cliente)`: Registra um empréstimo, marcando o livro como indisponível e adicionando ao dicionário `emprestimos`.
- `registrar_devolucao(self, codigo_livro)`: Registra a devolução de um livro, marcando-o como disponível e removendo-o do dicionário `emprestimos`.
- `mostrar_livros_disponiveis(self)`: Lista todos os livros disponíveis para empréstimo.
- `mostrar_total_livros(cls)`: Método de classe que exibe o número total de livros na biblioteca.

### 4. Automação com BotCity

A automação com **BotCity** simula o processo de um funcionário registrando um empréstimo via interface web.

#### Ações da Automação:
- Preencher o campo "Código do Livro" no formulário de empréstimo.
- Preencher o campo "Nome do Cliente".
- Submeter o formulário para registrar o empréstimo.

## Instruções para Implementação

### Passos a serem seguidos:

1. **Implementar as classes** `Autor`, `Livro` e `Biblioteca` com os métodos e encapsulamento corretos.
2. **Criar instâncias** dessas classes para testar o funcionamento do sistema, adicionando autores, livros e gerenciando empréstimos.
3. **Automatizar o registro de empréstimos** com o **BotCity**, simulando o preenchimento e submissão de um formulário online.
4. **Entender os conceitos de herança e composição**: Use a composição ao relacionar a classe `Autor` dentro da classe `Livro`. Explore esses conceitos no sistema implementado.

---

Esse sistema vai auxiliar no gerenciamento eficaz de uma biblioteca fictícia, integrando o uso de conceitos de **orientação a objetos** e automação com **BotCity**.
