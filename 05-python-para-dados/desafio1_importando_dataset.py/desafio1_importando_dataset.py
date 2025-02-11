# Importando a biblioteca necessária
from pydataset import data

# Carregando o dataset 'iris'
df = data("iris")

# Exibindo as primeiras 5 linhas do dataset
print("As primeiras 5 linhas do dataset:")
print(df.head())

# Exibindo o tipo de dado do dataset
print("\nTipo do dataset:", type(df))

# Exibindo o número de linhas e colunas
print("\nNúmero de linhas e colunas:", df.shape)

# Criando uma função que retorna o número de linhas e colunas
def tamanho_dataset(dataframe):
    linhas, colunas = dataframe.shape
    return f"O dataset tem {linhas} linhas e {colunas} colunas."

# Chamando a função e imprimindo o resultado
print("\n", tamanho_dataset(df))
