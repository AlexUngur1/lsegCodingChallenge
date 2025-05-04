# import unittest
# from io import StringIO
# import csv
# from datetime import datetime, timedelta
# from collections import defaultdict

# # Core logic extracted to a function
# def process_log_file(file_obj):
#     jobs = defaultdict(dict)
#     reader = csv.reader(file_obj)
#     for row in reader:
#         time_str, desc, status, pid = [item.strip() for item in row]
#         timestamp = datetime.strptime(time_str, "%H:%M:%S")
#         if status == "START":
#             jobs[pid]["start"] = timestamp
#             jobs[pid]["desc"] = desc
#         elif status == "END":
#             jobs[pid]["end"] = timestamp

#     results = []

#     for pid, data in jobs.items():
#         start = data.get("start")
#         end = data.get("end")
#         desc = data.get("desc", "N/A")

#         if not start or not end:
#             results.append(f"[MISSING] Job {pid} ({desc}) is missing {'start' if not start else 'end'} time.")
#             continue

#         duration = end - start
#         if duration > timedelta(minutes=10):
#             results.append(f"[ERROR] Job {pid} ({desc}) took {duration}.")
#         elif duration > timedelta(minutes=5):
#             results.append(f"[WARNING] Job {pid} ({desc}) took {duration}.")
#         else:
#             results.append(f"[OK] Job {pid} ({desc}) took {duration}.")
#     return results

# # Test suite
# class TestLogMonitor(unittest.TestCase):
#     def test_log_parsing(self):
#         test_log = StringIO("""\
# 10:00:00, Test Job A, START, 123
# 10:05:01, Test Job A, END, 123
# 10:00:00, Test Job B, START, 456
# 10:11:00, Test Job B, END, 456
# 10:00:00, Test Job C, START, 789
# 10:03:00, Test Job C, END, 789
# 10:00:00, Test Job D, START, 999
# """)
#         expected = [
#             "[WARNING] Job 123 (Test Job A) took 0:05:01.",
#             "[ERROR] Job 456 (Test Job B) took 0:11:00.",
#             "[OK] Job 789 (Test Job C) took 0:03:00.",
#             "[MISSING] Job 999 (Test Job D) is missing end time."
#         ]

#         actual = process_log_file(test_log)
#         self.assertEqual(sorted(actual), sorted(expected))

# unittest.main()
