from flask import Flask, jsonify, request, render_template
from db import sqliteDb
from config import *

from datetime import datetime

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


def get_now():
    return datetime.now()


def get_moment_last_spray():
    spray_moments = list(sqliteDb().get_spray_moments())

    # we assume the last record in the database is the latest
    moment_last_spray = spray_moments[len(spray_moments) - 1]

    format = '%Y-%m-%d %H:%M:%S'
    return(datetime.strptime(moment_last_spray, format))


def get_days_since_last_spray():
    time_since_last_spray = get_now() - get_moment_last_spray()

    days_since_last_spray = time_since_last_spray.days
    return days_since_last_spray


@app.route('/spray')
def spray():
    # check if any of the predictions exceeds the prediction percentage
    # predictions = sqliteDb().get_predictions()
    # for prediction in predictions:
    #     print(prediction)

    # check if the vineyard was sprayed recently
    print(get_days_since_last_spray())

    # both requirements are checked
    recently_sprayed = False
    prediction_over_threshold = True

    if prediction_over_threshold and not recently_sprayed:
        return jsonify(True)
