import csv
from datetime import datetime, timedelta
from collections import defaultdict

logFile = "logs.log"
warningLevel = timedelta(minutes=5)
errorLevel = timedelta(minutes=10)

def parse_log(file_path):
    jobs = defaultdict(dict)  
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            time_str, desc, status, pid = [item.strip() for item in row]
            timestamp = datetime.strptime(time_str, "%H:%M:%S")
            if status == "START":
                jobs[pid]["start"] = timestamp
                jobs[pid]["desc"] = desc
            elif status == "END":
                jobs[pid]["end"] = timestamp
    print(jobs)
    return jobs


jobs = parse_log(logFile)
