from flask import Flask, render_template, jsonify
import Modbus_Gw_Parsed
import Monitor_Host_Parsed
#import pyModbus_Client

app = Flask(__name__)

@app.route('/')
def Publisher_Display():
        return render_template('Publisher_Display.html')

@app.route('/update/')
def update():
    print("Updated?")
        #Modbus_Gw_Parsed
        #Monitor_Host_Parsed
        #pyModbus_Client

if __name__ == '__main__':
  app.run()