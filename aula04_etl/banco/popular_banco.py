# =============================================================================
# POPULAR O BANCO — rode este script UMA VEZ antes da aula
# =============================================================================
# Cria e popula as 4 tabelas usadas pelos alunos:
#
#   previsao_tempo  → forecast de SP via HG Brasil Weather API
#   cotacoes        → cotações de moedas via HG Brasil Finance API
#   fifaplayers     → jogadores FIFA via CSV da Harve
#   pais            → países da América do Sul (criada aqui)
#
# Dependências: pip install requests pandas sqlalchemy pymysql
# =============================================================================

import requests
import pandas as pd
from sqlalchemy import create_engine

# ⚠️  Preencha com as credenciais reais do banco
STRING_DE_CONEXAO = "mysql+pymysql://USUARIO:SENHA@HOST:3306/BANCO"

conn = create_engine(STRING_DE_CONEXAO).connect()
print("✅ Conectado ao banco.\n")


# ─────────────────────────────────────────────────────────────────────────────
# 1. previsao_tempo — HG Brasil Weather
# ─────────────────────────────────────────────────────────────────────────────
print("⏳ Carregando previsao_tempo...")
URL_WEATHER = "https://api.hgbrasil.com/weather?format=json&city_name=São Paulo,SP"
# Com chave: "&key=SUA_CHAVE"

resp = requests.get(URL_WEATHER)
dados_tempo = resp.json()["results"]

registros_tempo = []
for dia in dados_tempo["forecast"]:
    registros_tempo.append({
        "data":                dia["full_date"],
        "cidade":              dados_tempo["city_name"],
        "temp_min":            dia["min"],
        "temp_max":            dia["max"],
        "umidade":             dia["humidity"],
        "probabilidade_chuva": dia["rain_probability"],
        "chuva_mm":            dia["rain"],
        "condicao":            dia["description"],
        "vento":               dia["wind_speedy"],
    })

df_tempo = pd.DataFrame(registros_tempo)
df_tempo.to_sql("previsao_tempo", con=conn, if_exists="replace", index=False)
conn.commit()
print(f"✅ previsao_tempo — {len(df_tempo)} linhas")
print(df_tempo[["data","temp_min","temp_max","probabilidade_chuva","condicao"]].to_string(index=False))
print()


# ─────────────────────────────────────────────────────────────────────────────
# 2. cotacoes — HG Brasil Finance
# ─────────────────────────────────────────────────────────────────────────────
print("⏳ Carregando cotacoes...")
URL_FINANCE = "https://api.hgbrasil.com/finance?format=json"

resp = requests.get(URL_FINANCE)
moedas_raw = resp.json()["results"]["currencies"]

registros_cotacoes = []
for codigo, info in moedas_raw.items():
    if codigo == "source":
        continue
    registros_cotacoes.append({
        "moeda":    codigo,
        "nome":     info.get("name"),
        "compra":   info.get("buy"),
        "venda":    info.get("sell"),
        "variacao": info.get("variation"),
    })

df_cotacoes = pd.DataFrame(registros_cotacoes)
df_cotacoes.to_sql("cotacoes", con=conn, if_exists="replace", index=False)
conn.commit()
print(f"✅ cotacoes — {len(df_cotacoes)} linhas")
print(df_cotacoes.to_string(index=False))
print()


# ─────────────────────────────────────────────────────────────────────────────
# 3. fifaplayers — CSV da Harve
# ─────────────────────────────────────────────────────────────────────────────
print("⏳ Carregando fifaplayers...")
URL_FIFA = "https://www.harve.com.br/praticas/fifaplayers_pt.csv"
df_fifa = pd.read_csv(URL_FIFA)
df_fifa.to_sql("fifaplayers", con=conn, if_exists="replace", index=False)
conn.commit()
print(f"✅ fifaplayers — {len(df_fifa)} linhas | colunas: {list(df_fifa.columns)}\n")


# ─────────────────────────────────────────────────────────────────────────────
# 4. pais — criada localmente
# ─────────────────────────────────────────────────────────────────────────────
print("⏳ Criando tabela pais...")
df_paises = pd.DataFrame({
    "id":         [1, 2, 3, 4, 5, 6, 7, 8],
    "nome":       ["Brasil","Argentina","Chile","Colômbia",
                   "Peru","Uruguai","Paraguai","Bolívia"],
    "continente": ["América do Sul"] * 8,
    "populacao":  [215_000_000, 45_000_000, 19_000_000, 51_000_000,
                   33_000_000, 3_500_000, 7_400_000, 12_000_000],
    "capital":    ["Brasília","Buenos Aires","Santiago","Bogotá",
                   "Lima","Montevidéu","Assunção","Sucre"],
})
df_paises.to_sql("pais", con=conn, if_exists="replace", index=False)
conn.commit()
print(f"✅ pais — {len(df_paises)} linhas")
print(df_paises.to_string(index=False))
print()

conn.close()
print("=" * 50)
print("✅  BANCO POPULADO COM SUCESSO!")
print("   Tabelas disponíveis para os alunos:")
print("   → previsao_tempo")
print("   → cotacoes")
print("   → fifaplayers")
print("   → pais")
print("=" * 50)
