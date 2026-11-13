# HPKM: Recursive Hyperplane Partitioning based centroid initialisation for k-means

`HPKM_final.ipynb` reproduces all the results of the paper and of its Supplementary Material in one run:
Table 3, the cumulative explained variance of PCA, the convergence analysis on D31 (Fig. 3), the per-dataset figures,
and Supplementary Tables S1 to S6 (comparison with Var-Part, variability of KM and k-means++, effect of PCA,
Wilcoxon tests and initialisation time on data of increasing size).

## How to run
1. `pip install -r requirements.txt`
2. Run all the cells of `HPKM_final.ipynb`. The input files are in `Datasets/`; all tables (`.xlsx`, `.csv`, `.tex`) and
   figures are written to `Results/`.

The source and the preparation of every dataset are described in `data_preparation/README.md`;
`data_preparation/prepare_breast.py` rebuilds `Datasets/Breast.csv` from the original UCI file.

## Protocol
* The class column is used only for evaluation; it is excluded before PCA and clustering. PCA to 2-D is applied only when there are more than two features.
* HPKM splits the partition with the largest number of points, along the axis with the larger range, at its midpoint (a strict `>` comparison of the two ranges).
* All methods use the same k-means routine (at most 100 iterations, tolerance 1e-4). The iteration count is the number of centroid-update steps performed, including the final step at which the change of the centroids falls below the tolerance.
* Time is end-to-end (initialisation + k-means), median of 5 repetitions for deterministic runs.
* Seeds: 42 for KM and k-means++ in Table 3, 0-29 for the variability study, 0-99 for the convergence analysis. ECKM and HPKM are also executed in each of the 100 convergence runs.

Execution times depend on the machine; all the other values are deterministic.
