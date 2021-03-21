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


temp = sensor.get_temperature()
date = str(date.today())
time = datetime.now().time().replace(microsecond=0)

add_temp(temp, date, time)

cur.execute('select * from temperatures')
results = cur.fetchall()

for result in results:
    print(result)