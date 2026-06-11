# ============================================================
#  AULA 4 — BLOCO 1: Exportando Dados para CSV
# ============================================================
#
#  O QUE VAMOS APRENDER:
#  ✅ O que é um arquivo CSV
#  ✅ Como exportar um DataFrame para CSV
#  ✅ O que é o índice e como removê-lo
#  ✅ Como usar datas no nome do arquivo
#
#  Dependências: pip install pandas requests
# ============================================================

import pandas as pd
import requests
from datetime import datetime

print("=" * 50)
print("  BLOCO 1 — EXPORTANDO PARA CSV")
print("=" * 50)
print()


# ────────────────────────────────────────────────────────────
#  PASSO 1 — O que é CSV?
# ────────────────────────────────────────────────────────────
#
#  CSV = Comma-Separated Values (Valores Separados por Vírgula)
#
#  É um arquivo de texto simples onde:
#  - Cada linha = uma linha de dados
#  - Cada valor é separado por vírgula
#
#  Exemplo de como fica o arquivo:
#  nome,preco,variacao
#  USD,5.10,0.5
#  EUR,5.50,-0.3
#  BTC,350000,2.1
#
#  Qualquer Excel, Google Sheets ou Python consegue abrir.
#  É o formato mais portável do mundo de dados.


# ────────────────────────────────────────────────────────────
#  PASSO 2 — Buscando dados reais da API HG Brasil
# ────────────────────────────────────────────────────────────
#
#  Vamos pegar cotações ao vivo de moedas.
#  requests.get() faz uma requisição HTTP para a API
#  .json() converte a resposta para dicionário Python

print("  📡 Buscando cotações da API HG Brasil...")

URL = "https://api.hgbrasil.com/finance?format=json"
resposta = requests.get(URL)
dados    = resposta.json()

# Navegando no JSON para chegar nas moedas
moedas_raw = dados["results"]["currencies"]

# Transformando em lista de dicionários para virar DataFrame
registros = []
for codigo, info in moedas_raw.items():
    if codigo == "source":          # campo que não é moeda
        continue
    registros.append({
        "moeda":    codigo,
        "nome":     info.get("name"),
        "compra":   info.get("buy"),
        "venda":    info.get("sell"),
        "variacao": info.get("variation"),
    })

df = pd.DataFrame(registros)

print("  ✅ Dados recebidos!")
print()
print("  DataFrame:")
print(df.to_string(index=True))
print()


# ────────────────────────────────────────────────────────────
#  PASSO 3 — Exportação básica com to_csv()
# ────────────────────────────────────────────────────────────
#
#  df.to_csv("nome_arquivo.csv")
#  → salva o DataFrame como arquivo de texto no disco
#
#  ⚠️  PROBLEMA: por padrão, o pandas inclui o ÍNDICE
#     O índice é a numeração automática das linhas (0, 1, 2...)
#     Na maioria dos casos, não faz sentido ter isso no arquivo

df.to_csv("cotacoes_COM_indice.csv")

print("  📄 Arquivo gerado: cotacoes_COM_indice.csv")
print("  ⚠️  Abra o arquivo — tem uma coluna extra no início!")
print("     Essa coluna é o ÍNDICE do DataFrame (0, 1, 2...)")
print()


# ────────────────────────────────────────────────────────────
#  PASSO 4 — Removendo o índice com index=False
# ────────────────────────────────────────────────────────────
#
#  index=False → "não inclua a coluna de índice no arquivo"
#
#  Antes (com índice):        Depois (sem índice):
#  ,moeda,nome,compra         moeda,nome,compra
#  0,USD,Dólar,5.10           USD,Dólar,5.10
#  1,EUR,Euro,5.50            EUR,Euro,5.50

df.to_csv("cotacoes_SEM_indice.csv", index=False)

print("  📄 Arquivo gerado: cotacoes_SEM_indice.csv")
print("  ✅ Agora sem a coluna de índice — arquivo limpo!")
print()


# ────────────────────────────────────────────────────────────
#  PASSO 5 — Data no nome do arquivo (boa prática ETL)
# ────────────────────────────────────────────────────────────
#
#  Em pipelines de dados, salvamos com data no nome.
#  Por quê? Imagina extrair cotações todo dia:
#
#  cotacoes.csv        → amanhã sobrescreve hoje ❌
#  cotacoes_2024-01-15.csv → histórico preservado ✅
#
#  strftime() converte datetime para texto formatado:
#  %Y = ano  (2024)
#  %m = mês  (01)
#  %d = dia  (15)
#  %H = hora (09)
#  %M = minuto (30)

agora        = datetime.now().strftime("%Y-%m-%d_%H%M")
nome_arquivo = f"cotacoes_{agora}.csv"

df.to_csv(nome_arquivo, index=False)

print(f"  📄 Arquivo gerado: {nome_arquivo}")
print("  ✅ Com data e hora no nome — rastreável!")
print()


# ────────────────────────────────────────────────────────────
#  EXERCÍCIO — Tente você mesmo
# ────────────────────────────────────────────────────────────
#
#  A API HG Brasil também retorna dados de Bitcoin.
#  Acesse: dados["results"]["bitcoin"]
#
#  1. Extraia os dados de Bitcoin em um DataFrame com colunas:
#     corretora, ultimo_valor, variacao
#  2. Exporte para CSV com data e hora no nome
#  3. Sem índice
#
# ── Escreva seu código abaixo ────────────────────────────────


# ── Solução (não olhe antes de tentar!) ─────────────────────
# bitcoin_raw = dados["results"]["bitcoin"]
# registros_btc = []
# for corretora, info in bitcoin_raw.items():
#     registros_btc.append({
#         "corretora":    info.get("name"),
#         "ultimo_valor": info.get("last"),
#         "variacao":     info.get("variation"),
#     })
# df_btc = pd.DataFrame(registros_btc)
# agora = datetime.now().strftime("%Y-%m-%d_%H%M")
# df_btc.to_csv(f"bitcoin_{agora}.csv", index=False)
# print(df_btc)

print("=" * 50)
print("  FIM DO BLOCO 1")
print("  Próximo: 02_credenciais_bd/credenciais.py")
print("=" * 50)
