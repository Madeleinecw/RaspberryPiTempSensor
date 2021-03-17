import time
from w1thermsensor import W1ThermSensor
from datetime import datetime
from flask import Flask
app = Flask(__name__)

sensor = W1ThermSensor() 

@app.route('/')
def hello_world():
    temperature = sensor.get_temperature()
    timeNow = datetime.now().time().replace(microsecond=0)
    return"At %s the temperature is %s celsius" % (timeNow, temperature)