import csv

logFile = "logs.log"

with open(logFile, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)