"""
app.py
------
Flask web dashboard for SmartAttend.
View attendance logs, filter by date, export CSV.

Usage:
    python src/app.py
    Open: http://localhost:5000
"""

import os
import sys
import csv
import io

sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, render_template, request, Response, jsonify
from utils import get_all_logs, get_available_dates, mark_attendance

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'),
)


@app.route('/')
def dashboard():
    date_filter = request.args.get('date', '')
    all_records = get_all_logs()
    dates       = get_available_dates()

    if date_filter:
        records = [r for r in all_records if r.get('Date') == date_filter]
    else:
        records = all_records

    return render_template(
        'dashboard.html',
        records=records,
        dates=dates,
        selected_date=date_filter,
        total=len(records),
    )


@app.route('/api/logs')
def api_logs():
    """JSON API endpoint for attendance records."""
    date_filter = request.args.get('date', '')
    all_records = get_all_logs()
    if date_filter:
        records = [r for r in all_records if r.get('Date') == date_filter]
    else:
        records = all_records
    return jsonify(records)


@app.route('/export')
def export_csv():
    """Export attendance as downloadable CSV."""
    date_filter = request.args.get('date', '')
    all_records = get_all_logs()
    if date_filter:
        records = [r for r in all_records if r.get('Date') == date_filter]
    else:
        records = all_records

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['Name', 'Date', 'Time'])
    writer.writeheader()
    writer.writerows(records)

    filename = f"attendance_{date_filter or 'all'}.csv"
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
