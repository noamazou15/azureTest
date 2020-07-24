  
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    data='''{
  "Project": "paksmas",
  "Site": "mamram",
  "TimeGenerate": "14:21",
  "severity": "moti is on fire"
}'''
    return data
