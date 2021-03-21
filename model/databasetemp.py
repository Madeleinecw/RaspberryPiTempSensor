import psycopg2
from datetime import date, datetime
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor() 

conn = psycopg2.connect('dbname=TempSense')
cur = conn.cursor()



def add_temp(temp, date, time):
    query = """
    INSERT INTO
        temperatures
    VALUES
        (DEFAULT, %s, %s, %s)
    """
    values = (temp, date, time)
    cur.execute(query, values)
    conn.commit()

def get_time_of_most_recent_temp():
    query = """
    SELECT time FROM 
        temperatures
    ORDER BY id DESC
    LIMIT 1
    """

    cur.execute(query)
    return cur.fetchall()[0][0]


temp = sensor.get_temperature()
date = str(date.today())
time = datetime.now().time().replace(microsecond=0)

# add_temp(temp, date, time)

cur.execute('select * from temperatures')
results = cur.fetchall()

print(type(get_time_of_most_recent_temp()))
print(get_time_of_most_recent_temp())
print(get_time_of_most_recent_temp())

# for result in results:
#     print(result)