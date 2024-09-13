import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('banco_clientes.db')

# Criar um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Apagar a tabela "clientes" se ela já existir
cursor.execute('DROP TABLE IF EXISTS clientes')

# Criar a tabela "clientes" novamente
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    saldo FLOAT NOT NULL
)
''')

# Inserir alguns registros na tabela "clientes"
cursor.executemany('''
INSERT INTO clientes (id, nome, idade, saldo) 
VALUES (?, ?, ?, ?)
''', [
    (1, 'João da Silva', 45, 2500.75),
    (2, 'Maria Oliveira', 32, 1500.00),
    (3, 'Carlos Souza', 28, 800.50),
    (4, 'Ana Lima', 40, 3000.00),
    (5, 'Lucas Martins', 35, 950.00)
])

# Commit para salvar as mudanças
conexao.commit()

# Selecionar o nome e a idade dos clientes com idade superior a 30 anos
cursor.execute('''
SELECT nome, idade FROM clientes
WHERE idade > 30
''')
print("Clientes com idade superior a 30 anos:", cursor.fetchall())

# Calcular o saldo médio dos clientes
cursor.execute('''
SELECT AVG(saldo) AS saldo_medio FROM clientes
''')
print("Saldo médio dos clientes:", cursor.fetchone()[0])

# Encontrar o cliente com o saldo máximo
cursor.execute('''
SELECT nome, saldo FROM clientes
ORDER BY saldo DESC
LIMIT 1
''')
print("Cliente com o saldo máximo:", cursor.fetchone())

# Contar quantos clientes têm saldo acima de 1000
cursor.execute('''
SELECT COUNT(*) AS clientes_acima_1000 FROM clientes
WHERE saldo > 1000
''')
print("Número de clientes com saldo acima de 1000:", cursor.fetchone()[0])

# Atualize o saldo de um cliente específico
cursor.execute('''
UPDATE clientes
SET saldo = 3000.00
WHERE id = 1
''')

# Remova um cliente pelo seu ID
cursor.execute('''
DELETE FROM clientes
WHERE id = 3
''')

# Commit para salvar as mudanças
conexao.commit()

# Fechar a conexão
conexao.close()
