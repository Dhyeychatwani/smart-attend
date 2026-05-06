"""
utils.py
--------
Shared utility functions for SmartAttend.
"""

import os
import csv
import datetime

LOGS_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'attendance_logs')


def get_today_log_path():
    """Return the CSV file path for today's attendance log."""
    os.makedirs(LOGS_DIR, exist_ok=True)
    today = datetime.date.today().strftime('%Y-%m-%d')
    return os.path.join(LOGS_DIR, f'attendance_{today}.csv')


def load_today_attendance():
    """Return a set of names already marked present today."""
    log_path = get_today_log_path()
    marked = set()
    if os.path.exists(log_path):
        with open(log_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                marked.add(row['Name'])
    return marked


def mark_attendance(name: str):
    """
    Mark a student as present in today's CSV log.
    Avoids duplicate entries for the same student on the same day.

    Returns True if newly marked, False if already marked.
    """
    marked = load_today_attendance()
    if name in marked:
        return False  # Already marked today

    log_path = get_today_log_path()
    file_exists = os.path.exists(log_path)
    now = datetime.datetime.now()

    with open(log_path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Date', 'Time'])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'Name': name,
            'Date': now.strftime('%Y-%m-%d'),
            'Time': now.strftime('%H:%M:%S'),
        })

    return True


def get_all_logs():
    """
    Return a list of all attendance records across all log files.
    Each record is a dict with keys: Name, Date, Time.
    """
    records = []
    if not os.path.exists(LOGS_DIR):
        return records

    for filename in sorted(os.listdir(LOGS_DIR), reverse=True):
        if filename.endswith('.csv'):
            filepath = os.path.join(LOGS_DIR, filename)
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    records.append(row)

    return records


def get_available_dates():
    """Return a list of dates (strings) for which logs exist."""
    if not os.path.exists(LOGS_DIR):
        return []
    dates = []
    for filename in sorted(os.listdir(LOGS_DIR), reverse=True):
        if filename.startswith('attendance_') and filename.endswith('.csv'):
            date_str = filename.replace('attendance_', '').replace('.csv', '')
            dates.append(date_str)
    return dates
