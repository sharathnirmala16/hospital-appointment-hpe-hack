import os
from flask import Flask, jsonify, request
from waitress import serve
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from SqliteDBMS import SqliteDatabaseManager as dbms
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route('/start_test', methods = ['GET'])
def test_func() -> dict:
    return {'Server is live:': True}

serve(app, host='0.0.0.0', port=8080)