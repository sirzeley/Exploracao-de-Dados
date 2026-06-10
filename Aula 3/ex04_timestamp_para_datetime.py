# =============================================================================
#  Harve School — ETL | Aula 3 | Parte 1: Transformando Data
# =============================================================================
#  EXERCÍCIO 4 — Convertendo timestamp para datetime
#
# Objetivo: Faça o caminho inverso — converta o número 1702387987
#           (timestamp em segundos) para um datetime legível.
#
# Dicas:
#   - Use datetime.utcfromtimestamp(N) passando o timestamp como argumento
#   - Imprima o timestamp original e a data/hora convertida
# =============================================================================

timestamp_segundos = 1781045640

# Seu código aqui:


# =============================================================================
#  RESOLUÇÃO 4
# =============================================================================

import datetime

timestamp_segundos = 1781045640
data_convertida = datetime.datetime.utcfromtimestamp(timestamp_segundos)

print(f'Timestamp: {timestamp_segundos}')
print(f'Data/hora: {data_convertida}')
