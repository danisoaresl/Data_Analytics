import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('banco_clientes.db')

# Criar um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Criar a tabela "clientes" (se ainda não foi criada)
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    saldo FLOAT NOT NULL
)
''')

# Criar a tabela "compras"
cursor.execute('''
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    produto TEXT NOT NULL,
    valor REAL NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
''')

# Inserir algumas compras associadas a clientes existentes na tabela "clientes"
cursor.executemany('''
INSERT INTO compras (id, cliente_id, produto, valor)
VALUES (?, ?, ?, ?)
''', [
    (1, 1, 'Notebook', 1500.00),
    (2, 2, 'Smartphone', 800.00),
    (3, 1, 'Tablet', 600.00),
    (4, 4, 'Monitor', 300.00),
    (5, 5, 'Teclado', 150.00)
])

# Commit para salvar as mudanças
conexao.commit()

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
cursor.execute('''
SELECT clientes.nome, compras.produto, compras.valor
FROM compras
JOIN clientes ON compras.cliente_id = clientes.id
''')

# Mostrar os resultados
compras = cursor.fetchall()
for compra in compras:
    print(compra)

# Fechar a conexão
conexao.close()


