"""Gráfico de barras das posições dos jogadores de FIFA."""

import pandas as pd
import matplotlib.pyplot as plt


URL = 'https://www.harve.com.br/praticas/fifaplayers_pt.csv'


def carregar_fifa():
    return pd.read_csv(URL)


def plotar_posicoes(dffifa: pd.DataFrame):
    contagem = dffifa['posição'].value_counts().sort_values()
    contagem.plot.bar()
    plt.title('Frequência de posições dos jogadores')
    plt.xlabel('Posição')
    plt.ylabel('Contagem')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    dffifa = carregar_fifa()
    plotar_posicoes(dffifa)
