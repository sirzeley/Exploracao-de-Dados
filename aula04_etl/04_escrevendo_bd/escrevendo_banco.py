# ============================================================
#  AULA 4 — BLOCO 4: Escrevendo Dados em um Banco de Dados
# ============================================================
#
#  O QUE VAMOS APRENDER:
#  ✅ Pipeline ETL completo: API → DataFrame → Banco
#  ✅ O método .to_sql() — escrever DataFrame no banco
#  ✅ O parâmetro if_exists (fail / replace / append)
#  ✅ commit() e close() — confirmar e fechar
#
#  Dependências: pip install pandas sqlalchemy requests
# ============================================================

import pandas as pd
import requests
from sqlalchemy import create_engine, text
from datetime import datetime

print("=" * 50)
print("  BLOCO 4 — ESCREVENDO NO BANCO")
print("=" * 50)
print()

STRING_DE_CONEXAO = "sqlite:///harve_escola.db"


# ────────────────────────────────────────────────────────────
#  O CONCEITO — ETL em uma linha
# ────────────────────────────────────────────────────────────
#
#  ETL = Extract → Transform → Load
#
#  EXTRACT   → buscar dados de uma fonte (API, CSV, outro banco)
#  TRANSFORM → limpar, filtrar, formatar com pandas
#  LOAD      → salvar no banco de destino com .to_sql()
#
#  Bloco 1 foi Extract + Export para CSV
#  Este bloco é Extract + Load para banco de dados

print("  ETL = Extract → Transform → Load")
print()
print("  EXTRACT   → API HG Brasil (cotações ao vivo)")
print("  TRANSFORM → montar DataFrame limpo")
print("  LOAD      → salvar no banco SQLite")
print()


# ────────────────────────────────────────────────────────────
#  EXTRACT — Buscando dados da API HG Brasil
# ────────────────────────────────────────────────────────────

print("  ─" * 25)
print("  EXTRACT — buscando da API")
print("  ─" * 25)
print()

URL = "https://api.hgbrasil.com/finance?format=json"
print(f"  📡 Requisição para: {URL}")

try:
    resposta = requests.get(URL, timeout=5)
    dados    = resposta.json()
    moedas_raw = dados["results"]["currencies"]

    registros = []
    for codigo, info in moedas_raw.items():
        if codigo == "source":
            continue
        registros.append({
            "moeda":      codigo,
            "nome":       info.get("name"),
            "compra":     info.get("buy"),
            "venda":      info.get("sell"),
            "variacao":   info.get("variation"),
            "atualizado": datetime.now().strftime("%Y-%m-%d %H:%M"),
        })
    print("  ✅ Dados recebidos da API!")

except Exception:
    # Fallback com dados estáticos caso a API esteja indisponível
    print("  ⚠️  API indisponível. Usando dados de exemplo.")
    registros = [
        {"moeda": "USD", "nome": "Dólar Americano",  "compra": 5.10, "venda": 5.12, "variacao":  0.5, "atualizado": datetime.now().strftime("%Y-%m-%d %H:%M")},
        {"moeda": "EUR", "nome": "Euro",              "compra": 5.50, "venda": 5.53, "variacao": -0.3, "atualizado": datetime.now().strftime("%Y-%m-%d %H:%M")},
        {"moeda": "GBP", "nome": "Libra Esterlina",   "compra": 6.40, "venda": 6.43, "variacao":  0.1, "atualizado": datetime.now().strftime("%Y-%m-%d %H:%M")},
        {"moeda": "BTC", "nome": "Bitcoin",           "compra": 350000, "venda": 351000, "variacao": 2.1, "atualizado": datetime.now().strftime("%Y-%m-%d %H:%M")},
    ]

df_cotacoes = pd.DataFrame(registros)

print(f"  ✅ {len(df_cotacoes)} moedas extraídas")
print()
print("  DataFrame:")
print(df_cotacoes.to_string(index=False))
print()


