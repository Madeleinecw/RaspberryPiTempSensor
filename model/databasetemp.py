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

def get_time_of_most_recent_temp():
    query = """
    SELECT timestamp FROM 
        temp
    ORDER BY id DESC
    LIMIT 1
    """

    cur.execute(query)
    return cur.fetchall()[0][0]


temp = sensor.get_temperature()
timestamp = datetime.now().replace(microsecond=0)

# add_temp(temp, timestamp)

cur.execute('select * from temp')
results = cur.fetchall()

print(type(get_time_of_most_recent_temp()))
print(get_time_of_most_recent_temp())

# for result in results:
#     print(result)