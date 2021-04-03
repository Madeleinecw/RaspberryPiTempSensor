import psycopg2
from datetime import date, datetime, timedelta
from typing import List, Tuple

conn = psycopg2.connect('dbname=TempSense')
cur = conn.cursor()

def add_temperatures_to_temperatures_database(temperature, datetime, outsidetemperature, feelsliketemperature):
    query = """
    INSERT INTO
        openweathertemperatures
    VALUES
        (DEFAULT, %s, %s, %s, %s)
    """
    values = (temperature, datetime, outsidetemperature, feelsliketemperature)
    cur.execute(query, values)
    conn.commit()

def get_time_of_most_recent_temperature():
    query = """
    SELECT datetime FROM 
        openweathertemperatures
    ORDER BY id DESC
    LIMIT 1
    """

    cur.execute(query)
    return cur.fetchall()[0][0]


def get_all_temperatures():
    query = """
    SELECT 
        temperature
    FROM 
        openweathertemperatures
    """
    cur.execute(query)
    return cur.fetchall()


def get_all_timestamps():
    query = """
    SELECT 
        datetime
    FROM 
        openweathertemperatures
    """
    cur.execute(query)
    return cur.fetchall()

def get_all_outside_temps():
    query = """
    SELECT 
        outsidetemperature
    FROM 
        openweathertemperatures
    """
    cur.execute(query)
    return cur.fetchall()

def get_all_feels_like_temps():
    query = """
    SELECT 
        feelsliketemperature
    FROM 
        openweathertemperatures
    """
    cur.execute(query)
    return cur.fetchall()

def get_temperatures_from_range(startTime:datetime, endTime:datetime) -> List[Tuple[float, float, float, datetime]]:
    query = """
    SELECT temperature, outsidetemperature, feelsliketemperature, datetime FROM
        openweathertemperatures
    WHERE 
        datetime
    BETWEEN %s AND %s
    """

    cur.execute(query, (startTime, endTime))
    return cur.fetchall()



# print(datetime.now().replace(microsecond=0))