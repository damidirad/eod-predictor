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
    th = []
    d = []
    id = []

    pattern = r"INFO\s*\[(.*?)\].*(eod-thread-\d+).*duration: (\d*)"
    for i, row in df.iterrows():
        match = re.search(pattern, row['Line'])
        if match:
            name = match.group(1)
            thread = match.group(2)
            duration = match.group(3)
            t.append(df.at[i, 'Time'])
            th.append(thread)
            n.append(name)
            d.append(int(duration))
            id.append(df.at[i, 'id'])

    return n, d, id, t, th

times = []
names = []
durations = []
ids = []
threads = []

for path in paths:
    n, d, id, t, th = get_names_durations(path)
    names.extend(n)
    durations.extend(d)
    ids.extend(id)
    times.extend(t)
    threads.extend(th)

df = pd.DataFrame({'time': times, 'id': ids, 'account': names, 'duration': durations, 'thread': threads})
top_250 = df.sort_values('duration', ascending=False).head(250)
top_250.to_csv('top_250')

bottom_250 = df.sort_values('duration', ascending=True).head(250)
bottom_250.to_csv('bottom_250')

print(df[df['account'].str.contains('demo', case=False, na=False)]['duration'].sum())

for name in ['sonae', 'camesa', 'onmo', 'ascendnano']:
    tenant = df[df['account'] == name]
    job_count = tenant.shape[0]
    tenant['duration'] = tenant['duration'].apply(lambda x: x/3600000)
    max_duration = tenant['duration'].max()
    min_duration = tenant['duration'].min()
    plot = tenant.plot(x='time', y='duration', kind='scatter',
                       title=f"{job_count} EOD job run times for '{name}' during period of 8 days\n"
                             f"maximum duration: {max_duration} --- minimum duration: {min_duration}")
    plt.xticks([])
    plot.set(xlabel='time period of 8 days')
    plot.set(ylabel='duration of job in hours')
    plot.set_title(f"{job_count} EOD job run times for '{name}' during period of 8 days \n "
                             f"max. duration: {max_duration:.3f} hrs --- min. duration: {min_duration:.3f} hrs",
                   wrap=True)
    # plt.show()
    plt.savefig(f'{name}_run_times.png')
