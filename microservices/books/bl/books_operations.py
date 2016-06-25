import sqlite3

def get_all_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.execute("select * from books")
    res = []
    for row in cursor:
       rec = {}
       rec['id'] = row[0]
       rec['writers'] = row[1]
       rec['title'] = row[2]
       rec['series'] = row[3]
       rec['copies'] = row[4]
       rec['volumes'] = row[5]
       rec['date_created'] = row[6]
       res.append(rec)

    conn.close()
    return res

if __name__ == "__main__":
    print get_all_books()
