from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event
from datetime import date, datetime
from w1thermsensor import W1ThermSensor
from model.databasetemp import add_temp, get_time_of_most_recent_temp, get_temps, get_timestamps
from testplotting import make_plot


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)



sensor = W1ThermSensor() 
thread= Thread()
thread_stop_event = Event()


def save_temp_to_database():
        temp = sensor.get_temperature()
        timestamp = datetime.now().replace(microsecond=0)
        add_temp(temp, timestamp)

def send_time_and_temperature():
    print("getting the temperature")
    while not thread_stop_event.isSet():
        temperature = sensor.get_temperature()
        timeNow = datetime.now().time().replace(microsecond=0)
        time = str(timeNow)
        socketio.emit('newTemperature', {'temperature' : temperature}, namespace='/test')
        socketio.emit('newTime', {'time' : time}, namespace='/test')
        
        if (timeNow.minute % 10 == 0) and (timeNow.minute != get_time_of_most_recent_temp().minute):
            save_temp_to_database() 
            make_plot()
            graph = make_plot()
            print('emitting graph?')
            socketio.emit('newGraph', {'graph': graph}, namespace='/test')
        socketio.sleep(0.5)
         


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('base.html')

@app.route('/getgraph/<int:startTime>/<int:endTime>')
# def getGraph(startTime, endTime):
    # go to database, get data
    # using data, generate graph
    # return graph

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')
    graph = make_plot()
    socketio.emit('newGraph', {'graph': graph}, namespace = '/test')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = socketio.start_background_task(send_time_and_temperature)
    

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)