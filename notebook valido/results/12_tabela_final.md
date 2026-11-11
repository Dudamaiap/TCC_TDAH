| modelo | família | AUC média (folds) | AUC dp (folds) | AUC OOF | IC95 inf | IC95 sup | Acc. balanceada | Sensibilidade | Especificidade | F1 | IC inferior > 0,5 | execuções com 1 só classe prevista |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GAT | Grafo | 0.522 | 0.027 | 0.579 | 0.399 | 0.660 | 0.508 | 0.576 | 0.439 | 0.404 | não | 0 |
| Dummy_estratificado | Referência | 0.517 | 0.022 | — | — | — | 0.517 | 0.362 | 0.672 | 0.342 | — | 0 |
| XGBoost | Clássico | 0.506 | 0.034 | 0.451 | 0.334 | 0.568 | 0.502 | 0.210 | 0.794 | 0.223 | não | 0 |
| Random_Forest | Clássico | 0.504 | 0.037 | 0.390 | 0.291 | 0.537 | 0.501 | 0.010 | 0.992 | 0.017 | não | 3 |
| Dummy_prior | Referência | 0.500 | 0.000 | — | — | — | 0.500 | 0.000 | 1.000 | 0.000 | — | 5 |
| SVM_RBF | Clássico | 0.494 | 0.037 | 0.555 | 0.278 | 0.657 | 0.488 | 0.212 | 0.765 | 0.156 | não | 4 |
| GCN | Grafo | 0.490 | 0.057 | 0.535 | 0.438 | 0.647 | 0.495 | 0.393 | 0.598 | 0.315 | não | 0 |
| CNN | Deep learning | 0.406 | 0.061 | 0.355 | 0.233 | 0.564 | 0.427 | 0.294 | 0.559 | 0.225 | não | 0 |

Na base TDAH, o melhor desempenho médio entre folds foi do modelo GAT (AUC = 0.522 ± 0.027; AUC OOF = 0.579, IC 95% por bootstrap de sites [0.399, 0.660]). O IC incluiu 0,5; os resultados não permitem afirmar desempenho acima do acaso. Acurácia balanceada média de 0.508, sensibilidade 0.576 e especificidade 0.439. Os resultados vêm de validação cruzada de 5 folds agrupada por site, não de um conjunto de teste independente; não foram comparados com o diagnóstico clínico.
