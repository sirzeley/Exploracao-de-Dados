# ============================================================
#  AULA 4 — BLOCO 2: Credenciais para Banco de Dados
# ============================================================
#
#  O QUE VAMOS APRENDER:
#  ✅ O que são credenciais de banco de dados
#  ✅ Como organizar em um dicionário Python
#  ✅ Como montar a string de conexão
#  ✅ Como conectar usando SQLAlchemy
#
# ============================================================

from sqlalchemy import create_engine, text

# ────────────────────────────────────────────────────────────
#  PASSO 1 — As 5 credenciais necessárias
# ────────────────────────────────────────────────────────────
#
#  Para acessar qualquer banco de dados precisamos de:
#
#  hostname → endereço do servidor  (onde o banco mora)
#  username → nome do usuário       (quem está entrando)
#  password → senha do usuário      (prova de identidade)
#  port     → porta de entrada      (MySQL sempre usa 3306)
#  database → nome do banco         (qual banco dentro do servidor)
#
#  Analogia:
#  hostname = endereço do prédio
#  port     = número do apartamento
#  database = qual cômodo você quer
#  username = seu nome
#  password = sua chave

credenciais = {
    "hostname": "localhost",        # endereço do servidor
    "username": "aluno",            # usuário
    "password": "harve123",         # senha
    "port":      3306,              # porta padrão do MySQL
    "database":  "moduloetl",       # nome do banco
}

print("=" * 50)
print("  CREDENCIAIS CONFIGURADAS")
print("=" * 50)
for chave, valor in credenciais.items():
    # Oculta a senha no print por segurança
    exibir = "****" if chave == "password" else valor
    print(f"  {chave:10} → {exibir}")
print()


# ────────────────────────────────────────────────────────────
#  PASSO 2 — Montando a String de Conexão
# ────────────────────────────────────────────────────────────
#
#  O SQLAlchemy precisa das credenciais num formato específico:
#
#  mysql+pymysql:// USUARIO : SENHA @ HOST : PORTA / BANCO
#  ──────────────── ──────── ─────── ────── ──────── ──────
#       driver        login   senha  servidor porta   banco
#
#  No nosso caso com SQLite (banco local, sem servidor):
#
#  sqlite:///nome_do_arquivo.db
#  ────────────────────────────
#  mais simples: sem usuário, senha ou porta
#  o arquivo é criado automaticamente na pasta

STRING_DE_CONEXAO = "sqlite:///harve_escola.db"

print("  STRING DE CONEXÃO:")
print(f"  {STRING_DE_CONEXAO}")
print()
print("  💡 SQLite = banco local, arquivo no seu computador")
print("     Não precisa de servidor, usuário ou senha")
print()


# ────────────────────────────────────────────────────────────
#  PASSO 3 — Criando o Engine e Conectando
# ────────────────────────────────────────────────────────────
#
#  create_engine() → cria o "motor" que sabe falar com o banco
#  .connect()      → abre a conexão de fato
#
#  O try/except captura erros e mostra uma mensagem clara
#  em vez de travar com um erro gigante

print("=" * 50)
print("  TESTANDO CONEXÃO...")
print("=" * 50)

try:
    engine = create_engine(STRING_DE_CONEXAO)
    conn   = engine.connect()

    # SELECT 1 é o teste mais simples possível
    # Só verifica se o banco responde — não acessa dado nenhum
    conn.execute(text("SELECT 1"))

    print("  ✅ Engine criado com sucesso!")
    print("  ✅ Conexão estabelecida!")
    print("  ✅ Banco respondendo!")
    print()
    print("  📁 Arquivo criado: harve_escola.db")

except Exception as erro:
    print(f"  ❌ Erro: {erro}")
    conn = None

finally:
    if conn:
        conn.close()
        print()
        print("  🔒 Conexão fechada.")


# ────────────────────────────────────────────────────────────
#  RESUMO DO BLOCO
# ────────────────────────────────────────────────────────────
print()
print("=" * 50)
print("  RESUMO")
print("=" * 50)
print("  1. Credenciais  → 5 informações para acessar o banco")
print("  2. String       → formato que o SQLAlchemy entende")
print("  3. Engine       → motor de conexão")
print("  4. connect()    → abre a conexão")
print("  5. close()      → fecha a conexão (sempre!)")
