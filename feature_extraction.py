import json
import datetime
import re
import matplotlib.pyplot as plt

logs = open("data/eod_logs_job_only_cleaned_up.json")
logs_info = []
timestamps = []
date_format = "%Y-%m-%dT%H:%M:%S.%f%z"

for log in logs:
    log_dict = json.loads(log)
    logs_info.append(log_dict)
    timestamps.append(datetime.datetime.strptime(log_dict['timestamp'], date_format))

durations = []
pattern = r'name=(.*?),.*?duration=PT(.*?),'

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

new_patt = r"INFO.*?\[([^]]+)] .*?total number of batches is (\d+), and total number of accounts is (\d+)"
for log in logs_info:
    match = re.search(pattern, log['line'])
    if match:
        name = match.group(1)
        duration = match.group(2)
        result = {
            "name": name,
            "duration": parse_time_string(duration),}
        durations.append(result)
    new_match = re.search(new_patt, log['line'])
    if new_match:
        print(new_match.group(1))    

# plt.figure(figsize=(16,9))
# plt.title("Duration of EOD processing per EOD job")
# plt.xlabel("Job name")
# plt.ylabel("EOD processing time in seconds [s]")
# plt.bar([duration['name'][:9] for duration in durations], [durations[i]['duration'].total_seconds() for i in range(len(durations))])
# plt.xticks(rotation=45, fontsize=6)
# plt.show()