# lsegCodingChallenge
repo for lseg coding challenge

# Log Monitoring Application

This is a Python-based log monitoring tool designed to process and analyze job execution times from a CSV log file. It identifies jobs that exceed defined time thresholds and logs warnings or errors accordingly.

## Features

- Parses a CSV log file with job execution events (`START` / `END`)
- Tracks job duration based on start and end timestamps
- Generates:
  - `[OK]` for jobs under 5 minutes
  - `[WARNING]` for jobs over 5 minutes
  - `[ERROR]` for jobs over 10 minutes
  - `[MISSING]` for jobs missing a start or end time
- Writes output to a `.log` file and prints results to the console
- Validates output against an expected result using `filecmp`

