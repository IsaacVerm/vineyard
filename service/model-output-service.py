import mysql.connector
from flask import Flask, escape, request

app = Flask(__name__)


cnx = mysql.connector.connect(user='root',
                              host='localhost',
                              database='vineyard')

cursor = cnx.cursor()

query = ("SELECT * FROM output_model")
cursor.execute(query)

for (moment) in cursor:
    print(moment)

cnx.close()


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
