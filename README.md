# IOT Project: Team9
### By Crehul Vlad, Farcasan Darius and Hornai Vlad

## Following is an example on how the graph might look after some usage
![Imgur](https://i.imgur.com/7rIDZBw.jpg)

## Recieved/Input Data
### The `modbus_gw.ini` will have to be of this format:
```
[INPUT_REGISTERS]

REGISTER = 10,2,1020000000000061,2,129,5,0,0,0,2
REGISTER = 13,2,0022FF0000021F11,2,7,1,0,0,0,2

#[INPUT_REGISTERS]
#REGISTER = <start_addr>,<word_cnt>,<EUI64>,<TSAPID>,<ObjId>,<AttrId>,<Idx1>,<Idx2>,<MethId>,<status>
#REGISTER = <start_addr>,<word_cnt>,<EUI64>,<TSAPID>,<ObjId>,<AttrId>,<Idx1>,<Idx2>,<MethId>,<status>

#[HOLDING_REGISTERS]
#REGISTER = <start_addr>,<word_cnt>,<EUI64>,<TSAPID>,<ObjId>,<AttrId>,<Idx1>,<Idx2>,<MethId>,<status>
#REGISTER = <start_addr>,<word_cnt>,<EUI64>,<TSAPID>,<ObjId>,<AttrId>,<Idx1>,<Idx2>,<MethId>,<status>
```
### And the `Monitor_Host_Publisher.conf` will have this format:
```

[1020:0000:0000:0061]
#concentrator_info = CO_TSAP_ID, CO_ID, Data_Period, Data_Phase, Data_StaleLimit, Data_version, interfaceType
CONCENTRATOR = 2, 4, 15, 0, 5, 16, 2
#channel_info = TSAP_ID, ObjID, AttrID, Index1, Index2, format = {'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'float'}, name, unit of measurement, withStatus
CHANNEL = 2, 129, 5, 0, 0, 'float', '°C', 'degree Celsius', 0
CHANNEL = 2, 129, 6, 0, 0, 'float', 'Reserved', 'Manufacturer Specific', 0
CHANNEL = 2, 129, 7, 0, 0, 'float', 'Reserved', 'Manufacturer Specific', 0
CHANNEL = 2, 129, 8, 0, 0, 'float', 'Reserved', 'Manufacturer Specific', 0


[0022:FF00:0002:1F11]
#concentrator_info = CO_TSAP_ID, CO_ID, Data_Period, Data_Phase, Data_StaleLimit, Data_version, interfaceType
CONCENTRATOR = 2, 3, 10, 0, 5, 61, 1
#channel_info = TSAP_ID, ObjID, AttrID, Index1, Index2, format = {'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'float'}, name, unit of measurement, withStatus
CHANNEL = 2, 5, 1, 0, 0, 'float', '%', 'percent', 1
CHANNEL = 2, 6, 1, 0, 0, 'float', '%', 'percent', 1
CHANNEL = 2, 7, 1, 0, 0, 'float', '°C', 'degree Celsius', 1


[1060:0000:0000:0061]
#concentrator_info = CO_TSAP_ID, CO_ID, Data_Period, Data_Phase, Data_StaleLimit, Data_version, interfaceType
CONCENTRATOR = 2, 4, 60, 0, 5, 16, 2
#channel_info = TSAP_ID, ObjID, AttrID, Index1, Index2, format = {'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'float'}, name, unit of measurement, withStatus
CHANNEL = 2, 129, 5, 0, 0, 'float', '°C', 'degree Celsius', 0
CHANNEL = 2, 129, 6, 0, 0, 'float', '%', 'percent', 0
CHANNEL = 2, 129, 7, 0, 0, 'float', 'Reserved', 'Manufacturer Specific', 0
CHANNEL = 2, 129, 8, 0, 0, 'float', 'Reserved', 'Manufacturer Specific', 0
```

## Data Parsing
- We had to parse the data from `modbus_gw.in` and `Monitor_Host_Publisher.conf`
- Those will be saved after fetching new data into `\static\Modbus_Gw_File_Parsed.json`, respectivly `\static\Monitor_Host_Publisher_Parsed.json`
- The parsing is done by `Modbus_Gw_Parsed.py` and `Monitor_Host_Parsed.py`

Alongside the `conf` and `ini` file we had to parse the data coming from the modbus server.

- This data will be saved in `\static\pyModbus.json`
- The connection to the modbus server is done via `pyModbus.py`. This also handles the parsing

## Database
- The data from `\static\pyModbus.json` will be stored in a database via MongoDB and handled by PyMongo

## Backend
- The python scripts will be called by `backend.py` which is a web framework known as Flask. This will handle the webpage rendering and using the python programs.

## Frontend/Interface/Graph
- The data will be dispalyed on a web application
- The interface is handled by `\templates\Publisher_Display.html` This includes the HTML and JavaScript part. Also of note part of the styling is in `\static\css\chart.css`
- The page is rendered by the backend as mentioned above.
## This is a complete overview of the result
![Imgur](https://i.imgur.com/EC3pt18.jpg)