from flask import Flask, request, render_template, json
# //import requests
from flask_json import FlaskJSON, JsonError, json_response, as_json
from datetime import datetime


app = Flask(__name__)
json = FlaskJSON(app)

@json.encoder
def custom_encoder(o):
    pass


@app.route('/')
def index():
    return 'Server Workssssssssssss!'


@app.route('/gettime')
def gettime():
    now = datetime.utcnow()
    return json_response(time=now)
    # return type(now)


@app.route('/bus/<line>')
def show_bus(line):
    return render_template('bus-lines.html', line=line)





