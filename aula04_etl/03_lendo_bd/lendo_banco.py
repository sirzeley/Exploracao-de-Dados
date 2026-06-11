# ============================================================
#  AULA 4 — BLOCO 3: Lendo Dados de um Banco de Dados
# ============================================================
#
#  O QUE VAMOS APRENDER:
#  ✅ Como criar e popular tabelas com SQLite
#  ✅ A sequência completa de leitura (5 passos)
#  ✅ Como escrever queries SQL em Python
#  ✅ Filtros: WHERE, ORDER BY, GROUP BY, HAVING, BETWEEN
#
#  Dependências: pip install pandas sqlalchemy
# ============================================================

import pandas as pd
from sqlalchemy import create_engine, text

print("=" * 50)
print("  BLOCO 3 — LENDO DADOS DO BANCO")
print("=" * 50)
print()


# ────────────────────────────────────────────────────────────
#  PREPARAÇÃO — Criando o banco e populando com dados reais
# ────────────────────────────────────────────────────────────
#
#  SQLite cria um arquivo .db local — sem servidor, sem senha
#  É o mesmo conceito do MySQL, só mais simples para aprender

STRING_DE_CONEXAO = "sqlite:///harve_escola.db"

engine = create_engine(STRING_DE_CONEXAO)
conn   = engine.connect()

# Carregando dados reais de jogadores FIFA
# (o CSV vem do site da Harve)
print("  📥 Carregando dados FIFA para o banco...")

URL_FIFA = "https://www.harve.com.br/praticas/fifaplayers_pt.csv"
try:
    df_fifa = pd.read_csv(URL_FIFA)
    df_fifa.to_sql("fifanova", conn, if_exists="replace", index=False)
    conn.commit()
    print(f"  ✅ Tabela 'fifanova' criada — {len(df_fifa)} jogadores")
    print(f"  📋 Colunas: {list(df_fifa.columns[:6])}...")
except Exception as e:
    # Se a URL não estiver acessível, usa dados de exemplo
    print(f"  ⚠️  URL indisponível. Usando dados de exemplo.")
    conn.execute(text("DROP TABLE IF EXISTS fifanova"))
    conn.execute(text("""
        CREATE TABLE fifanova (
            Name TEXT, Nationality TEXT,
            Overall INTEGER, Potential INTEGER,
            Age INTEGER, Club TEXT
        )
    """))
    conn.execute(text("""
        INSERT INTO fifanova VALUES
        ('L. Messi',     'Argentina', 91, 91, 36, 'Inter Miami'),
        ('C. Ronaldo',   'Portugal',  88, 88, 38, 'Al-Nassr'),
        ('Neymar Jr',    'Brazil',    87, 87, 31, 'Al-Hilal'),
        ('K. Mbappé',    'France',    91, 95, 24, 'PSG'),
        ('V. Jr.',       'Brazil',    86, 92, 22, 'Real Madrid'),
        ('Pedri',        'Spain',     87, 93, 20, 'Barcelona'),
        ('J. Bellingham','England',   88, 94, 19, 'Real Madrid'),
        ('R. Leão',      'Portugal',  84, 89, 23, 'AC Milan'),
        ('Rodrygo',      'Brazil',    82, 88, 22, 'Real Madrid'),
        ('G. Ramos',     'Portugal',  80, 86, 21, 'PSG')
    """))
    conn.commit()
    print("  ✅ Tabela 'fifanova' criada com dados de exemplo")

print()


# ────────────────────────────────────────────────────────────
#  OS 5 PASSOS DA LEITURA
# ────────────────────────────────────────────────────────────
#
#  1. create_engine()  → cria o motor de conexão
#  2. .connect()       → abre a conexão de fato
#  3. text()           → escreve a query SQL
#  4. pd.read_sql()    → executa e devolve um DataFrame
#  5. .close()         → fecha a conexão (SEMPRE!)

print("  ─" * 25)
print("  OS 5 PASSOS DA LEITURA")
print("  ─" * 25)
print()

# Passo 1 e 2 — já feitos acima (engine + conn)

# Passo 3 — escrever a query
#  text() é uma função do SQLAlchemy que recebe SQL como string
#  O foco aqui é Python — SQL é só a ferramenta de filtro
query = text("SELECT * FROM fifanova WHERE Potential > 80")

# Passo 4 — executar e receber DataFrame
#  pd.read_sql(query, conn) →
#  "execute essa query usando essa conexão e me dê um DataFrame"
df = pd.read_sql(query, conn)

print(f"  Query executada: SELECT * FROM fifanova WHERE Potential > 80")
print(f"  ✅ {len(df)} jogadores encontrados com Potential > 80")
print()
print("  Primeiros 5 resultados:")
print(df.head().to_string(index=False))
print()

# Passo 5 — fechar a conexão
#  Conexões abertas consomem recursos do servidor
#  Bom hábito: sempre fechar quando terminar
conn.close()
print("  🔒 Conexão fechada.")
print()


# ────────────────────────────────────────────────────────────
#  EXEMPLOS DE QUERY SQL — descomente e teste um por vez
# ────────────────────────────────────────────────────────────
#
#  SQL tem alguns "filtros" principais:
#
#  WHERE   → filtra linhas         (como if no Python)
#  ORDER BY → ordena resultado     (como sort)
#  GROUP BY → agrupa e calcula     (como groupby do pandas)
#  HAVING  → filtra grupos         (WHERE pós-agrupamento)
#  BETWEEN → seleciona intervalo   (como >= e <=)
#  LIMIT   → limita linhas         (como head())

print("  ─" * 25)
print("  EXEMPLOS DE QUERY")
print("  ─" * 25)

conn   = engine.connect()
queries = {
    "WHERE — jogadores brasileiros":
        "SELECT Name, Overall, Potential FROM fifanova WHERE Nationality = 'Brazil'",

    "ORDER BY — top 5 por Overall":
        "SELECT Name, Overall FROM fifanova ORDER BY Overall DESC LIMIT 5",

    "GROUP BY — média de Overall por nacionalidade":
        "SELECT Nationality, AVG(Overall) as media FROM fifanova GROUP BY Nationality",

    "BETWEEN — Overall entre 85 e 90":
        "SELECT Name, Overall FROM fifanova WHERE Overall BETWEEN 85 AND 90",
}

for descricao, sql in queries.items():
    print(f"\n  📌 {descricao}")
    print(f"     {sql}")
    df_ex = pd.read_sql(text(sql), conn)
    print(df_ex.to_string(index=False))

conn.close()
print()


# ────────────────────────────────────────────────────────────
#  EXERCÍCIO — Tente você mesmo
# ────────────────────────────────────────────────────────────
#
#  1. Conecte ao banco (harve_escola.db)
#  2. Traga jogadores da seleção brasileira
#  3. Ordene por Potential (maior primeiro)
#  4. Mostre só as colunas: Name, Overall, Potential
#  5. Feche a conexão
#
# ── Escreva seu código abaixo ────────────────────────────────


# ── Solução (não olhe antes de tentar!) ─────────────────────
# conn = engine.connect()
# query = text("""
#     SELECT Name, Overall, Potential
#     FROM fifanova
#     WHERE Nationality = 'Brazil'
#     ORDER BY Potential DESC
# """)
# df_brasil = pd.read_sql(query, conn)
# print(df_brasil)
# conn.close()

print("=" * 50)
print("  FIM DO BLOCO 3")
print("  Próximo: 04_escrevendo_bd/escrevendo_banco.py")
print("=" * 50)
