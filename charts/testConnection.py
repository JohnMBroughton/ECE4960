import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("connection made")
    except Error as e:
        print(e)

    return conn

def select_all_tasks(conn):
    """
    Query all rows in the auth_user table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM chartjs_rfid")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def insert_RFID(conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO chartjs_rfid (Lot,RFID) VALUES ('CO2',99999999)")

def delete_RFID(conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM chartjs_rfid WHERE RFID=99999999")

conn = create_connection("db.sqlite3")
select_all_tasks(conn)
insert_RFID(conn)
select_all_tasks(conn)
delete_RFID(conn)
select_all_tasks(conn)