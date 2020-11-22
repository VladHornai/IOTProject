
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging
import json 
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

UNIT = 0x1

# Opening JSON file 
filename = 'modbus_gw_file_parsed.json'

# Iterating through the json 
# list 
client = ModbusClient('127.0.0.1', port=502)
client.connect()

with open(filename, 'r') as file:
    data = json.load(file)
    for obj in data: 
        #for key, value in obj.items():
        startaddr = int(obj.get("start_addr", None).strip(" "))
        wordcnt = int(obj.get("word_cnt",None))
        rr = client.read_input_registers(startaddr, wordcnt, unit=UNIT)
        print(rr)
        #print(startaddr, type(wordcnt))
        
client.close()
