import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import numpy as np
import re
import random

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


df = pd.DataFrame({'time': times, 'id': ids, 'account': names, 'duration': durations, 'thread': threads})
pick_2_top = df.sort_values('duration', ascending=False).head(100).sample(2)
print(pick_2_top)
pick_3_top = df.sort_values('duration', ascending=False).head(5000).sample(3)
print(pick_3_top)

print(top_250.head(1))
demo_accounts = df[df['account'].str.contains('demo', case=False, na=False)]
normal_accounts = df[~df['account'].str.contains('demo', case=False, na=False)].drop_duplicates(['account'])
normal_accounts['account'].to_csv('normal_accounts', index=False)
demo_accounts.sort_values(by=['duration'], ascending=False).to_csv('demo_accounts', index=False)
normal_accounts_num = len(normal_accounts)
demo_accounts_num = len(demo_accounts)
demo_accounts_duration = df[df['account'].str.contains('demo', case=False, na=False)]['duration'].sum()
normal_accounts_duration = df[~df['account'].str.contains('demo', case=False, na=False)]['duration'].sum()

# Data for the first pie chart
labels1 = ['Real tenants', 'Demo tenants']
sizes1 = [normal_accounts_num, demo_accounts_num]

# Data for the second pie chart
labels2 = ['Real tenants', 'Demo tenants']
sizes2_ms = [normal_accounts_duration, demo_accounts_duration]

# Calculate durations in hours
sizes2_hours = [duration_ms / (1000 * 60 * 60) for duration_ms in sizes2_ms]  # Convert ms to hours

labels1_combined = [f'{label}\n({sizes1[i]} tenants)' for i, label in enumerate(labels1)]
# Format labels to include both ms and hours
labels2_combined = [f'{label}\n({sizes2_hours[i]:.2f} hours)' for i, label in enumerate(labels2)]

# Create a figure with 2 subplots arranged horizontally
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot the first pie chart
ax1.pie(sizes1, labels=labels1_combined, autopct='%1.1f%%')
ax1.set_title('Tenants')

# Plot the second pie chart
ax2.pie(sizes2_ms, labels=labels2_combined, autopct='%1.1f%%')
ax2.set_title('Cron job durations')

plt.savefig('demo_tenant_distribution.png')