# ────────────────────────────────────────────────────────────
#  LOAD — Enviando para o banco com .to_sql()
# ────────────────────────────────────────────────────────────
#
#  .to_sql() é o oposto do .read_sql():
#
#  read_sql()  → banco ──► DataFrame   (leitura)
#  to_sql()    → DataFrame ──► banco   (escrita)
#
#  Parâmetros do .to_sql():
#
#  name      → nome da tabela que será criada/atualizada
#  con       → a conexão aberta
#  if_exists → o que fazer se a tabela já existir:
#
#    "fail"    → gera erro se a tabela existir     (proteção)
#    "replace" → apaga tudo e recria               (carga full)
#    "append"  → adiciona linhas sem deletar       (incremental)
#
#  index     → False = não salva a coluna de índice

print("  ─" * 25)
print("  LOAD — enviando para o banco")
print("  ─" * 25)
print()

engine = create_engine(STRING_DE_CONEXAO)
conn   = engine.connect()

df_cotacoes.to_sql(
    name      = "cotacoes",
    con       = conn,
    if_exists = "replace",
    index     = False,
)

print("  ✅ DataFrame enviado para o banco!")
print("  📋 Tabela criada: 'cotacoes'")
print()


# ────────────────────────────────────────────────────────────
#  COMMIT e CLOSE — confirmar e fechar
# ────────────────────────────────────────────────────────────
#
#  COMMIT = "confirme as mudanças de verdade"
#
#  Operações de escrita ficam em estado de "rascunho"
#  até o commit ser executado. É como o Ctrl+S do banco.
#
#  Sem commit → dados NÃO são salvos permanentemente
#  Sem close  → conexão fica aberta consumindo recursos

conn.commit()
conn.close()

print("  💾 commit() — mudanças confirmadas no banco")
print("  🔒 close()  — conexão encerrada")
print()


# ────────────────────────────────────────────────────────────
#  VERIFICAÇÃO — Lendo de volta para confirmar
# ────────────────────────────────────────────────────────────

print("  ─" * 25)
print("  VERIFICAÇÃO — lendo do banco para confirmar")
print("  ─" * 25)
print()

conn     = engine.connect()
df_check = pd.read_sql(text("SELECT * FROM cotacoes"), conn)
conn.close()

print(f"  ✅ {len(df_check)} registros encontrados na tabela 'cotacoes'")
print()
print(df_check.to_string(index=False))
print()


# ────────────────────────────────────────────────────────────
#  QUANDO USAR CADA if_exists?
# ────────────────────────────────────────────────────────────

print("  ─" * 25)
print("  QUANDO USAR CADA if_exists?")
print("  ─" * 25)
print()
print("  'fail'    → primeira carga, tabela não deve existir ainda")
print("             gera erro se tentar rodar duas vezes")
print()
print("  'replace' → recarrega dados do zero a cada execução")
print("             ⚠️  apaga tudo que estava antes!")
print()
print("  'append'  → adiciona novos registros sem apagar")
print("             ideal para logs e histórico")
print()


# ────────────────────────────────────────────────────────────
#  EXERCÍCIO — Tente você mesmo
# ────────────────────────────────────────────────────────────
#
#  1. Leia o arquivo "../dados/stock_petr4.csv" em um DataFrame
#  2. Conecte ao banco harve_escola.db
#  3. Envie o DataFrame para o banco com nome "acoes_petr4"
#     Use if_exists="replace" e index=False
#  4. Faça commit e feche a conexão
#  5. Reconecte e leia a tabela de volta para confirmar
#
# ── Escreva seu código abaixo ────────────────────────────────


# ── Solução (não olhe antes de tentar!) ─────────────────────
# df_petr = pd.read_csv("../dados/stock_petr4.csv")
# conn = engine.connect()
# df_petr.to_sql("acoes_petr4", conn, if_exists="replace", index=False)
# conn.commit()
# conn.close()
# print("✅ Tabela acoes_petr4 criada!")
#
# conn = engine.connect()
# df_v = pd.read_sql(text("SELECT * FROM acoes_petr4 LIMIT 5"), conn)
# print(df_v)
# conn.close()

print("=" * 50)
print("  FIM DO BLOCO 4")
print("  Próximo: 05_desafio/desafio_final.py")
print("=" * 50)
