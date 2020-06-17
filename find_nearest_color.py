#!/usr/bin/python3

import json
import sys

import numpy as np

hex_col = sys.argv[1]
if len(hex_col) > 7 or len(hex_col) < 6:
    sys.exit(1)

with open("data.json") as f:
    data = json.load(f)

rgbs = np.array([list(col["rgb"].values()) for col in data])

col = []
for i in range(len(hex_col) == 7, 6 + (len(hex_col) == 7), 2):
    col.append(int(hex_col[i: i+2], 16))
col = np.array(col)

idx = np.argmin(np.linalg.norm(rgbs - col, axis=1))
print(data[idx])
