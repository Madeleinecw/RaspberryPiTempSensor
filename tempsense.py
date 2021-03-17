import time
from w1thermsensor import W1ThermSensor
from datetime import datetime

sensor = W1ThermSensor() 


while True:
    temperature = sensor.get_temperature()
    timeNow = datetime.now().time().replace(microsecond=0)
    print("At %s the temperature is %s celsius" % (timeNow, temperature))
    time.sleep(2)