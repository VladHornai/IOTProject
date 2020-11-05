import json
from json import JSONEncoder


class IP:
    def __init__(self,name): 
        self.name = name
    
    def concentrator(self,co_tsap_id, co_id, data_period, data_phase, data_stalelimit, data_version, interface_type):
        self.co_tsap_id = co_tsap_id
        self.co_id = co_id
        self.data_period = data_period
        self.data_phase = data_phase
        self.data_stalelimit = data_stalelimit
        self.data_version = data_version
        self.interface_type = interface_type

class IPEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

filename = "Resources/Monitor_Host_Publishers.conf"

#fields in our file
#fields = ['CO_TSAP_ID', 'CO_ID', 'Data_Period', 'Data_Phase', 'Data_StaleLimit', 'Data_version', 'interfaceType']

with open(filename) as file:
    for line in file:
        #read line by line the file
        description = list(line.strip().split(None, 4))

        #delete comments 
        description = ''.join(line for line in file if not line.startswith('#'))
        #print(description)

        #put the ip in place

        ip = description.split('CONCENTRATOR')[0]
        
        if description.startswith('['):
            print("yes")
            data = IP(description)
           
        #we deal with the data of concentrator
        print("--------")
        print(description.split('CONCENTRATOR')[0])
        print("----")
       
        if description.startswith('C'): 

            description.split('=')
         
            data = IP.concentrator(description.split(',')[0], description.split(',')[1], description.split(',')[2], description.split(',')[3],
                                        description.split(',')[4], description.split(',')[5], description.split(',')[6])
        
        
        print(IPEncoder().encode(data))
        dataJSON = json.dumps(data, indent = 4, cls=IPEncoder)
        out_file = open("parsedFile.json", "w")
        print(dataJSON)
        out_file.close()


#json.dump(dict1, out_file, indent = 4)

