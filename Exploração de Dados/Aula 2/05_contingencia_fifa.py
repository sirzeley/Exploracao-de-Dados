"""Tabela de contingência entre posição e perna de preferência no dataset FIFA."""

import pandas as pd


URL = 'https://www.harve.com.br/praticas/fifaplayers_pt.csv'


def carregar_fifa():
    return pd.read_csv(URL)


def tabela_contingencia_fifa(dffifa: pd.DataFrame) -> pd.DataFrame:
    return pd.crosstab(dffifa['perna de preferência'], dffifa['posição'])


def plotar_contingencia_fifa(dffifa: pd.DataFrame):
    tabela = tabela_contingencia_fifa(dffifa)
    tabela.T.plot.bar()


if __name__ == '__main__':
    dffifa = carregar_fifa()
    print('Tabela de contingência (perna de preferência x posição):')
    print(tabela_contingencia_fifa(dffifa))
    plotar_contingencia_fifa(dffifa)
