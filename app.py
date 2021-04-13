from datetime import date, datetime, timedelta
from flask import Flask, render_template, url_for, copy_current_request_context, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import json
from threading import Thread, Event
from time import sleep
from utils.open_weather_map_service import get_outside_temp, get_outside_feels_like_temperature
from utils.temperatures_database_service import add_temperatures_to_temperatures_database, get_temperatures_from_range, get_time_of_most_recent_temperature
from w1thermsensor import W1ThermSensor

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True


socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=False, cors_allowed_origins='*')

sensor = W1ThermSensor() 
thread = Thread()
thread_stop_event = Event()
reloadGraph = True


def time_and_temp_background_task():
    global reloadGraph
    while not thread_stop_event.isSet():
        temperature = sensor.get_temperature()
        timeNow = datetime.now().time().replace(microsecond=0)
        
        socketio.emit('newTemperature', {'temperature' : temperature})
        socketio.emit('newTime', {'time' : str(timeNow)})
        
        if (timeNow.minute % 10 == 0) and (timeNow.minute != get_time_of_most_recent_temperature().minute):
            add_temperatures_to_temperatures_database(temperature, datetime.now().replace(microsecond=0), get_outside_temp(), get_outside_feels_like_temperature())
            outsideFeelsLikeTemperature = str(get_outside_feels_like_temperature())
            socketio.emit('newOutsideFeelsLike', {'outsideFeelsLikeTemperature': outsideFeelsLikeTemperature})
            socketio.emit('updated', {'updated': outsideFeelsLikeTemperature})
            outsideTemp = str(get_outside_temp())
            socketio.emit('newOutsideTemp', {'outsideTemp' :  outsideTemp}) 
        socketio.sleep(0.5)


def get_last_7_days():
    endTime = datetime.now()
    startTime = endTime - timedelta(days=7)   
    return get_temperatures_from_range(startTime, endTime)

def get_last_day():
    endTime = datetime.now()
    startTime = endTime - timedelta(days=1)   
    return get_temperatures_from_range(startTime, endTime)

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template("base.html")


@app.route('/getgraph/<startTime>/<endTime>')
def getGraphAsHtml(startTime: str, endTime: str):
    global reloadGraph
    reloadGraph = False

    formattedStartTime = datetime.strptime(startTime, '%Y-%m-%dT%H:%M')
    formattedEndTime = datetime.strptime(endTime, '%Y-%m-%dT%H:%M')
    
    rangeOfTemperatures = get_temperatures_from_range(formattedStartTime, formattedEndTime)    
    jsonBody = jsonify(rangeOfTemperatures)
    return jsonBody

@app.route('/getTemp')
def getTemp():
    temp = sensor.get_temperature() 
    return jsonify(temp)


@socketio.on('connect')
def test_connect():
    global thread

    print('Client connected')

    # graph = make_plot_from_range(get_last_day())
    # socketio.emit('newGraph', {'graph': graph}, namespace = '/test')

    outsideFeelsLikeTemperature = str(get_outside_feels_like_temperature())
    socketio.emit('newOutsideFeelsLike', {'outsideFeelsLikeTemperature': outsideFeelsLikeTemperature})

    outsideTemp = str(get_outside_temp())
    socketio.emit('newOutsideTemp', {'outsideTemp' :  outsideTemp})

    if not thread.isAlive():
        thread = socketio.start_background_task(time_and_temp_background_task)
    

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)