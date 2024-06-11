import json
import datetime
import re
import matplotlib.pyplot as plt
import numpy as np

logs = open("data/eod_logs_job_only_cleaned_up.json")
logs_info = []
timestamps = []
date_format = "%Y-%m-%dT%H:%M:%S.%f%z"

# load logs as dictionaries and parse datetime
for log in logs:
    log_dict = json.loads(log)
    logs_info.append(log_dict)
    timestamps.append(datetime.datetime.strptime(log_dict['timestamp'], date_format))

durations = []
pattern = r'name=(.*?),.*?duration=PT(.*?),'

# parse time strings for duration of jobs to create datetime object
def parse_time_string(time_str):
    time_pattern = re.compile(
        r'(?:(?P<hours>\d+)H)?(?:(?P<minutes>\d+)M)?(?P<seconds>\d+(?:\.\d+)?)?S'
    )
    
    match = time_pattern.match(time_str)
    
    time_data = match.groupdict(default='0')
    hours = int(time_data['hours'])
    minutes = int(time_data['minutes'])
    seconds = float(time_data['seconds'])

    return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)

# create list of job names and durations of jobs
for log in logs_info:
    match = re.search(pattern, log['line'])
    if match:
        name = match.group(1)
        duration = match.group(2)
        result = {
            "name": name,
            "duration": parse_time_string(duration),}
        durations.append(result)

# Create figure with all job durations
# fig, ax = plt.subplots()
# for i in range(len(durations)):
#     y = durations[i]['duration'].total_seconds()
#     b = ax.bar(durations[i]['name'], y)
# plt.title("Duration of EOD processing per EOD job")
# fig.set_figheight(9)
# fig.set_figwidth(12)
# ax.set_yscale('log')
# ax.tick_params(labelrotation=12, labelsize=6)
# ax.set_xlabel('Job name')
# ax.set_ylabel('EOD processing time in seconds [s]')
# plt.show()

loan_accounts = 2371124
deposit_accounts = 6056048

# Filter the specific durations
filtered_durations = [
    duration for duration in durations 
    if duration['name'] in ['LOANS_JOB_RUN_ON_BACKGROUND_WORKER', 'DEPOSITS_JOB_RUN_ON_WORKERS']
]

# Convert durations to seconds
job_names = [duration['name'] for duration in filtered_durations]
processing_times = [duration['duration'].total_seconds() for duration in filtered_durations]
account_numbers = [loan_accounts if 'LOANS' in name else deposit_accounts for name in job_names]
avg_pt = [pt / na * 1000 for pt, na in zip(processing_times, account_numbers)]

# Create figure 1
fig, ax1 = plt.subplots(figsize=(16, 9))
width_x = 0.35
x = np.arange(len(job_names))  # X-axis positions for the groups

# Plotting the processing times
color = 'tab:blue'
ax1.set_xlabel('Job name')
ax1.set_ylabel('EOD processing time in seconds [s]', color=color)
bars1 = ax1.bar(x - width_x/2, processing_times, width_x, label='Processing Time', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Creating the second y-axis for average processing time per account
ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('Average processing time per account [ms]', color=color)
bars2 = ax2.bar(x + width_x/2, avg_pt, width_x, label='Avg Time/Account', color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Adding legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Adding values on top of the bars
def add_labels(bars, ax, scale=1):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}' if scale == 1 else f'{height/scale:.4f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
for i, (x_pos, num_accounts) in enumerate(zip(x, account_numbers)):
    ax1.annotate(f'Accounts: {["6.05 million", "2.37 million"][i]}', 
                 xy=(x_pos, max(processing_times[i], avg_pt[i] * 1000)), 
                 xytext=(0, 10),
                 textcoords="offset points",
                 ha='center', 
                 va='bottom', 
                 fontsize=10, 
                 color='black', 
                 weight='bold')

add_labels(bars1, ax1)
add_labels(bars2, ax2, scale=1)
ax1.set_xticks(x)
ax1.set_xticklabels(job_names)
fig.tight_layout()
plt.show()