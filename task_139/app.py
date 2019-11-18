from flask import Flask, request, render_template, json, jsonify
# //import requests
from flask_json import FlaskJSON, JsonError, json_response, as_json
from datetime import datetime


app = Flask(__name__)
json = FlaskJSON(app)


@app.route('/')
def index():
    return 'Server Workssssssssssss!'


@app.route('/bus/<line>')
def show_bus(line):
    return render_template('bus-lines.html', line=line)

##########nova funckia

@app.route('/spoje', methods=['GET', 'POST'])
def spoje():
    if request.method == 'POST':
        if request.is_json:
            key = request.json.get("show")
            # #return "JSON received", 200
            # #return jsonify(req)
            return jsonify(data[key])
        else:
            return "not a JSON", 400
    else:
        return "None"


data = {
    "busy": [
        {
            "id" : "1",
            "smer" : "sever",
            "cislo" : "11",
            "driver_id" : "125",
            "type" : "bus"
    },
    {
        "id" : "2",
        "smer" : "juh",
        "cislo" : "12",
        "driver_id" : "521",
        "type" : "bus"
    }
    ],
    "elektricky": [
        {
            "id" : "3",
            "smer" : "zapad",
            "cislo" : "5",
            "driver_id" : "64684",
            "type" : "elektricka"
        },
        {
            "id" : "4",
            "smer" : "vychod",
            "cislo" : "7",
            "driver_id" : "8852",
            "type" : "elektricka"
        }
    ]
}

#print(type(data))







