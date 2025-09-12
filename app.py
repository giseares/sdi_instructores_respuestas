from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
CSV_FILE = 'intructores.txt'
FIELDNAMES = ['name', 'centerName', 'email', 'phone', 'location', 'timestamp', 'sessionId']

@app.route('/api/instructor', methods=['POST'])
def save_instructor():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data received'}), 400

    # Check if file exists to write header only once
    write_header = not os.path.exists(CSV_FILE)

    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow({key: data.get(key, '') for key in FIELDNAMES})

    return jsonify({'status': 'success', 'data': data}), 200

if __name__ == '__main__':
    app.run(debug=True)