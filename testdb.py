import psycopg2

conn = psycopg2.connect('dbname=test')
cur = conn.cursor()

def add_person(name, company):
    query = """
    INSERT INTO
        people
    VALUES
        (%s, %s)
    """
    values = (name, company)
    cur.execute(query, values)
    conn.commit()

def get_people_by_company(company):
    query = """
    SELECT
        *
    FROM
        people
    WHERE
        company = %s
    """
    values = (company, )
    cur.execute(query, values)
    return cur.fetchall()

# print(get_people_by_company('Dickhead & Co'))
# add_person('maddie', 'unemployed')

cur.execute('select * from people')

results = cur.fetchall()

for result in results:
    print(result)