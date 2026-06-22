# Harve School — Material de Aulas

## 🌐 O que está neste repositório
Este repositório contém material de várias aulas e turmas da Harve School, não apenas Python ETL.
A ideia é organizar o conteúdo por pasta de turma, com cada turma tendo suas próprias pastas de aulas e material dentro delas.

### Estrutura atual
- `Exploração de Dados/` — material de análise e estatística descritiva
- `Python_ETL/` — material de ETL com Python, SQLAlchemy e SQLite/MySQL
- `README.md` — este guia de navegação e instalação

## 📁 Como o material está organizado
A estrutura foi pensada para ser fácil de navegar:

- Cada **turma** tem sua própria pasta no root
- Dentro de cada turma, há uma pasta para cada **aula**
- Dentro de cada aula estão notebooks, scripts e arquivos de dados

### Exemplo de navegação
```
Harve-School/
  Exploração de Dados/
    Aula 1/
    Aula 2/
    Aula 3/
    EDA.ipynb
  Python_ETL/
    Aula 3/
    Aula 4/
    Harve_School_API_application.ipynb
    install.py
    FUNCTIONS_DICTIONARY.md
```

> Se você tiver outra turma, siga o mesmo padrão: `Turma X / Aula Y / material`.

---

## 🧭 Guia ideal para quem estuda este material

### Se você está começando agora
1. Leia este `README.md` para entender a estrutura do repositório.
2. Abra a pasta da sua turma:
   - `Exploração de Dados` para análise de dados e estatística
   - `Python_ETL` para ETL, bancos de dados e pipelines Python
3. Abra o arquivo de aula correspondente:
   - Notebooks `.ipynb` para trabalhar em ambiente interativo
   - Scripts `.py` para executar no terminal
4. Execute os exemplos na ordem sugerida, de preferência com o Python do seu ambiente local.

### Se você quer um caminho rápido
- Para **Exploração de Dados**: comece por `Exploração de Dados/EDA.ipynb`
- Para **Python ETL**: comece por `Python_ETL/Aula 4/01_exportando_csv/exportando_csv.py`
- Para **SQLAlchemy**: veja `Python_ETL/Aula 4/02_credenciais_bd/credenciais.py` e `Python_ETL/Aula 4/03_lendo_bd/lendo_banco.py`

---

## 💻 Instalação recomendada

