import json
import re
from json import JSONEncoder

class IP:
    # takes coresponding parameters
    def __init__(self, concentrator, channel):
        self.concentrator = concentrator # concentrator
        self.channel = channel # channel list

class Concentrator:
    def __init__(self, co_tsap_id, co_id, data_period, data_phase, data_stalelimit, data_version, interface_type):
        self.co_tsap_id = co_tsap_id
        self.co_id = co_id
        self.data_period = data_period
        self.data_phase = data_phase
        self.data_stalelimit = data_stalelimit
        self.data_version = data_version
        self.interface_type = interface_type

class Channel:
    # takes coresponding parameters
    def __init__(self, tsap_id, ObjID, AttrID, Index1, Index2, Format, name, unit_of_measurement, withStatus):
        self.tsap_id = tsap_id
        self.ObjID = ObjID
        self.AttrID = AttrID
        self.Index1 = Index1
        self.Index2 = Index2
        self.Format = Format
        self.name = name
        self.unit_of_measurement = unit_of_measurement
        self.withStatus = withStatus


class IPEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


filename = "Resources/Monitor_Host_Publishers.conf"

# fields in our file
#fields = ['CO_TSAP_ID', 'CO_ID', 'Data_Period', 'Data_Phase', 'Data_StaleLimit', 'Data_version', 'interfaceType']
#channel_info = TSAP_ID, ObjID, AttrID, Index1, Index2, format = {'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'float'}, name, unit of measurement, withStatus

data_chunk = {}
ip = ''
concentrator = {}
chObj = {}
channel = []

with open(filename,'r') as file:
    for line in file:     
        # extracts ip
        if(line.startswith('[')):
            ip = re.split(r'CONCENTRATOR |\n |\]', line)[0]
            ip = ip.replace('[', '')
            channel = []

        # list of channels
        if(line.startswith('CHANNEL =')):
            chObj = Channel(re.split(', |\n|=', line)[1],    # TSAP_ID
                            re.split(', |\n|=', line)[2],    # ObjID
                            re.split(', |\n|=', line)[3],    # AttrID
                            re.split(', |\n|=', line)[4],    # Index1
                            re.split(', |\n|=', line)[5],    # Index2
                            re.split(', |\n|=', line)[6],    # format
                            re.split(', |\n|=', line)[7],    # name
                            re.split(', |\n|=', line)[8],    # unit of measurement
                            re.split(', |\n|=', line)[9])    # withStatus
            channel.append(chObj)
            
        if(line.startswith('CONCENTRATOR =')):
            concentrator = Concentrator(re.split(', |\n|=', line)[1],    # CO_TSAP_ID
                                        re.split(', |\n|=', line)[2],    # CO_ID
                                        re.split(', |\n|=', line)[3],    # Data_Period
                                        re.split(', |\n|=', line)[4],    # Data_Phase
                                        re.split(', |\n|=', line)[5],    # Data_StaleLimit
                                        re.split(', |\n|=', line)[6],    # Data_version
                                        re.split(', |\n|=', line)[7])    # interfaceType
        
        if not(line.startswith('\n') or line.startswith('#')):
            data_chunk[ip] = IP(concentrator, channel)
            dataJSON = json.dumps(data_chunk, indent=4, cls=IPEncoder)

out_file = open("parsedFile.json", "w")
out_file.write(dataJSON)
out_file.close()