from flask import Flask, render_template, jsonify
<<<<<<< HEAD
<<<<<<< HEAD
import json
import Modbus_Gw_Parsed
import Monitor_Host_Parsed
import pyModbus_Client

app = Flask(__name__)


=======
=======
>>>>>>> da7bcc1f62a912886e4eb58e8311a826649a023d
import Modbus_Gw_Parsed
import Monitor_Host_Parsed
#import pyModbus_Client

app = Flask(__name__)

<<<<<<< HEAD
>>>>>>> da7bcc1 (server commit)
=======
>>>>>>> da7bcc1f62a912886e4eb58e8311a826649a023d
@app.route('/')
def Publisher_Display():
        return render_template('Publisher_Display.html')

<<<<<<< HEAD
<<<<<<< HEAD
@app.route('/update')
def update():
    Modbus_Gw_Parsed.runGw()
    Monitor_Host_Parsed.runHost()
    #pyModbus_Client.runMod()
    return render_template('Publisher_Display.html')
    
if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
=======
=======
>>>>>>> da7bcc1f62a912886e4eb58e8311a826649a023d
@app.route('/update/')
def update():
    print("Updated?")
        #Modbus_Gw_Parsed
        #Monitor_Host_Parsed
        #pyModbus_Client

if __name__ == '__main__':
<<<<<<< HEAD
>>>>>>> da7bcc1 (server commit)
=======
>>>>>>> da7bcc1f62a912886e4eb58e8311a826649a023d
  app.run()