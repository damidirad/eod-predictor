import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import numpy as np
import re

paths = ['data/drive-download-20240618T155245Z-001/Explore-logs-A-data-2024-06-11.csv',
          'data/drive-download-20240618T155245Z-001/Explore-logs-A-data-2024-06-12.csv',
          'data/drive-download-20240618T155245Z-001/Explore-logs-A-data-2024-06-13.csv',
          'data/drive-download-20240618T155245Z-001/Explore-logs-A-data-2024-06-14.csv',
          'data/drive-download-20240618T155245Z-001/Explore-logs-A-data-2024-06-15.csv',
          'data/drive-download-20240618T155245Z-001/Explore-logs-A-data-2024-06-16.csv',
          'data/drive-download-20240618T155245Z-001/Explore-logs-A-data-2024-06-17.csv',
          'data/drive-download-20240618T155245Z-001/Explore-logs-A-data-2024-06-18.csv']

def get_names_durations(path):
    df = pd.read_csv(path)
    
    t = []
    n = []
    d = []
    id = []

    pattern = r"INFO\s*\[(.*?)\].*duration: (\d*)"
    for i, row in df.iterrows():
        match = re.search(pattern, row['Line'])
        if match:
            name = match.group(1)
            duration = match.group(2)
            t.append(df.at[i, 'Time'])
            n.append(name)
            d.append(int(duration))
            id.append(df.at[i, 'id'])

    return n, d, id, t

times = []
names = []
durations = []
ids = []

for path in paths:
    n, d, id, t = get_names_durations(path)
    names.extend(n)
    durations.extend(d)
    ids.extend(id)
    times.extend(t)

df = pd.DataFrame({'time': times, 'id': ids, 'account': names, 'duration': durations})
top_250 = df.sort_values('duration', ascending=False).head(250)
top_250.to_csv('top_250')