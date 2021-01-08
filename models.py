import sqlite3

class TaskObject(object):

    def __init__(self, name, status, type):
        """Constructor"""
        self.name = name
        self.status = status
        self.type = type # three types of tasks - ten-year, annual, monthly



# conn = sqlite3.connect('tm_base.db')
# cur = conn.cursor()
# # cur.execute("SELECT * FROM channels;")
# # all_results = cur.fetchall()
# cur.execute("""CREATE TABLE IF NOT EXISTS vidos(
#    User TEXT PRIMARY KEY,
#    Goals TEXT,
#    prosm TEXT,
#    Others TEXT);
# """)
# conn.commit()