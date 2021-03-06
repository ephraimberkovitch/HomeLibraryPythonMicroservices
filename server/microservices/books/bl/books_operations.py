import sqlite3
from dateutil import parser

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
       rec['volumes'] = row[4]
       rec['copies'] = row[5]
       rec['date_created'] = parser.parse(row[6])
       rec['is_owned'] = row[7]
       rec['is_younger'] = row[8]
       res.append(rec)

    conn.close()
    return res

def insert_book(writers,title,series,volumes,copies,is_owned,is_younger):
    try:
        conn = sqlite3.connect('books.db')
        conn.execute("insert into books(writers,title,series,volumes,copies,is_owned,is_younger) values('%s','%s','%s',%s,%s,%s,%s)" % (writers,title,series,volumes,copies,is_owned,is_younger))
        conn.commit()
        cursor = conn.execute("select last_insert_rowid() as new_id")
        for row in cursor:
            id = row[0]
            break
        conn.close()
        return {'new_id':id}
    except Exception as err:
        return {'error':err}

def update_book(id,writers,title,series,volumes,copies,is_owned,is_younger):
    try:
        conn = sqlite3.connect('books.db')
        conn.execute("update books set writers='%s',title='%s',series='%s',volumes=%s,copies=%s,is_owned=%s,is_younger=%s where BookId=%s" %
                     (writers,title,series,volumes,copies,is_owned,is_younger, id))
        conn.commit()
        conn.close()
        return 'Ok'
    except Exception as err:
        return err

def delete_book(book_id):
    conn = sqlite3.connect('books.db')
    conn.execute("delete from books where BookId=%s" % book_id)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print get_all_books()
