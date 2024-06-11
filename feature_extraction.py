import json
import datetime
import re
import matplotlib.pyplot as plt

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

fig, ax = plt.subplots()
for i in range(len(durations)):
    y = durations[i]['duration'].total_seconds()
    b = ax.bar(durations[i]['name'][:9], y)
plt.title("Duration of EOD processing per EOD job")
fig.set_figheight(6)
fig.set_figwidth(12)
ax.set_yscale('log')
ax.set_xlabel('Job name')
ax.set_ylabel('EOD processing time in seconds [s]')
plt.show()

loan_accounts = 0
deposit_accounts = 0

# Filter the specific durations
filtered_durations = [
    duration for duration in durations 
    if duration['name'] in ['LOANS_JOB_RUN_ON_BACKGROUND_WORKER', 'DEPOSITS_JOB_RUN_ON_WORKERS']
]

# Convert durations to seconds
job_names = [duration['name'] for duration in filtered_durations]
processing_times = [duration['duration'].total_seconds() for duration in filtered_durations]
account_numbers = [loan_accounts if 'LOANS' in name else deposit_accounts for name in job_names]

# Create figure 1
fig, ax1 = plt.subplots(figsize=(16, 9))

color = 'tab:blue'
ax1.set_xlabel('Job name')
ax1.set_ylabel('EOD processing time in seconds [s]', color=color)
ax1.bar(job_names, processing_times, color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Number of Accounts', color=color)
ax2.plot(job_names, account_numbers, color=color, marker='o', ms='10', linestyle='none')
ax2.tick_params(axis='y', labelcolor=color)
plt.show()