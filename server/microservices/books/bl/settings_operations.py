import sqlite3
from dateutil import parser

def get_all_settings():
    conn = sqlite3.connect('books.db')
    cursor = conn.execute("select * from defs")
    res = []
    for row in cursor:
       rec = {}
       rec['id'] = row[0]
       rec['key'] = row[1]
       rec['value'] = row[2]
       res.append(rec)

    conn.close()
    return res

def update_setting(key,value):
    try:
        conn = sqlite3.connect('books.db')
        conn.execute("update books set value='%s' where key='%s'" % (key,value))
        conn.commit()
        conn.close()
        return 'Ok'
    except Exception as err:
        return err

if __name__ == "__main__":
    print get_all_settings()
