from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context, jsonify
from random import random
from time import sleep
from threading import Thread, Event
from datetime import date, datetime
from w1thermsensor import W1ThermSensor
from utils.database_service import add_temp, get_time_of_most_recent_temp, get_temps, get_timestamps, get_temperatures_from_range
from testplotting import make_plot
from markupsafe import escape
from graphmaker import make_plot_from_range
from utils.open_weather_map_service import get_outside_temp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app, async_mode=None, logger=False, engineio_logger=False)

sensor = W1ThermSensor() 
thread = Thread()
thread_stop_event = Event()
reloadGraph = True


def time_and_temp_background_task():
    global reloadGraph
    while not thread_stop_event.isSet():
        temperature = sensor.get_temperature()
        timeNow = datetime.now().time().replace(microsecond=0)
        
        socketio.emit('newTemperature', {'temperature' : temperature}, namespace='/test')
        socketio.emit('newTime', {'time' : str(timeNow)}, namespace='/test')
        
        if (timeNow.minute % 10 == 0) and (timeNow.minute != get_time_of_most_recent_temp().minute):
            add_temp(temperature, timeNow)
            graph = make_plot()
            if reloadGraph:
                socketio.emit('newGraph', {'graph': graph}, namespace='/test')
                
        socketio.sleep(0.5)


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('base.html')

@app.route('/check')
def check():
    return render_template('lines.html')

@app.route('/all')
def getAllTimeGraph():
    global reloadGraph
    reloadGraph = True
    graphHtml = make_plot()
    body = {'graphHtml': graphHtml}
    
    return jsonify(body)

@app.route('/getgraph/<startTime>/<endTime>')
def getGraphAsHtml(startTime: str, endTime: str):

    global reloadGraph
    reloadGraph = False
    formattedStartTime = datetime.strptime(startTime, '%Y-%m-%dT%H:%M')
    formattedEndTime = datetime.strptime(endTime, '%Y-%m-%dT%H:%M')
    
    rangeOfTemperatures = get_temperatures_from_range(formattedStartTime, formattedEndTime)
    
    graphHtml = make_plot_from_range(rangeOfTemperatures)

    body = {'graphHtml' : graphHtml}

    return jsonify(body) 

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread

    print('Client connected')

    graph = make_plot()
    socketio.emit('newGraph', {'graph': graph}, namespace = '/test')

    outsideTemp = get_outside_temp()
    socketio.emit('newoutsideTemp', {'outsideTemp' :  outsideTemp}, namespace='/test')

    if not thread.isAlive():
        thread = socketio.start_background_task(time_and_temp_background_task)
    

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)