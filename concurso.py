import pandas as pd

# Carregando o arquivo CSV
df = pd.read_csv('concurso.csv')

pessoas_piaui = df[df['Estado'] == 'Piauí'].shape[0]
print(f"Quantidade de pessoas do estado do Piauí: {pessoas_piaui}")

pessoas_es_feminino = df[(df['Estado'] == 'ES') & (df['Sexo'] == 'F')].shape[0]
print(f"Quantidade de pessoas do ES do sexo feminino: {pessoas_es_feminino}")

pessoas_antes_1995 = df[df['Ano_Nascimento'] < 1995].shape[0]
print(f"Quantidade de pessoas que nasceram antes de 1995: {pessoas_antes_1995}")

dados_inscritos = df[['nºinscrição', 'nome', 'idade']]
print(dados_inscritos)

# Substituir valores faltosos em colunas de string
df.fillna('Falta informação', inplace=True)

# Substituir valores faltosos em colunas numéricas com a mediana
for column in df.select_dtypes(include=['float64', 'int64']):
    mediana = df[column].median()
    df[column].fillna(mediana, inplace=True)

import matplotlib.pyplot as plt

# Calcular a porcentagem de dados faltosos
porcentagem_faltosos = df.isnull().mean() * 100

# Plotar a porcentagem de dados faltosos
porcentagem_faltosos.plot(kind='bar')
plt.title('Porcentagem de Dados Faltosos por Coluna')
plt.xlabel('Colunas')
plt.ylabel('Porcentagem de Dados Faltosos')
plt.show()

