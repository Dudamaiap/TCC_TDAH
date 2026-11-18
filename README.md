# TCC TDAH

Projeto de classificação de TDAH com dados de conectividade funcional do ADHD-200.

## Estado atual

O fluxo oficial usa a amostra validada de **709 participantes** (256 TDAH, 453 controles, 9 sites). Os dados preparados, matrizes de conectividade, resultados, figuras e modelos já existentes fazem parte deste fluxo. **Não é necessário executar os notebooks para consultar os resultados disponíveis.**

## Estrutura do projeto

```text
data/
  raw/                 dados de origem
  extracted/           dados extraídos
  processed/           participantes, validação e dataset preparado
  connectivity/        matrizes FC_<id>.npy
notebooks/
  01_Configuracao_ADHD200.ipynb
  02_Download_ADHD200.ipynb
  ...
  12_Resultados_Finais_Corretos_ADHD200.ipynb
models/                checkpoints e modelos treinados
results/               métricas, previsões e tabelas consolidadas
figures/               figuras dos resultados atuais
docs/                  documentação de apoio
```

## Fluxo dos notebooks

| Nº | Notebook | Conteúdo |
|---:|---|---|
| 01 | [`01_Configuracao_ADHD200.ipynb`](notebooks/01_Configuracao_ADHD200.ipynb) | Configuração do ambiente e pastas |
| 02 | [`02_Download_ADHD200.ipynb`](notebooks/02_Download_ADHD200.ipynb) | Obtenção/preparação dos dados de origem |
| 03 | [`03_Exploracao_ADHD200.ipynb`](notebooks/03_Exploracao_ADHD200.ipynb) | Exploração fenotípica |
| 04 | [`04_Selecao_Correta_ADHD200.ipynb`](notebooks/04_Selecao_Correta_ADHD200.ipynb) | Seleção de participantes e dados |
| 05 | [`05_Validacao_Correta_ADHD200.ipynb`](notebooks/05_Validacao_Correta_ADHD200.ipynb) | Validação da amostra |
| 06 | [`06_Analise_Exploratoria_ADHD200.ipynb`](notebooks/06_Analise_Exploratoria_ADHD200.ipynb) | Análise exploratória da amostra validada |
| 07 | [`07_Preparacao_Correta_ADHD200.ipynb`](notebooks/07_Preparacao_Correta_ADHD200.ipynb) | Preparação do dataset para modelos |
| 08 | [`08_Baselines_Correto_ADHD200.ipynb`](notebooks/08_Baselines_Correto_ADHD200.ipynb) | SVM RBF, Random Forest e XGBoost |
| 09 | [`09_Deep_Learning_Correto_ADHD200.ipynb`](notebooks/09_Deep_Learning_Correto_ADHD200.ipynb) | MLP e BrainNetCNN |
| 10 | [`10_Grafos_Corretos_ADHD200.ipynb`](notebooks/10_Grafos_Corretos_ADHD200.ipynb) | GCN, GAT e BrainGNN |
| 11 | [`11_XAI_Correto_ADHD200.ipynb`](notebooks/11_XAI_Correto_ADHD200.ipynb) | Explicabilidade; usa os resultados do notebook 08 |
| 12 | [`12_Resultados_Finais_Corretos_ADHD200.ipynb`](notebooks/12_Resultados_Finais_Corretos_ADHD200.ipynb) | Consolidação; depende dos notebooks 08–10 |

Os 12 notebooks ficam diretamente nesta pasta e estão listados em sequência lógica. Como a amostra validada, matrizes e artefatos dos modelos atuais já estão presentes, **não é preciso reexecutá-los para consultar os resultados**. Os notebooks 01–07 documentam configuração, aquisição, exploração e preparação; para reproduzir os resultados de modelagem, o fluxo parte dos dados já preparados nos notebooks 08–10, seguido do 12. O notebook 11 é opcional.

## Resultados já disponíveis

- Tabela final: [`results/12_tabela_final.md`](results/12_tabela_final.md) e [`results/12_tabela_final.csv`](results/12_tabela_final.csv).
- Resultados detalhados por modelo e fold: arquivos `08_*`, `09_*` e `10_*` em `results/`.
- Resultados de explicabilidade: arquivos `11_*` em `results/`.
- Figuras finais: `figures/12_*.png`; figuras de XAI: `figures/11_*.png`.

Os artefatos acima são os resultados existentes do fluxo atual. A execução dos notebooks serve para reproduzir ou atualizar esses artefatos e não é necessária para consultá-los.

## Ambiente e execução (opcional)

A partir da raiz do repositório:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyter lab
```

Para reproduzir os resultados a partir dos dados preparados, execute os notebooks 08 → 09 → 10 → 12. O notebook 11 é opcional. Para refazer a preparação, siga os notebooks 04 → 05 → 06 → 07 antes dos modelos; 01–03 tratam da configuração, obtenção e exploração inicial dos dados. Os notebooks 09 e 10 podem exigir bastante tempo e memória, especialmente em CPU.

## Dados e protocolo

- Atlas CC200 com **190 ROIs** utilizadas no experimento.
- Validação cruzada agrupada por site, com 5 folds.
- Semente configurada em `config.py`.
- Os resultados são de validação cruzada, não de um conjunto de teste independente; não foram comparados com diagnóstico clínico.

Consulte [`config.py`](config.py) para caminhos e parâmetros e [`avaliacao.py`](avaliacao.py) para as rotinas de avaliação compartilhadas.
