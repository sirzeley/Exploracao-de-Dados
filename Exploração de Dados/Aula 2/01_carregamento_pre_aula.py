"""Carregamento de dados para a Aula 2 de Exploração de Dados."""

import pandas as pd


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


def converter_valores(valor: str) -> float:
    valor = str(valor).upper().replace('€', '').replace('$', '').replace('£', '')
    if 'K' in valor:
        return float(valor.replace('K', '')) * 1_000
    if 'M' in valor:
        return float(valor.replace('M', '')) * 1_000_000
    return float(valor)


def carregar_fifa():
    url = 'https://www.harve.com.br/praticas/fifaplayers_pt.csv'
    dffifa = pd.read_csv(url)
    dffifa['remuneracao_corrigida'] = dffifa['remuneração'].apply(converter_valores)
    return dffifa


if __name__ == '__main__':
    print('--- DataFrame de exemplo ---')
    df = criar_dataframe_exemplo()
    print(df.head())

    print('\n--- FIFA players ---')
    dffifa = carregar_fifa()
    print(dffifa.head())
