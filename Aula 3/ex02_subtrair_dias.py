# =============================================================================
#  Harve School — ETL | Aula 3 | Parte 1: Transformando Data
# =============================================================================
#  EXERCÍCIO 2 — Subtraindo dias de uma data
#
# Objetivo: Se você pegar a data atual e diminuir 90 dias dela,
#           qual será a data resultado?
#
# Dicas:
#   - Use datetime.now() e timedelta para subtrair 90 dias da data atual
#   - Armazene o resultado em 'data_90_dias_atras'
#   - Imprima o resultado formatado
# =============================================================================

# Seu código aqui:


# =============================================================================
# RESOLUÇÃO 2
# =============================================================================

from datetime import datetime, timedelta

data_90_dias_atras = datetime.now() - timedelta(90)
print(f'Data atual:    {datetime.now()}')
print(f'90 dias atrás: {data_90_dias_atras.strftime("%d/%B/%y")}')
