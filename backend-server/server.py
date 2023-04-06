import os
from flask import Flask, jsonify, request
from waitress import serve
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from SqliteDBMS import SqliteDatabaseManager as dbms
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

db_path = 'D:\\Computer Programming\\Programs\\HPE Hackathon\\hospital-appointment-hpe-hack\\backend-server\\database\\Doctor.db'

@app.route('/start_test', methods = ['GET'])
def test_func() -> dict:
    return {'Server is live:': True}

@app.route('/doctor_data', methods = ['GET'])
def get_doctor_data() -> dict:
    db_object = dbms(db_path)
    return db_object.get_data_dict(table_name="Doctor")

serve(app, host='0.0.0.0', port=8080)