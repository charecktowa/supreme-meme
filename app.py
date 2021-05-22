import flask
from flask import request, jsonify

import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return '''<h1> Bee Hack </h1>'''

@app.route('/api/v1/resources/devices/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory

    cur = conn.cursor()
    all_devices = cur.execute('SELECT * FROM devices;').fetchall()

    return jsonify(all_devices)

@app.route('/api/v1/resources/devices', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id_dev = query_parameters.get('id')
    ip = query_parameters.get('device_ip')
    campus = query_parameters.get('campus')
    division = query_parameters.get('division')
    location = query_parameters.get('device_location')

    query = "SELECT * FROM devices WHERE"
    to_filter = []

    if id_dev:
        query += ' id=? AND'
        to_filter.append(id_dev)
    
    if ip:
        query += ' device_ip=? AND'
        to_filter.append(ip)

    if campus:
        query += ' campus=? AND'
        to_filter.append(campus)

    if division:
        query += ' division=? AND'
        to_filter.append(division)

    if location:
        query += ' device_location=? AND'
        to_filter.append(location)

    if not (id_dev or ip or campus or division or location):
        pass

    query = query[:-4] + ';'

    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

if __name__ == '__main__':
    app.run(    )