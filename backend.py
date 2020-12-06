from flask import Flask, render_template, jsonify
import json
import Modbus_Gw_Parsed
import Monitor_Host_Parsed
import pyModbus_Client

app = Flask(__name__)


@app.route('/')
def Publisher_Display():
        return render_template('Publisher_Display.html')

@app.route('/update')
def update():
    Modbus_Gw_Parsed.runGw()
    Monitor_Host_Parsed.runHost()
    #pyModbus_Client.runMod()
    return render_template('Publisher_Display.html')
    
if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
  app.run()