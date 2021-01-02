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
file_GW = 'static/modbus_gw_file_parsed.json'

client = MongoClient(DB_Modbus.URL_MONGO)
db = client.IOT_Modbus_DB
col = db.IOT_Modbus_Coll
ips = []

with open(file_GW, 'r') as file:
        data = json.load(file)
        for obj in data:
            ip = obj.get("Eui64", None)
            ips.append(ip)

Reg = [ [] for x in range(len(ips)) ]

for i in range(len(ips)):
  for x in col.find({ "Register": ips[i] },{"_id": 0}):
    Reg[i].append(x)

d = [[ [],[],[],[],[] ] for x in range(len(Reg))]

for i in range(len(Reg)):
  for j in range(len(Reg[i])):
    d[i][0].append(Reg[i][j]["Time"])
    d[i][1].append(Reg[i][j]["Type"])
    d[i][2].append(Reg[i][j]["Value"])
    d[i][3].append(Reg[i][j]["Status"])
    d[i][4].append(Reg[i][j]["Register"])

@app.route('/')
def Publisher_Display():
        return render_template('Publisher_Display.html', Data = d, t = title)

@app.route('/update')
def update():
  Modbus_Gw_Parsed.runGw()
  Monitor_Host_Parsed.runHost()
  pyModbus_Client.runMod()
  DB_Modbus.Create_Db()

  Reg = [ [] for x in range(len(ips)) ]

  for i in range(len(ips)):
   for x in col.find({ "Register": ips[i] },{"_id": 0}):
     Reg[i].append(x)
  
   d = [[ [],[],[],[],[] ] for x in range(len(Reg))]

  for i in range(len(Reg)):
   for j in range(len(Reg[i])):
     d[i][0].append(Reg[i][j]["Time"])
     d[i][1].append(Reg[i][j]["Type"])
     d[i][2].append(Reg[i][j]["Value"])
     d[i][3].append(Reg[i][j]["Status"])
     d[i][4].append(Reg[i][j]["Register"])
  
  return render_template('Publisher_Display.html', Data = d, t = title)
    
if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
  app.run()