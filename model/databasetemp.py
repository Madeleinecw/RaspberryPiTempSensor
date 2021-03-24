import psycopg2
from datetime import date, datetime
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor() 

conn = psycopg2.connect('dbname=TempSense')
cur = conn.cursor()



def add_temp(temp, timestamp):
    query = """
    INSERT INTO
        temp
    VALUES
        (DEFAULT, %s, %s)
    """
    values = (temp, timestamp)
    cur.execute(query, values)
    conn.commit()

def get_temperatures_from_range(startTime:datetime, endTime:datetime) -> list:
    query = """
    SELECT temp, timestamp FROM
        temp
    WHERE 
        timestamp
    BETWEEN %s AND %s
    """

    cur.execute(query, (startTime, endTime))
    return cur.fetchall()


def get_time_of_most_recent_temp():
    query = """
    SELECT timestamp FROM 
        temp
    ORDER BY id DESC
    LIMIT 1
    """

    cur.execute(query)
    return cur.fetchall()[0][0]


def get_temps():
    query = """
    SELECT 
        temp
    FROM 
        temp
    """
    cur.execute(query)
    return cur.fetchall()


def get_timestamps():
    query = """
    SELECT 
        timestamp
    FROM 
        temp
    """
    cur.execute(query)
    return cur.fetchall()

def temp_list():
    new_list = []
    temps_list = get_temps()

    for temps in temps_list:
        new_list.append(float(temps[0]))
    return new_list


def timestamp_list():
    new_list = []
    timestamps = get_timestamps()

    for times in timestamps:
        new_list.append(times[0].strftime("%x") + " " + times[0].strftime("%X"))
    return new_list



temp = sensor.get_temperature()
timestamp = datetime.now().replace(microsecond=0)

# add_temp(temp, timestamp)

cur.execute('select * from temp')
results = cur.fetchall()


timestr = '2021-03-23T17:38'
datetime_obj = datetime.strptime(timestr, '%Y-%m-%dT%H:%M')
print(datetime_obj)
print(timestamp_list()[-1])
# for result in results:
#     print(result)