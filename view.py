import sqlite3

# Função para conectar ao banco de dados
def connect():
    conn = sqlite3.connect('biblioteca.db')
    return conn

# Função para inserir um novo livro na tabela "livros"
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)", (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

# Função para inserir um novo usuário na tabela "usuarios"
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios (nome, sobrenome, endereco, email, telefone) VALUES (?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Função para inserir um novo empréstimo na tabela "emprestimos"
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

# Função para recuperar todos os livros emprestados no momento
def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM livros \
                           INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

# Função para atualizar a data de devolução de um empréstimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()

# Exemplo de uso das funções
insert_book("Dom Quixote", "Miguel de Cervantes", "Editora Saraiva", 1605, "9788578270692")
insert_user("João", "Silva", "Rua A, 123", "joao.silva@email.com", "(11) 1234-5678")
insert_loan(1, 1, "2022-03-25", None)
books_on_loan = get_books_on_loan()
print(books_on_loan)
update_loan_return_date(1, "2022-03-28")