"""Gráficos de dispersão e análises de correlação para os datasets de família e FIFA."""

import pandas as pd
import seaborn as sns
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


def carregar_fifa():
    url = 'https://www.harve.com.br/praticas/fifaplayers_pt.csv'
    dffifa = pd.read_csv(url)
    dffifa['remuneracao_corrigida'] = dffifa['remuneração'].apply(converter_valores)
    return dffifa


def converter_valores(valor: str) -> float:
    valor = str(valor).upper().replace('€', '').replace('$', '').replace('£', '')
    if 'K' in valor:
        return float(valor.replace('K', '')) * 1_000
    if 'M' in valor:
        return float(valor.replace('M', '')) * 1_000_000
    return float(valor)


def plot_scatter_fifa(dffifa: pd.DataFrame):
    dffifa.plot.scatter(y='remuneracao_corrigida', x='pontuação geral')


def plot_scatter_familia(df: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='tamanho_familia', y='renda_familiar', hue='num_automoveis')
    plt.title('Dispersão: renda familiar x número de automóveis')
    plt.xlabel('Tamanho da família')
    plt.ylabel('Renda familiar (R$)')
    plt.tight_layout()
    plt.show()


def plot_sns_fifa(dffifa: pd.DataFrame):
    plt.figure(figsize=(15, 8))
    sns.scatterplot(data=dffifa, x='pontuação geral', y='remuneracao_corrigida', hue='posição')
    plt.title('Dispersão: pontuação geral x remuneração corrigida')
    plt.tight_layout()
    plt.show()


def plot_heatmap_fifa(dffifa: pd.DataFrame):
    df_pivot = dffifa.pivot_table(
        index='pontuação geral',
        columns='posição',
        values='remuneracao_corrigida'
    )
    sns.heatmap(df_pivot, cmap='viridis')


def pairplot_fifa(dffifa: pd.DataFrame):
    sns.pairplot(dffifa)


def pairplot_familia(df: pd.DataFrame):
    sns.pairplot(df)


def correlacao_fifa(dffifa: pd.DataFrame) -> pd.DataFrame:
    return dffifa.corr(numeric_only=True, method='spearman')


def correlacao_familia(df: pd.DataFrame) -> pd.DataFrame:
    return df.corr(numeric_only=True)


if __name__ == '__main__':
    print('--- Dispersão FIFA ---')
    dffifa = carregar_fifa()
    plot_scatter_fifa(dffifa)
    plot_sns_fifa(dffifa)
    plot_heatmap_fifa(dffifa)
    print('\n--- Correlação FIFA ---')
    print(correlacao_fifa(dffifa))

    print('\n--- Dispersão Família ---')
    df = criar_dataframe_exemplo()
    plot_scatter_familia(df)
    print('\n--- Correlação Família ---')
    print(correlacao_familia(df))
