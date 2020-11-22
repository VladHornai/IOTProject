
from pymodbus.client.sync import ModbusTcpClient
import logging
import json 
import Modbus_Gw_Parsed

# Opening JSON file 
filename = 'modbus_gw_file_parsed.json'

# Iterating through the json 
# list 
client = ModbusTcpClient('127.0.0.1', port=502)
client.connect()

with open(filename, 'r') as file:
    data = json.load(file)
    for obj in data: 
        startaddr = int(obj.get("start_addr", None).strip(" "))
        wordcnt = int(obj.get("word_cnt", None))
        reg = client.read_input_registers(startaddr,wordcnt)
        print(reg.registers)
            
client.close()
