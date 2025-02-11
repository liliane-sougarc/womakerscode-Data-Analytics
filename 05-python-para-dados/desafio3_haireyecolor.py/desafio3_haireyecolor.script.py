import pandas as pd
from pydataset import data

# Carregar o dataset
df = data("HairEyeColor")

# Ajustar os dados: agrupar por Hair e Eye e somar os valores
df = df.groupby(['Hair', 'Eye'])['Freq'].sum().reset_index()
df.rename(columns={'Freq': 'Count'}, inplace=True)

# Exibir a tabela de contagem por combinação de cabelo e olhos
print("Número total de pessoas por combinação de cabelo e olhos:")
print(df)

# Encontrar a cor de cabelo mais comum entre pessoas com olhos castanhos
brown_eyes = df[df['Eye'] == 'Brown']
most_common_hair = brown_eyes.loc[brown_eyes['Count'].idxmax(), 'Hair']
print(f"\nCor de cabelo mais comum entre pessoas com olhos castanhos: {most_common_hair}")

# Criar uma tabela com a contagem total de cada cor de cabelo
hair_totals = df.groupby('Hair')['Count'].sum().reset_index()
print("\nTabela de contagem total por cor de cabelo:")
print(hair_totals)

# Salvar os resultados em um arquivo CSV
df.to_csv("resultado_hair_eye.csv", index=False)
