import pandas as pd
from datetime import datetime

df = pd.read_csv("/Aula 3/chamados.csv")
df["data_abertura"] = pd.to_datetime(df["data_abertura"])

abertos = df[df["status"] == "aberto"].copy()

abertos["dias_aberto"] = (datetime.now() - abertos["data_abertura"]).dt.days

atrasados = abertos[abertos["dias_aberto"] > 3]

print(f"Chamados em aberto há mais de 3 dias: {len(atrasados)}\n")

for _, row in atrasados.iterrows():
    if row["prioridade"] == "alta":
        nivel = "URGENTE"
    else:
        nivel = "atenção"

    print(f"[{nivel}] ID {int(row['id'])} | {row['cliente']} | {int(row['dias_aberto'])} dias | prioridade: {row['prioridade']}")

mais_antigo = abertos.loc[abertos["dias_aberto"].idxmax()]
print(f"\nChamado mais antigo: ID {int(mais_antigo['id'])} — {mais_antigo['cliente']} ({int(mais_antigo['dias_aberto'])} dias)")
print(f"Total de chamados abertos: {len(abertos)}")