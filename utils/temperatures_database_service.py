import psycopg2
from datetime import date, datetime
from typing import List, Tuple

conn = psycopg2.connect('dbname=TempSense')
cur = conn.cursor()

def add_temperatures_to_temperatures_database(temperature, timestamp, outsideTemperature, feelsLike):
    query = """
    INSERT INTO
        temperatures
    VALUES
        (DEFAULT, %s, %s, %s, %s)
    """
    values = (temperature, timestamp, outsideTemperature, feelsLike)
    cur.execute(query, values)
    conn.commit()

def get_temperatures_from_range(startTime:datetime, endTime:datetime) -> List[Tuple[float, datetime]]:
    query = """
    SELECT temp, timestamp FROM
        temp
    WHERE 
        timestamp
    BETWEEN %s AND %s
    """

    cur.execute(query, (startTime, endTime))
    return cur.fetchall()


def get_time_of_most_recent_temperature():
    query = """
    SELECT timestamp FROM 
        temperatures
    ORDER BY id DESC
    LIMIT 1
    """

    cur.execute(query)
    return cur.fetchall()[0][0]


def get_all_temperatures():
    query = """
    SELECT 
        temp
    FROM 
        temp
    """
    cur.execute(query)
    return cur.fetchall()


def get_all_timestamps():
    query = """
    SELECT 
        timestamp
    FROM 
        temp
    """
    cur.execute(query)
    return cur.fetchall()