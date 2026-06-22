"""Tabela de contingência entre tamanho da casa e tipo de casa."""

import pandas as pd
import matplotlib.pyplot as plt


def criar_dataframe_exemplo():
    dados = {
        'id_familia': [1, 2, 3, 4, 5, 6, 7, 8],
        'tipo_casa': [
            'apartamento', 'casa', 'casa', 'kitnet',
            'sobrado', 'apartamento', 'apartamento', 'casa'
        ],
        'tamanho_casa': [
            'pequeno', 'médio', 'grande', 'pequeno',
            'médio', 'grande', 'grande', 'pequeno'
        ],
        'n_cartoes': [4, 6, 6, 7, 8, 7, 8, 10],
        'tamanho_familia': [2, 2, 4, 4, 5, 5, 6, 6],
        'renda_familiar': [14, 16, 14, 17, 18, 21, 17, 25],
        'num_automoveis': [1, 2, 2, 1, 3, 2, 1, 3],
        'distanciacentro': [22.2, 3, 31, 2, 1, 12, 2, 4],
    }
    return pd.DataFrame(dados)


def tabela_contingencia_casas(df: pd.DataFrame) -> pd.DataFrame:
    return pd.crosstab(df['tamanho_casa'], df['tipo_casa'])


def plotar_contingencia_casas(df: pd.DataFrame):
    tabela = tabela_contingencia_casas(df)
    tabela.plot.bar()
    plt.title('Contingência: tamanho da casa x tipo de casa')
    plt.xlabel('Tamanho da casa')
    plt.ylabel('Contagem')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    df = criar_dataframe_exemplo()
    print('Tabela de contingência (tamanho da casa x tipo de casa):')
    print(tabela_contingencia_casas(df))
    plotar_contingencia_casas(df)
