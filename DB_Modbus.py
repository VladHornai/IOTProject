import pymongo
from datetime import datetime
import json

# Change each time
URL_MONGO = "mongodb://127.0.0.1:49689/82ec598c-450d-4274-bf9e-75d25dcae2be?"
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

myclient = pymongo.MongoClient(URL_MONGO) 
mydb = myclient["IOT_Modbus_DB"]
mycol = mydb["IOT_Modbus_Coll"]

file_GW = 'static/modbus_gw_file_parsed.json'
file_MB = 'static/pyModbus.json'

def Create_Db():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ips = []

    with open(file_GW, 'r') as file:
        data = json.load(file)
        for obj in data:
            ip = obj.get("Eui64", None)
            ips.append(ip)

    resps = []
    with open(file_MB, 'r') as file:
        data = json.load(file)
        for obj in data:
            resp = data[obj].get("response")
            resps.append(resp)

    dict_arr = []
    for i in range(len(resps)):
        dict = {"Register" : ips[i], "Time" : current_time, "Type" : "Celsius", "Value" : resps[i][0], "Status" : resps[i][1]}
        dict_arr.append(dict)

    x = mycol.insert_many(dict_arr)
    print("Database Created/Updated!")   

Create_Db()