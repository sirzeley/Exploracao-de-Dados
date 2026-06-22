"""Exercícios de tabela de frequência para dados FIFA."""

import pandas as pd


URL = 'https://www.harve.com.br/praticas/fifaplayers_pt.csv'


def carregar_fifa():
    return pd.read_csv(URL)


def tabela_frequencia_posicao(dffifa: pd.DataFrame) -> pd.Series:
    return dffifa['posição'].value_counts()


def frequencia_relativa_posicao(dffifa: pd.DataFrame) -> pd.Series:
    return dffifa['posição'].value_counts() / dffifa.shape[0]


if __name__ == '__main__':
    dffifa = carregar_fifa()
    print('Frequência absoluta por posição:')
    print(tabela_frequencia_posicao(dffifa))

    print('\nFrequência relativa por posição:')
    print(frequencia_relativa_posicao(dffifa))
