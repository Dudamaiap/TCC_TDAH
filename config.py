from pathlib import Path
import numpy as np



# RAIZ DO PROJETO


RAIZ = Path(__file__).resolve().parent



# ESTRUTURA PRINCIPAL DO PROJETO


DATA = RAIZ / "data"
DOCS = RAIZ / "docs"
FIGURES = RAIZ / "figures"
MODELS = RAIZ / "models"
NOTEBOOKS = RAIZ / "notebooks"
RESULTS = RAIZ / "results"



# SUBPASTAS DE DADOS


RAW = DATA / "raw"
EXTRACTED = DATA / "extracted"
PROCESSED = DATA / "processed"
CONNECTIVITY = DATA / "connectivity"



# ARQUIVOS DE ENTRADA


# Arquivo compactado contendo os dados de rs-fMRI
# pré-processados pelo pipeline Athena e representados
# utilizando o atlas CC200.

ARQ_TAR = RAW / "ADHD200_CC200_TCs_filtfix.tar.gz"

# Arquivo fenotípico do ADHD-200
ARQ_PHENO = RAW / "adhd200_preprocessed_phenotypics.tsv"



# ARQUIVOS GERADOS PELO PROJETO


# Participantes selecionados após os critérios de inclusão/QC
ARQ_PARTICIPANTES = PROCESSED / "participants.csv"

# Identificadores das ROIs utilizadas
ARQ_ROIS = PROCESSED / "roi_ids.npy"

# Dataset final preparado para Machine Learning
ARQ_DATASET = PROCESSED / "dataset.npz"



# CONFIGURAÇÕES DO EXPERIMENTO


# Número de regiões de interesse utilizadas nos dados Athena/CC200
N_ROIS = 190

# Número de conexões únicas da matriz simétrica 190 x 190
N_CONNECTIONS = N_ROIS * (N_ROIS - 1) // 2

# Número de folds da validação cruzada
N_FOLDS = 5

# Semente para garantir reprodutibilidade
SEED = 42



# CONFIGURAÇÃO DAS CLASSES

# Controle
CONTROL_LABEL = 0

# TDAH
ADHD_LABEL = 1

# Códigos fenotípicos considerados TDAH no ADHD-200
ADHD_DX_CODES = [1, 2, 3]



# COLUNAS PADRÃO


ID_COLUMN = "participant_id"

TARGET_COLUMN = "target"

SITE_COLUMN = "site"


# CRIAÇÃO DA ESTRUTURA DE PASTAS

def criar_pastas():
    """
    Cria toda a estrutura de diretórios necessária
    para o projeto TDAH.
    """

    pastas = [
        DATA,
        RAW,
        EXTRACTED,
        PROCESSED,
        CONNECTIVITY,
        DOCS,
        FIGURES,
        MODELS,
        NOTEBOOKS,
        RESULTS,
    ]

    for pasta in pastas:
        pasta.mkdir(parents=True, exist_ok=True)


# CARREGAMENTO DAS MATRIZES DE CONECTIVIDADE


def carregar_fc(ids):
    """
    Carrega as matrizes de conectividade funcional
    dos participantes informados.

    Cada arquivo deve estar no formato:

        FC_<id>.npy

    e conter uma matriz 190 x 190.
    """

    return np.stack(
        [
            np.load(CONNECTIVITY / f"FC_{i}.npy")
            for i in ids
        ]
    ).astype(np.float32)