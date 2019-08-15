from flask import Flask, jsonify, request, render_template
from db import sqliteDb

app = Flask(__name__)


@app.route('/output/predictions')
def predictions():
    accept_header = request.headers.get('Accept')

    predictions = sqliteDb().get_predictions()

    if 'application/json' in accept_header:
        return jsonify(predictions)
    elif 'text/html' in accept_header:
        columns = list(predictions[0].keys())

        rows = []
        for prediction in predictions:
            rows.append([*prediction.values()])

        return render_template('predictions.html', predictions=predictions, columns=columns, rows=rows)
    else:
        return("I'm sorry but support for that content type has not been implemented yet.")
