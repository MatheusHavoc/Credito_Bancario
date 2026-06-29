# Credito Bancario - Analise de Risco de Credito

Estudo exploratorio sobre comportamento de clientes de cartao de credito em Taiwan. O notebook analisa perfil, pagamentos, inadimplencia e variaveis financeiras para apoiar discussoes de risco de credito.

## Objetivo

Entender fatores associados ao risco de inadimplencia e organizar uma base analitica para futuras etapas de modelagem de credito.

## O que o projeto demonstra

- Leitura de dados tabulares de credito.
- Avaliacao de qualidade: dimensoes, tipos, nulos, duplicados e outliers.
- Renomeacao e interpretacao de colunas para melhorar legibilidade analitica.
- Analises descritivas de variaveis categoricas e numericas.
- Visualizacoes com Plotly, Matplotlib e Seaborn.
- Investigacao de relacoes entre perfil do cliente, comportamento de pagamento e inadimplencia.

## Stack

- Python
- Pandas e NumPy
- Plotly, Matplotlib e Seaborn
- SciPy
- Jupyter Notebook / Google Colab

## Arquivos

| Arquivo | Descricao |
| --- | --- |
| `CréditoBancário.ipynb` | Notebook principal com limpeza, EDA e analise de risco. |

## Como executar

1. Abra o notebook no Google Colab ou Jupyter.
2. Disponibilize o arquivo `credit_card_clients.csv` no caminho esperado ou ajuste a celula de leitura.
3. Execute as celulas em ordem a partir da importacao das bibliotecas.

## Pontos fortes para portfólio

O tema tem forte aderencia a empresas financeiras, especialmente para entrevistas em bancos digitais e fintechs. O projeto mostra raciocinio sobre qualidade de dados e analise de comportamento de clientes, pontos relevantes para times de dados.

## Limitações atuais

- O projeto ainda nao esta estruturado como pipeline reproduzivel.
- O dataset nao esta documentado no repositorio.
- O notebook contem caminhos locais e de Google Drive.
- Falta uma secao executiva final com principais achados e recomendacoes.
- Ainda nao ha modelo preditivo versionado nem avaliacao automatizada.

## Próximas melhorias recomendadas

- Criar uma etapa de feature engineering para modelagem de inadimplencia.
- Adicionar baseline de classificacao e matriz de confusao.
- Separar funcoes de limpeza em scripts Python.
- Incluir `requirements.txt` e instrucoes de ambiente.
- Criar uma tabela final com insights, impacto esperado e limitacoes de negocio.
