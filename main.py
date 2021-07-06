import csv
import pandas as pd

data = []

data = pd.read_csv('brownStar.csv')

data = data[data["distance"].notna()]
data = data[data["mass"].notna()]
data = data[data["radius"].notna()]

data['mass'] = data['mass'].astype(float)
data['radius'] = data['radius'].astype(float)

data["mass"] = 0.000954588 * data["mass"]
data["radius"] = 0.102763 * data["radius"]

data.to_csv('brownStar_sorted.csv')