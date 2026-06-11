# ============================================================
#  AULA 4 — DESAFIO FINAL: Pipeline ETL Completo
# ============================================================
#
#  MISSÃO:
#  Montar um pipeline ETL do zero combinando tudo que
#  você aprendeu hoje.
#
#  EXTRACT   → ler tabela "pais" do banco
#  TRANSFORM → adicionar 3 novos países
#  LOAD      → salvar tabela nova no banco
#  EXPORT    → exportar CSV com data no nome
#
#  Dependências: pip install pandas sqlalchemy
# ============================================================

import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

print("=" * 50)
print("  DESAFIO FINAL — PIPELINE ETL COMPLETO")
print("=" * 50)
print()

STRING_DE_CONEXAO = "sqlite:///harve_escola.db"
engine = create_engine(STRING_DE_CONEXAO)


# ────────────────────────────────────────────────────────────
#  PREPARAÇÃO — Criando a tabela "pais" no banco
# ────────────────────────────────────────────────────────────
#
#  A tabela já existe no banco real da Harve.
#  Aqui criamos localmente para o exercício funcionar.

conn = engine.connect()
conn.execute(text("DROP TABLE IF EXISTS pais"))
conn.execute(text("""
    CREATE TABLE pais (
        id         INTEGER,
        nome       TEXT,
        continente TEXT,
        populacao  INTEGER,
        capital    TEXT
    )
"""))
conn.execute(text("""
    INSERT INTO pais VALUES
    (1, 'Brasil',    'América do Sul', 215000000, 'Brasília'),
    (2, 'Argentina', 'América do Sul',  45000000, 'Buenos Aires'),
    (3, 'Chile',     'América do Sul',  19000000, 'Santiago'),
    (4, 'Colômbia',  'América do Sul',  51000000, 'Bogotá'),
    (5, 'Peru',      'América do Sul',  33000000, 'Lima'),
    (6, 'Uruguai',   'América do Sul',   3500000, 'Montevidéu'),
    (7, 'Paraguai',  'América do Sul',   7400000, 'Assunção'),
    (8, 'Bolívia',   'América do Sul',  12000000, 'Sucre')
"""))
conn.commit()
conn.close()

print("  ✅ Tabela 'pais' pronta no banco")
print()


# ────────────────────────────────────────────────────────────
#  CONTEXTO DO DESAFIO
# ────────────────────────────────────────────────────────────

print("  ─" * 25)
print("  CONTEXTO")
print("  ─" * 25)
print()

# Mostra o estado atual da tabela
conn       = engine.connect()
df_atual   = pd.read_sql(text("SELECT * FROM pais"), conn)
conn.close()

print("  Estado atual da tabela 'pais':")
print(df_atual.to_string(index=False))
print()
print("  SUA MISSÃO:")
print("  → Adicionar: Estados Unidos, Canadá, Groelândia")
print("  → Salvar como tabela nova: 'paises_novos_SEUNOME'")
print("  → Exportar para CSV com data no nome")
print()


# ────────────────────────────────────────────────────────────
#  PASSO 1 — EXTRACT: ler a tabela "pais" do banco
# ────────────────────────────────────────────────────────────
print("  ─" * 25)
print("  PASSO 1 — EXTRACT")
print("  ─" * 25)

# ── Seu código aqui ──────────────────────────────────────────


# ────────────────────────────────────────────────────────────
#  PASSO 2 — TRANSFORM: criar DataFrame com os 3 novos países
# ────────────────────────────────────────────────────────────
print("  ─" * 25)
print("  PASSO 2 — TRANSFORM")
print("  ─" * 25)

# ── Seu código aqui ──────────────────────────────────────────


# ────────────────────────────────────────────────────────────
#  PASSO 3 — TRANSFORM: unir os dois DataFrames
# ────────────────────────────────────────────────────────────
#  Dica: pd.concat([df1, df2], ignore_index=True)

# ── Seu código aqui ──────────────────────────────────────────


# ────────────────────────────────────────────────────────────
#  PASSO 4 — LOAD: salvar no banco como tabela nova
# ────────────────────────────────────────────────────────────
#  Nome: "paises_novos_seunome"  ← troque "seunome" pelo seu nome
#  if_exists="replace", index=False
#  Não esqueça: commit() e close()

# ── Seu código aqui ──────────────────────────────────────────


# ────────────────────────────────────────────────────────────
#  PASSO 5 — EXPORT: exportar CSV com data e hora no nome
# ────────────────────────────────────────────────────────────
#  Dica: datetime.now().strftime("%Y-%m-%d_%H%M")

# ── Seu código aqui ──────────────────────────────────────────


# ============================================================
#  SOLUÇÃO COMPLETA (não olhe antes de tentar!)
# ============================================================

# # PASSO 1 — EXTRACT
# conn       = engine.connect()
# df_paises  = pd.read_sql(text("SELECT * FROM pais"), conn)
# conn.close()
# print(f"\n  ✅ {len(df_paises)} países extraídos do banco")
# print(df_paises.to_string(index=False))

# # PASSO 2 — TRANSFORM: novos países
# novos = pd.DataFrame({
#     "id":         [df_paises["id"].max() + 1,
#                    df_paises["id"].max() + 2,
#                    df_paises["id"].max() + 3],
#     "nome":       ["Estados Unidos", "Canadá", "Groelândia"],
#     "continente": ["América do Norte"] * 3,
#     "populacao":  [331_000_000, 38_000_000, 56_000],
#     "capital":    ["Washington D.C.", "Ottawa", "Nuuk"],
# })
# print(f"\n  ✅ {len(novos)} novos países criados")

# # PASSO 3 — TRANSFORM: unir
# df_final = pd.concat([df_paises, novos], ignore_index=True)
# print(f"\n  ✅ DataFrame final: {len(df_final)} países")
# print(df_final.to_string(index=False))

# # PASSO 4 — LOAD
# conn = engine.connect()
# df_final.to_sql(
#     name      = "paises_novos_seunome",
#     con       = conn,
#     if_exists = "replace",
#     index     = False,
# )
# conn.commit()
# conn.close()
# print("\n  ✅ Tabela 'paises_novos_seunome' criada no banco!")

# # PASSO 5 — EXPORT
# agora = datetime.now().strftime("%Y-%m-%d_%H%M")
# nome  = f"paises_novos_{agora}.csv"
# df_final.to_csv(nome, index=False)
# print(f"  ✅ Exportado: {nome}")

print()
print("=" * 50)
print("  FIM DA AULA 4 — ETL com Python")
print("  ✅ CSV  ✅ Credenciais  ✅ Leitura  ✅ Escrita")
print("=" * 50)
