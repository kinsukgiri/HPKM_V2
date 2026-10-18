# HPKM: Recursive Hyperplane Partitioning based centroid initialisation for k-means

`HPKM_final.ipynb` reproduces all the results of the paper and its Supplementary Material in one run:
Table 3, the cumulative explained variance of PCA, the convergence analysis on D31 (Fig. 3),
the per-dataset figures and Supplementary Tables S1 to S3 (comparison with Var-Part and the
variability of KM and k-means++).

## How to run
1. `pip install -r requirements.txt`
2. Put the 11 datasets in the folder `Datasets/` as `S1.csv`, `Aggregation.csv`, `D31.csv`, `Flame.csv`,
   `Hepta.csv`, `R15.csv`, `Target.csv`, `Iris.csv`, `Breast.csv`, `Yeast.csv`, `Wine.csv`.
   Each file contains the feature columns and a column named `Class` (used only for evaluation).
3. Run all the cells of `HPKM_final.ipynb`. All tables (`.xlsx`, `.csv`, `.tex`) and figures are written to `Results/`.

## Protocol
* The class column is excluded before PCA and clustering. PCA to 2-D is applied only when there are more than two features.
* HPKM splits the partition with the largest number of points, along the axis with the larger range, at its midpoint.
* All methods use the same k-means routine (at most 100 iterations, tolerance 1e-4).
* Time is end-to-end (initialisation + k-means), median of 5 repetitions for deterministic runs.
* Seeds: 42 for KM and k-means++ in Table 3, 0-29 for the variability study, 0-99 for the convergence analysis.

Execution times depend on the machine; all the other values are deterministic.
