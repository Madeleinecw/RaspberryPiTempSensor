import time
from w1thermsensor import W1ThermSensor
from datetime import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@socketio.on('my event')
def test_message(message):
        emit('my response', {'data': 'got it!'})

sensor = W1ThermSensor() 


@app.route('/')
def hello_world():
    temperature = sensor.get_temperature()
    timeNow = datetime.now().time().replace(microsecond=0)
    return render_template('base.html', temperature=temperature, timeNow=timeNow) 
