import json
import re
from json import JSONEncoder


class IP:
    def __init__(self,co_tsap_id, co_id, data_period, data_phase, data_stalelimit, data_version, interface_type, ): #takes coresponding parameters
        self.co_tsap_id = co_tsap_id
        self.co_id = co_id
        self.data_period = data_period
        self.data_phase = data_phase
        self.data_stalelimit = data_stalelimit
        self.data_version = data_version
        self.interface_type = interface_type
        self.channel = []

class IPEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

filename = "Resources/Monitor_Host_Publishers.conf"

#fields in our file
#fields = ['CO_TSAP_ID', 'CO_ID', 'Data_Period', 'Data_Phase', 'Data_StaleLimit', 'Data_version', 'interfaceType']

concentrator = {}

with open(filename) as file:
    for line in file:
        #read line by line the file
        description = list(line.strip().split(None, 4))

        description = ''.join(line for line in file if not line.startswith('#')) #skip comments and creates string for file

        #extracts ip
        ip = re.split(r'CONCENTRATOR |\n |\]',description)[0]
        ip = ip.replace('[','')
        
        concentrator[ip] = IP(re.split(', |\n|=',description)[2],   # CO_TSAP_ID
                              re.split(', |\n|=',description)[3],   # CO_ID
                              re.split(', |\n|=',description)[4],   # Data_Period
                              re.split(', |\n|=',description)[5],   # Data_Phase
                              re.split(', |\n|=',description)[6],   # Data_StaleLimit
                              re.split(', |\n|=',description)[7],   # Data_version
                              re.split(', |\n|=',description)[8])   # interfaceType
        
        
        
        dataJSON = json.dumps(concentrator, indent = 4, cls=IPEncoder)
        out_file = open("parsedFile.json", "w")
        out_file.write(dataJSON)
        out_file.close()