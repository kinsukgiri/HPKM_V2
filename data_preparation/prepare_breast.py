"""Prepare Breast.csv from the Breast Cancer Wisconsin (Original) dataset of the UCI repository.

Source : https://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original
Raw file: breast-cancer-wisconsin.data (699 records, ID + 9 attributes + class, '?' = missing)

Processing:
  * the sample ID column is removed,
  * the 16 records with a missing value of Bare Nuclei ('?') are removed (683 records remain),
  * the diagnosis (2 = benign, 4 = malignant) is written to the column 'Class', which is used only for evaluation.

Usage:  python prepare_breast.py [path/to/breast-cancer-wisconsin.data] [output.csv]
If no input path is given, the raw file is downloaded from the UCI repository.
"""
import sys, urllib.request
import pandas as pd

URL = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
       "breast-cancer-wisconsin/breast-cancer-wisconsin.data")
COLS = ["ID", "Clump_Thickness", "Uniformity_Cell_Size", "Uniformity_Cell_Shape", "Marginal_Adhesion",
        "Single_Epithelial_Cell_Size", "Bare_Nuclei", "Bland_Chromatin", "Normal_Nucleoli", "Mitoses", "Class"]

def main(src=None, out="Breast.csv"):
    if src is None:
        src = "breast-cancer-wisconsin.data"
        urllib.request.urlretrieve(URL, src)
    df = pd.read_csv(src, header=None, names=COLS, na_values="?")
    n0 = len(df)
    df = df.dropna().drop(columns=["ID"]).astype(int)
    df.to_csv(out, index=False)
    print(f"{n0} records read, {n0 - len(df)} with missing values removed, {len(df)} written to {out}")
    print("Class counts:", df["Class"].value_counts().sort_index().to_dict())

if __name__ == "__main__":
    main(*(sys.argv[1:3]))