### 1. Instalar Python
A forma mais simples é baixar em:
- [Python 3.12](https://www.python.org/downloads/)

No Windows, marque a opção **Add Python to PATH** durante a instalação.

### 2. Criar um ambiente virtual
Abra o terminal e rode:
```bash
python -m venv .venv
```
Depois ative:
- Windows PowerShell:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- Windows CMD:
  ```cmd
  .\.venv\Scripts\activate.bat
  ```
- macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### 3. Instalar dependências
```bash
pip install pandas matplotlib seaborn requests sqlalchemy pymysql python-dotenv
```

> Dica: use `pip install --upgrade pip` antes para garantir a versão mais recente.

---

## 🧰 Instalar Git

### Windows
1. Baixe em: https://git-scm.com/download/win
2. Instale e mantenha as opções padrão.
3. Abra o **Git Bash** ou o terminal do VS Code.

### macOS
```bash
brew install git
```

### Ubuntu / Debian
```bash
sudo apt update
git --version
sudo apt install git
```

### Verificar instalação
```bash
git --version
```

---

## 🖥️ Como abrir o terminal e usar Git
### No Windows / VS Code
- Abra a pasta do projeto no VS Code
- Clique em **Terminal > New Terminal**
- Ou use o atalho: `Ctrl + ``
- Para abrir o controle de código-fonte, clique no ícone de **Source Control** (ícone de ramificação) na barra lateral esquerda

### Comandos Git importantes
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```
Verifica o usuário configurado:
```bash
git config --global user.name
git config --global user.email
```

### Atualizar o repositório
```bash
git pull origin main
```
- `git pull` = baixar alterações do repositório remoto e mesclar localmente

### Enviar suas alterações
```bash
git add .
git commit -m "mensagem explicando a mudança"
git push origin main
```
- `git push` = envia suas alterações para o repositório remoto

### Status e histórico
```bash
git status
git log --oneline --decorate --graph -n 10
```
- `git status` mostra arquivos modificados
- `git log` mostra histórico de commits

> Dica: sempre faça `git pull` antes de começar a trabalhar para evitar conflitos.

---

## 📘 Seções deste README
1. [Como funciona a pasta por turma/aula](#como-funciona-a-pasta-por-turmaaula)
2. [Instalação e ambiente](#instalação-e-ambiente)
3. [Git e terminal](#git-e-terminal)
4. [Material de Exploração de Dados](#material-de-exploração-de-dados)
5. [Material de Python ETL](#material-de-python-etl)
6. [SQLAlchemy e bancos](#sqlalchemy-e-bancos)
7. [Bibliotecas recomendadas](#bibliotecas-recomendadas)
8. [Links úteis](#links-úteis)

---

## Como funciona a pasta por turma/aula
Neste repositório, cada turma ou disciplina deve ter sua própria pasta no nível raiz.

### Exemplo de organização:
```
Harve-School/
  Exploração de Dados/
    Aula 1/
    Aula 2/
    Aula 3/
    EDA.ipynb
  Python_ETL/
    Aula 3/
    Aula 4/
    Harve_School_API_application.ipynb
    install.py
    FUNCTIONS_DICTIONARY.md
```

- `Exploração de Dados/` é a pasta desta disciplina principal.
- `Python_ETL/` é o material do módulo de ETL em Python.
- Cada `Aula X/` deve conter notebooks, scripts e dados específicos.
- Arquivos `.ipynb` são usados para notebooks interativos.
- Arquivos `.py` são exercícios ou exemplos executáveis.

---

## Instalação e ambiente
### Requisitos básicos
- Python 3.10 ou superior
- Git instalado
- Conexão com internet para baixar pacotes e consultar APIs

### Criar e usar ambiente virtual
```bash
python -m venv .venv
```
Ative o ambiente:
- PowerShell:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### Instalar bibliotecas comuns
```bash
pip install pandas matplotlib seaborn requests sqlalchemy pymysql python-dotenv
```

---

## Git e terminal
### Abrindo o terminal
- No VS Code: `Terminal > New Terminal`
- No Windows: pesquise por **PowerShell** ou **Git Bash**
- No macOS/Linux: abra o aplicativo Terminal

### Verificar usuário Git
```bash
git config --global user.name
git config --global user.email
```

### Configurar usuário Git
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### Fluxo básico com Git
```bash
git pull origin main
# trabalhar nas alterações
git status
git add .
git commit -m "Adiciona material da aula"
git push origin main
```

### O que é cada comando
- `git pull`: traz as últimas mudanças do repositório remoto
- `git add .`: prepara arquivos para commit
- `git commit -m "..."`: cria um ponto de versão local
- `git push`: envia suas mudanças para o GitHub remoto
- `git status`: mostra arquivos alterados

### Ícone de controle de versão no VS Code
No VS Code, o ícone de controle de versão parece uma ramificação ou fonte:
- clique nele para ver arquivos modificados
- use os botões `+` para stage, `✓` para commit e `...` para ações adicionais

---

## Material de Exploração de Dados
A pasta principal para esta disciplina é `Exploração de Dados`.

### Conteúdo disponível
- `EDA.ipynb` — notebook principal de exploração de dados
- `Aula 1/`, `Aula 2/`, `Aula 3/` — pastas onde cada aula deve guardar material específico
- `Exploração_De_Dados/*.py` — scripts gerados para separar os exercícios do notebook

### O que aprender aqui
- Tipos de dados qualitativos e quantitativos
- Medidas de posição: média, mediana e moda
- Medidas de dispersão: amplitude, desvio padrão, CV
- Quartis, boxplot e outliers
- Distribuição de frequência e tabelas de contingência

### Dicas de instalação específicas
Para análise de dados, recomendamos também:
```bash
pip install jupyterlab
```
Se preferir usar o notebook localmente:
```bash
jupyter notebook
```

---

## Material de Python ETL
A pasta principal para ETL é `Python_ETL`.

### Estrutura principal
- `install.py` — exemplo de banco SQLite local
- `Harve_School_API_application.ipynb` — notebook de aula
- `Harve_School_ETL_first_class.ipynb` — primeiro notebook de ETL
- `FUNCTIONS_DICTIONARY.md` — dicionário de funções usadas nos scripts
- `Aula 3/` — exercícios de manipulação de datas e previsão do tempo
- `Aula 4/` — pipeline ETL completo com CSV e banco de dados

### Principais arquivos em `Aula 4`
- `01_exportando_csv/exportando_csv.py`
- `02_credenciais_bd/credenciais.py`
- `03_lendo_bd/lendo_banco.py`
- `04_escrevendo_bd/escrevendo_banco.py`
- `05_desafio/desafio_final.py`
- `banco/popular_banco.py`

### O que aprender aqui
- Extração de dados de APIs
- Transformação de dados com `pandas`
- Salvamento em `.csv`
- Conexão a bancos com `SQLAlchemy`
- Criação e leitura de tabelas SQLite/MySQL
- Uso de `to_sql`, `read_sql`, `commit()` e `close()`

### Dicas de instalação específicas
```bash
pip install sqlalchemy pymysql python-dotenv
```

### SQLAlchemy rápido
- `create_engine(...)` → cria o motor de conexão
- `engine.connect()` → abre a conexão com o banco
- `text(...)` → cria a query SQL
- `pd.read_sql(query, conn)` → traz o resultado para DataFrame
- `df.to_sql(name, con, if_exists, index=False)` → salva no banco
- `conn.commit()` → confirma a escrita
- `conn.close()` → fecha a conexão

---

## Bibliotecas recomendadas
- pandas: https://pandas.pydata.org/
- matplotlib: https://matplotlib.org/
- seaborn: https://seaborn.pydata.org/
- requests: https://docs.python-requests.org/
- sqlalchemy: https://www.sqlalchemy.org/
- pymysql: https://pymysql.readthedocs.io/
- python-dotenv: https://saurabh-kumar.com/python-dotenv/

---

## Links úteis
- Git: https://git-scm.com/
- GitHub Docs: https://docs.github.com/
- VS Code Source Control: https://code.visualstudio.com/docs/editor/versioncontrol
- Instalar Python: https://www.python.org/downloads/
- SQLAlchemy Docs: https://docs.sqlalchemy.org/
- Pandas Docs: https://pandas.pydata.org/docs/

---

## Dicas finais
- Sempre use `git pull` antes de começar um dia de estudo.
- Mantenha seu ambiente virtual ativado ao trabalhar.
- Se estiver usando o VS Code, prefira o terminal integrado e o painel Source Control.
- Para cada nova aula, crie uma nova pasta `Aula X` e coloque o material lá.
- Documente no commit o que foi alterado, por exemplo: `git commit -m "Adiciona solução do exercício de quartis"`.

Boa jornada de estudos!

