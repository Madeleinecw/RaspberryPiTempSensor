import psycopg2
from datetime import datetime

conn = psycopg2.connect('dbname=TempSense')
cur = conn.cursor()



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

# cur.execute('select * from temp')

# results = cur.fetchall()


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

print(temp_list())
print(timestamp_list())
# for result in results:
#     print(result)