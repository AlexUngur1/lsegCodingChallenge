import csv
from datetime import datetime, timedelta
from collections import defaultdict

logFile = "logs.log"
output_path = "output.log"
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
    return jobs

def analyze_jobs(jobs, outfile):
    for pid, data in jobs.items():
        start = data.get("start")
        end = data.get("end")
        desc = data.get("desc", "N/A")

        if not start or not end:
            print(f"[MISSING] Job {pid} ({desc}) is missing {'start' if not start else 'end'} time.")
            continue

        duration = end - start
        # with open(output_path, "w") as outfile:
        if duration > errorLevel:
            print(f"[ERROR] Job {pid} ({desc}) took {duration}.")
            outfile.write(f"[ERROR] Job {pid} ({desc}) took {duration}.\n")
        elif duration > warningLevel:
            print(f"[WARNING] Job {pid} ({desc}) took {duration}.")
            outfile.write(f"[WARNING] Job {pid} ({desc}) took {duration}.\n")
        else:
            print(f"[OK] Job {pid} ({desc}) took {duration}.")
            outfile.write(f"[OK] Job {pid} ({desc}) took {duration}.\n")

jobs = parse_log(logFile)
with open(output_path, "w") as outfile:
    analyze_jobs(jobs, outfile)
