from sqlalchemy import create_engine, text
import pandas as pd

# SQLite local — cria um arquivo .db na pasta
engine = create_engine("sqlite:///teste_local.db")
conn = engine.connect()

# Cria uma tabela de teste
conn.execute(text("""
    CREATE TABLE IF NOT EXISTS fifanova (
        Name TEXT,
        Nationality TEXT,
        Overall INTEGER,
        Potential INTEGER
    )
"""))
conn.execute(text("""
    INSERT INTO fifanova VALUES 
    ('Messi', 'Argentina', 91, 91),
    ('Neymar', 'Brazil', 89, 89),
    ('Vinicius Jr', 'Brazil', 86, 92),
    ('Rodrygo', 'Brazil', 82, 88)
"""))
conn.commit()

# Testa a query que vai usar na aula
query = text("SELECT * FROM fifanova WHERE Potential > 88")
df = pd.read_sql(query, conn)
print(df)
conn.close()