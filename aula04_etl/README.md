# Aula 4 — ETL com Python: CSV e Banco de Dados
**Harve Bootcamp de Tecnologia**

---

## 🗺️ De onde vêm os dados (mapa completo)

| Tabela/Arquivo | Fonte | Como chega |
|---|---|---|
| `previsao_tempo` | HG Brasil Weather API | `banco/popular_banco.py` cria no banco |
| `cotacoes` | HG Brasil Finance API | `banco/popular_banco.py` cria no banco |
| `fifaplayers` | harve.com.br/praticas/fifaplayers_pt.csv | `banco/popular_banco.py` cria no banco |
| `pais` | Criado localmente | `banco/popular_banco.py` cria no banco |
| `stock_petr4.csv` | Repo rafaelpyc/harve (GitHub) | Já está em `/dados` |

---

## 📂 Estrutura da pasta

```
aula04_etl/
│
├── banco/
│   └── popular_banco.py     ← ⚠️  RODE ANTES DA AULA para criar as tabelas
│
├── dados/
│   ├── stock_petr4.csv      ← ações PETR4 (repo Harve)
│   ├── negociacao.csv       ← vendas DW (repo Harve)
│   ├── cliente.csv          ← clientes (repo Harve)
│   ├── funcionario.csv      ← funcionários (repo Harve)
│   ├── cargo.csv            ← cargos (repo Harve)
│   ├── equipe.csv           ← equipes (repo Harve)
│   ├── pagamento.csv        ← pagamentos (repo Harve)
│   └── data.csv             ← dimensão datas (repo Harve)
│
├── 01_exportando_csv/
│   └── exportando_csv.py    ← HG Brasil → DataFrame → CSV
│
├── 02_credenciais_bd/
│   ├── credenciais.py       ← dicionário, .env, string de conexão
│   └── .env.exemplo
│
├── 03_lendo_bd/
│   └── lendo_banco.py       ← read_sql nas tabelas do banco
│
├── 04_escrevendo_bd/
│   └── escrevendo_banco.py  ← HG Brasil → DataFrame → banco (ETL completo)
│
└── 05_desafio/
    └── desafio_final.py     ← ler tabela pais → adicionar países → salvar
```

---

## ⚡ Como preparar a aula

### 1. Instale as dependências
```bash
pip install pandas sqlalchemy pymysql requests python-dotenv
```

### 2. ⚠️  Popule o banco (fazer ANTES da aula)
Abra `banco/popular_banco.py`, preencha a `STRING_DE_CONEXAO` com as
credenciais reais e rode:
```bash
python banco/popular_banco.py
```
Saída esperada:
```
✅ Conectado ao banco.
✅ previsao_tempo — 15 linhas
✅ cotacoes — 9 linhas
✅ fifaplayers — XXXX linhas
✅ pais — 8 linhas
✅ BANCO POPULADO COM SUCESSO!
```

### 3. Preencha as credenciais nos exercícios
Nos arquivos dos blocos 2, 3, 4 e 5, substitua:
```python
STRING_DE_CONEXAO = "mysql+pymysql://USUARIO:SENHA@HOST:3306/BANCO"
```

---

## 📋 Agenda da Aula (3h30)

| Horário | Bloco | Arquivo | Tabela/dado |
|---|---|---|---|
| 0:00–0:35 | Exportando para CSV | `01_exportando_csv/exportando_csv.py` | HG Brasil API (ao vivo) |
| 0:35–1:20 | Credenciais para BD | `02_credenciais_bd/credenciais.py` | — |
| 1:20–1:55 | Lendo dados do BD | `03_lendo_bd/lendo_banco.py` | `previsao_tempo`, `fifaplayers` |
| 1:55–2:35 | Escrevendo no BD | `04_escrevendo_bd/escrevendo_banco.py` | HG Brasil → `cotacoes` |
| 2:35–3:00 | Desafio Final | `05_desafio/desafio_final.py` | `pais` |
| 3:00–3:30 | Dúvidas e revisão | — | — |
