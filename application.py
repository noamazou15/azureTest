  
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    data='''[{
  "Project": "paksmas",
  "Site": "mamram",
  "TimeGenerate": "14:21",
  "severity": "moti is on fire",
  "ID":"207882622@idf.il"
},
 {
  "Project": "pakdfdfmas",
  "Site": "mafsafam",
  "TimeGenerate": "14sf1",
  "severity": "moti issfsf fire",
  "ID":"207882sfsf@idf.il"
}
 ]'''
    return data
