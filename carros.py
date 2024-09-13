import pandas as pd

# Carregando o CSV
df = pd.read_csv('caminho/para/o/arquivo/carros.csv')

# Exibindo as primeiras 10 linhas
print(df.head(10))

print("Colunas do DataFrame:", df.columns)
print("Índice do DataFrame:", df.index)

# Supondo que a coluna que contém a quantidade de carros seja 'Quantidade de Carros'
df_sorted = df.sort_values(by='Quantidade de Carros', ascending=True)
print(df_sorted)

# Supondo que as colunas sejam 'População' e 'Quantidade de Carros'
df['Proporção Carros/Habitante'] = df['Quantidade de Carros'] / df['População']
print(df)

df_estado_proporcao = df[['Estado', 'Proporção Carros/Habitante']]
print(df_estado_proporcao)

# Supondo que as colunas sejam 'Região' e 'Idade'
media_idade_regiao = df.groupby('Região')['Idade'].mean()
print(media_idade_regiao)

# Supondo que a coluna 'Deficiencia' tenha valores binários, onde 1 = tem deficiência, 0 = não tem
porcentagem_deficiencia = df['Deficiencia'].mean() * 100
print(f"Porcentagem de pessoas com deficiência: {porcentagem_deficiencia:.2f}%")

# Supondo que a coluna 'Estado' tenha os nomes dos estados
pessoas_piaui = df[df['Estado'] == 'Piauí'].shape[0]
print(f"Quantidade de pessoas no estado do Piauí: {pessoas_piaui}")
