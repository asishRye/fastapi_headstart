import psycopg2
conn = psycopg2.connect(
    "dbname=mydb user=postgres password=mysecretpassword")
cur = conn.cursor()


def createtable():
    cur.execute(
        "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    print("Table created")


def insertdata():
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
                (100, "abc'def"))
    print("Data inserted")


def fetchdata():
    cur.execute("SELECT * FROM test;")
    print(cur.fetchone())


conn.commit()

cur.close()
conn.close()
