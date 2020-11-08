import json
import re
from json import JSONEncoder


class Register:
    def __init__(self, start_addr, word_cnt, Eui64, Tsapid, ObjId, AttrId, Idx1, Idx2, MethId, status):
        self.start_addr = start_addr
        self.word_cnt = word_cnt
        self.Eui64 = Eui64
        self.Tsapid = Tsapid
        self.ObjId = ObjId
        self.AttrId = AttrId
        self.Idx1 = Idx1
        self.Idx2 = Idx2
        self.MethId = MethId
        self.status = status


class RegisterEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


filename = "Resources/modbus_gw.ini"


reg = []
regObj = {}

with open(filename, 'r') as file:
    for line in file:
        # list of registers
        if(line.startswith('REGISTER =')):
            regObj = Register(re.split(',|\n|=', line)[1],
                              re.split(',|\n|=', line)[2],
                              re.split(',|\n|=', line)[3],
                              re.split(',|\n|=', line)[4],
                              re.split(',|\n|=', line)[5],
                              re.split(',|\n|=', line)[6],
                              re.split(',|\n|=', line)[7],
                              re.split(',|\n|=', line)[8],
                              re.split(',|\n|=', line)[9],
                              re.split(',|\n|=', line)[10])
            reg.append(regObj)

        if not(line.startswith('\n') or line.startswith('#')):
            dataJSON = json.dumps(reg, indent=4, cls=RegisterEncoder)

out_file = open("modbus_gw_file_parsed.json", "w")
out_file.write(dataJSON)
out_file.close()
