"""
Script auxiliar — cria dados locais para testes offline.

Execute UMA VEZ antes de começar:
    python dados/gerar_dados.py

Os CSVs reais do repositório já estão nesta pasta (stock_petr4, negociacao, etc).
Este script gera apenas os dados que NÃO existem no repo:
  - previsao_tempo_sp.csv  → usado nos exemplos de leitura do banco
  - paises.csv             → usado no desafio final
"""

import pandas as pd
import os

pasta = os.path.dirname(os.path.abspath(__file__))

# ── Previsão do tempo — São Paulo ─────────────────────────────────────────────
previsao = pd.DataFrame({
    "data":               pd.date_range("2024-01-01", periods=10, freq="D"),
    "cidade":             "São Paulo",
    "temp_min":           [18, 20, 17, 22, 19, 21, 16, 23, 20, 18],
    "temp_max":           [28, 30, 25, 32, 27, 29, 24, 33, 28, 26],
    "umidade":            [75, 70, 80, 65, 72, 68, 85, 60, 73, 78],
    "probabilidade_chuva":[30, 20, 60, 10, 40, 25, 70,  5, 35, 50],
    "condicao":           ["Nublado","Ensolarado","Chuvoso","Ensolarado",
                           "Parcialmente nublado","Ensolarado","Tempestade",
                           "Ensolarado","Nublado","Chuvoso"],
})
previsao.to_csv(f"{pasta}/previsao_tempo_sp.csv", index=False)
print("✅  previsao_tempo_sp.csv gerado")

# ── Países da América do Sul ──────────────────────────────────────────────────
paises = pd.DataFrame({
    "id":         [1, 2, 3, 4, 5, 6, 7, 8],
    "nome":       ["Brasil","Argentina","Chile","Colômbia","Peru","Uruguai","Paraguai","Bolívia"],
    "continente": ["América do Sul"] * 8,
    "populacao":  [215_000_000, 45_000_000, 19_000_000, 51_000_000,
                   33_000_000, 3_500_000, 7_400_000, 12_000_000],
    "capital":    ["Brasília","Buenos Aires","Santiago","Bogotá",
                   "Lima","Montevidéu","Assunção","Sucre"],
})
paises.to_csv(f"{pasta}/paises.csv", index=False)
print("✅  paises.csv gerado")

print("\n✅  Dados auxiliares gerados. CSVs disponíveis na pasta /dados:")
for f in sorted(os.listdir(pasta)):
    if f.endswith(".csv"):
        print(f"   {f}")
