import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('banco_alunos.db')

# Criar um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Apagar a tabela "alunos" se ela já existir
cursor.execute('DROP TABLE IF EXISTS alunos')

# Criar a tabela "alunos" novamente
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    curso TEXT NOT NULL
)
''')

# Inserir registros na tabela "alunos"
cursor.executemany('''
INSERT INTO alunos (id, nome, idade, curso) 
VALUES (?, ?, ?, ?)
''', [
    (1, 'João Silva', 22, 'Engenharia'),
    (2, 'Maria Souza', 19, 'Medicina'),
    (3, 'Carlos Pereira', 21, 'Engenharia'),
    (4, 'Ana Oliveira', 25, 'Direito'),
    (5, 'Lucas Fernandes', 18, 'Arquitetura')
])

# Atualizar a idade de um aluno específico
cursor.execute('''
UPDATE alunos
SET idade = 23
WHERE id = 1
''')

# Remover um aluno pelo seu ID
cursor.execute('''
DELETE FROM alunos
WHERE id = 5
''')

# Commit para salvar as mudanças
conexao.commit()

# Fechar a conexão
conexao.close()
