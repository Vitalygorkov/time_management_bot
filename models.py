import sqlite3

class TaskObject(object):

    def __init__(self, name, status, type):
        """Constructor"""
        self.name = name
        self.status = status
        self.type = type # three types of tasks - ten-year, annual, monthly



conn = sqlite3.connect('tm_base.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS tasks(
   name TEXT PRIMARY KEY,
   status INTEGER,
   type INTEGER);
""")
conn.commit()

# module for writing to the database
def task_write(name, status, type):
    # conn = sqlite3.connect('tm_base.db')
    # cur = conn.cursor()
    task = (name, status, type)
    try:
        cur.execute("INSERT INTO tasks VALUES(?, ?, ?);", task)
        conn.commit()
    except Exception as e:
        print(e)
    print('database entry completed')


# module for reading from the database


def task_read():
    # conn = sqlite3.connect('tm_base.db')
    # cur = conn.cursor()

    cur.execute("SELECT * FROM tasks;")
    all_results = cur.fetchall()
    return all_results

