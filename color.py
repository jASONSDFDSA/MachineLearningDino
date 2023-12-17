import numpy as np
import csv
import pandas as pd

colors = []
for i in range(256):
    colors.append(np.array([i, i, i]))

for i in reversed(range(255)):
    colors.append(np.array([i, i, i]))

colors = np.array(colors)

filename="colors.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)

    # 逐行写入数据
    for row in colors:
        writer.writerow(row)

colors = np.array(pd.read_csv('colors.csv'))
print(colors.shape)