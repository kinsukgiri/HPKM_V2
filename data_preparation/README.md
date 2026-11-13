# Input datasets and their preparation

The folder `Datasets/` contains the exact input files used for every result in the paper and in its Supplementary Material.
Each file contains the numeric feature columns and one column named `Class`. The class label is used **only for evaluation**:
it is removed before PCA and before clustering by the notebook.

| Dataset | Records | Features | Classes | Source | SHA-256 (first 16 hex) |
|---|---|---|---|---|---|
| S1 | 5000 | 2 | 15 | Clustering basic benchmark, University of Eastern Finland, https://cs.uef.fi/sipu/datasets/ | `75e8d8cc76520f16` |
| Aggregation | 788 | 2 | 7 | Clustering basic benchmark, University of Eastern Finland, https://cs.uef.fi/sipu/datasets/ | `7915d7882a3dfbbb` |
| D31 | 3100 | 2 | 31 | Clustering basic benchmark, University of Eastern Finland, https://cs.uef.fi/sipu/datasets/ | `1c8cc78a8c7a5660` |
| Flame | 240 | 2 | 2 | Clustering basic benchmark, University of Eastern Finland, https://cs.uef.fi/sipu/datasets/ | `80b7cef979f2185f` |
| R15 | 600 | 2 | 15 | Clustering basic benchmark, University of Eastern Finland, https://cs.uef.fi/sipu/datasets/ | `3be2b890b4cec34d` |
| Hepta | 212 | 3 | 7 | Fundamental Clustering Problems Suite (FCPS), https://doi.org/10.1016/j.dib.2020.105501 | `fbec70a32aca361c` |
| Target | 770 | 2 | 6 | Fundamental Clustering Problems Suite (FCPS), https://doi.org/10.1016/j.dib.2020.105501 | `b48cc8efa678e821` |
| Iris | 150 | 4 | 3 | UCI Machine Learning Repository, Iris, https://doi.org/10.24432/C56C76 | `74834d0defd552a3` |
| Breast | 683 | 9 | 2 | UCI Machine Learning Repository, Breast Cancer Wisconsin (Original), https://doi.org/10.24432/C5HP4Z | `836d0449a71145a5` |
| Yeast | 1484 | 8 | 10 | UCI Machine Learning Repository, Yeast, https://doi.org/10.24432/C5KG68 | `22dec630d743c082` |
| Wine | 178 | 13 | 3 | UCI Machine Learning Repository, Wine, https://doi.org/10.24432/C5PC7J | `2c141c8828b53675` |

## Preparation

* **Synthetic datasets (S1, Aggregation, D31, Flame, R15, Hepta, Target):** the two (Hepta: three) coordinates and the ground-truth
  label of the original benchmark files, with the label column named `Class`. No other change.
* **Iris, Yeast, Wine:** the numeric attributes and the class attribute of the UCI files, with the class column named `Class`
  (the sequence name of Yeast is not used). No record is removed.
* **Breast (Breast Cancer Wisconsin, Original):** prepared with `prepare_breast.py` from the raw UCI file
  `breast-cancer-wisconsin.data`. The sample ID is removed, the 16 records with a missing value of Bare Nuclei (`?`) are removed,
  and the diagnosis (2 = benign, 4 = malignant) is written to `Class`. The result has 683 records (444 benign, 239 malignant),
  9 attributes and 2 classes.

```
python prepare_breast.py                                   # downloads the raw file from UCI
python prepare_breast.py breast-cancer-wisconsin.data ../Datasets/Breast.csv
```

**Note on the earlier version.** In the version of `Breast.csv` used before this revision, the diagnosis column and the attribute
Bare Nuclei had been lost, and the attribute Mitoses had been used as the class label (9 values). All Breast results have been
regenerated with the corrected file.
