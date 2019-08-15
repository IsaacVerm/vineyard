from flask import Flask, escape, request
from db import sqliteDb

app = Flask(__name__)

@app.route('/')
def output_model_records():
    records = sqliteDb().get_output_model_records()
    return str(records)
