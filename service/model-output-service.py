from flask import Flask, jsonify, request
from db import sqliteDb

app = Flask(__name__)


@app.route('/output/predictions')
def predictions():
    accept_header = request.headers.get('Accept')
    if 'application/json' in accept_header:
        records = sqliteDb().get_predictions()
        return jsonify(records)
    elif 'text/html' in accept_header:
        return('html')
    else:
        return("I'm sorry but support for that content type has not been implemented yet.")
