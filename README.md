# Python ETL - Harve School

## 📖 O que é este projeto?
Este é o material prático do módulo de **Python ETL** da Harve. O objetivo deste repositório é mostrar na prática como:
- **Extrair** dados de arquivos e APIs da internet (como a HG Brasil Finance).
- **Transformar** e limpar esses dados usando a biblioteca `pandas` (como apagar colunas inúteis e cruzar informações).
- **Carregar** (salvar) os dados finais já tratados em novos formatos prontos para uso, como `.csv` e `.json`.

## 🚀 Como testar e executar (via Google Colab)

Nós utilizamos o **Google Colab** para rodar os códigos, o que significa que **você não precisa instalar nada no seu computador**. As bibliotecas principais (`pandas` e `requests`) já vêm prontas para uso.

Siga este passo a passo simples:

1. **Baixe o arquivo:** Faça o download do arquivo `Harve_School_API_application.ipynb` disponibilizado neste repositório.
2. **Acesse o Colab:** Abra o seu navegador e acesse [colab.research.google.com](https://colab.research.google.com/).
3. **Faça o Upload:** Na tela inicial do Colab, escolha a aba **Upload** (ou vá em *Arquivo > Fazer upload de notebook*) e arraste o arquivo `.ipynb` que você baixou.
4. **Execute o código:** Com o notebook aberto, basta ler as instruções de cada etapa e executar as células de código clicando no botão de **Play** ▶️ ao lado de cada bloco (ou selecionando o bloco e apertando `Shift + Enter`).

> 💡 *Dica:* Como o ambiente já está configurado na nuvem do Google, comandos complexos de instalação (`pip install`) não são necessários para as atividades base deste módulo!



# Simular um arquivo XML com dados de clientes
xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<clientes>
    <cliente>
        <id>001</id>
        <nome>João Silva</nome>
        <pais>Brasil</pais>
        <moeda>USD</moeda>
        <valor_contrato>10000</valor_contrato>
    </cliente>
    <cliente>
        <id>002</id>
        <nome>Maria Santos</nome>
        <pais>Brasil</pais>
        <moeda>USD</moeda>
        <valor_contrato>25000</valor_contrato>
    </cliente>
    <cliente>
        <id>003</id>
        <nome>Pedro Costa</nome>
        <pais>Brasil</pais>
        <moeda>EUR</moeda>
        <valor_contrato>15000</valor_contrato>
    </cliente>
</clientes>
"""

# Salvar para simular arquivo XML
with open('clientes.xml', 'w', encoding='utf-8') as f:
    f.write(xml_content)


    #DESAFIOSS!!
import pandas as pd

dados_estoque = {
    "Produto": ["Placa Mãe", "Processador", "Memória RAM", "Monitor", "Teclado"],
    "Moeda": ["USD", "USD", "EUR", "EUR", "USD"],
    "Preco_Original": [150.00, 250.00, 80.00, 200.00, 45.00]
}
df_estoque = pd.DataFrame(dados_estoque)
