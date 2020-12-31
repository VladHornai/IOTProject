from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
import json
import Modbus_Gw_Parsed
import Monitor_Host_Parsed
import pyModbus_Client
import DB_Modbus

app = Flask(__name__)

title = "IOT Project"

client = MongoClient(DB_Modbus.URL_MONGO)
db = client.IOT_Modbus_DB
col = db.IOT_Modbus_Coll
Reg1 = []
Reg2 = []

for x in col.find({ "Register": "1020000000000061" },{"_id": 0}):
  Reg1.append(x)
for x in col.find({ "Register": "0022FF0000021F11" },{"_id": 0}):
  Reg2.append(x)

d1 = [[],[],[],[],[]]

d1[0].append(Reg1[0]["Register"])
for i in range(len(Reg1)):
  d1[1].append(Reg1[i]["Time"])
  d1[2].append(Reg1[i]["Type"])
  d1[3].append(Reg1[i]["Value"])
  d1[4].append(Reg1[i]["Status"])

d2 = [[],[],[],[],[]]

d2[0].append(Reg2[0]["Register"])
for i in range(len(Reg2)):
  d2[1].append(Reg2[i]["Time"])
  d2[2].append(Reg2[i]["Type"])
  d2[3].append(Reg2[i]["Value"])
  d2[4].append(Reg2[i]["Status"])

@app.route('/')
def Publisher_Display():
        return render_template('Publisher_Display.html', Data1 = d1, Data2 = d2, t = title)

@app.route('/update')
def update():
    Modbus_Gw_Parsed.runGw()
    Monitor_Host_Parsed.runHost()
    pyModbus_Client.runMod()
    DB_Modbus.Create_Db()

    Reg1 = []
    Reg2 = []

    for x in col.find({ "Register": "1020000000000061" },{"_id": 0}):
      Reg1.append(x)
    for x in col.find({ "Register": "0022FF0000021F11" },{"_id": 0}):
      Reg2.append(x)

    d1 = [[],[],[],[],[]]

    d1[0].append(Reg1[0]["Register"])
    for i in range(len(Reg1)):
      d1[1].append(Reg1[i]["Time"])
      d1[2].append(Reg1[i]["Type"])
      d1[3].append(Reg1[i]["Value"])
      d1[4].append(Reg1[i]["Status"])

    d2 = [[],[],[],[],[]]

    d2[0].append(Reg2[0]["Register"])
    for i in range(len(Reg2)):
      d2[1].append(Reg2[i]["Time"])
      d2[2].append(Reg2[i]["Type"])
      d2[3].append(Reg2[i]["Value"])
      d2[4].append(Reg2[i]["Status"])
  
    return render_template('Publisher_Display.html', Data1 = d1, Data2 = d2, t = title)
    
if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
  app.run()