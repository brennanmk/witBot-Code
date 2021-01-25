from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
import interfaces.setMotorPower as motorControl
import interfaces.lineSensor as lineSensor
import interfaces.distanceSensor as distanceSensor
import interfaces.bot_config as config
import threading
import time

# Setup flask app
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
motorControl.init()

running = True

# Setup bot components
lineSensor.init(config.PINS['line/sense'])
lineValue = lineSensor.read()

distanceSensor.init(config.PINS['ultrasonic/trigger'],config.PINS['ultrasonic/echo'])
distValue = distanceSensor.read_cm()

def updateSensor():
              global lineValue,distValue

              print('start of thread')
              while running: # global variable to stop loop
                            lineValue = lineSensor.read()
                            distValue = distanceSensor.read_cm()
                            time.sleep(1)
              print('stop of thread')
              
@app.route("/")
def indexRefresh(device=None, action=None):
              threading.Thread(target=updateSensor).start()
              return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def index():
              if request.method == 'POST':
                            if request.form.get('Forward') == 'Forward':
                                          motorControl.set("LEFT",100)
                                          motorControl.set("RIGHT",100)
                                          print("Motor Forward")
                            elif  request.form.get('Stop') == 'Stop':
                                          motorControl.set("LEFT",0)
                                          motorControl.set("RIGHT",0)
                                          print("Motor Stop")
                            elif request.form.get('Backwards') == 'Backwards':
                                          motorControl.set("LEFT",-100)
                                          motorControl.set("RIGHT",-100)
                                          print("Motor Back")
                            elif request.form.get("Left")==("Left"):
                                          motorControl.set("LEFT",-100)
                                          motorControl.set("RIGHT",100)
                                          print("Motor Left")
                            elif request.form.get("Right")==("Right"):
                                          motorControl.set("LEFT",100)
                                          motorControl.set("RIGHT",-100)
                                          print("Motor Right")
                            else:
                                          return render_template('index.html')

              elif request.method == 'GET':
                            print("No Post Back Call")
              return render_template('index.html')


@app.route('/update', methods=['POST'])
def update():
              return jsonify({
                            'title': 'Sensor Values',
                            'lineValue': lineValue,'distValue':distValue
                            })
if __name__ == '__main__':
              app.run(host='0.0.0.0')