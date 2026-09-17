"""
Generates a report from the Online Examination System.
Run this in Jenkins to produce report.txt as a build artifact.
"""
import json
import os
from datetime import datetime

RESULTS_FILE = "results.json"

def generate_report():
    # Load existing results (or start empty)
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            results = json.load(f)
    else:
        # Demo data if no results exist yet
        results = [
            {"student": "Alice",   "score": 5, "total": 5, "percentage": 100.0,
             "status": "PASS", "date": "2026-09-10 10:00:00"},
            {"student": "Bob",     "score": 3, "total": 5, "percentage": 60.0,
             "status": "PASS", "date": "2026-09-10 10:05:00"},
            {"student": "Charlie", "score": 1, "total": 5, "percentage": 20.0,
             "status": "FAIL", "date": "2026-09-10 10:10:00"},
            {"student": "Dhruv", "score": 4, "total": 5, "percentage": 80.0,
             "status": "PASS", "date": "2026-09-10 10:15:00"},
            {"student": "Ezhil", "score": 4, "total": 5, "percentage": 80.0,
             "status": "PASS", "date": "2026-09-10 10:15:00"},
        ]

    total_students = len(results)
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = total_students - passed
    avg_percent = (sum(r["percentage"] for r in results) / total_students) if total_students else 0

    # Write the report
    with open("report.txt", "w") as f:
        f.write("Online Examination System - Report\n")
        f.write("=" * 40 + "\n")
        f.write(f"Generated On     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Students   : {total_students}\n")
        f.write(f"Passed           : {passed}\n")
        f.write(f"Failed           : {failed}\n")
        f.write(f"Average Percent  : {avg_percent:.2f}%\n")
        f.write("=" * 40 + "\n\n")
        f.write("Detailed Results:\n")
        f.write("-" * 40 + "\n")
        for r in results:
            f.write(f"{r['student']:<15} {r['score']}/{r['total']}  "
                    f"{r['percentage']:>6.2f}%  {r['status']}\n")

    print("Report generated: report.txt")

if __name__ == "__main__":
    generate_report()
