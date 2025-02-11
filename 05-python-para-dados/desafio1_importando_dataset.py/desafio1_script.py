# Importando a biblioteca necessária
try:
    from pydataset import data
    import pandas as pd
except ImportError:
    print("A biblioteca 'pydataset' não está instalada. Instale com 'pip install pydataset'.")

# Carregando o dataset 'iris'
df = data("iris")

# Verifica se o dataset foi carregado corretamente
if df is None:
    print("Erro ao carregar o dataset 'iris'. Verifique se a biblioteca pydataset está funcionando corretamente.")
else:
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
