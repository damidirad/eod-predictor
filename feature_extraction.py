import json
import datetime
import re

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
for log in logs_info:
    match = re.search(pattern, log['line'])
    if match:
        name = match.group(1)
        duration = match.group(2)
        result = {
            "name": name,
            "duration": duration,}
        durations.append(result)
