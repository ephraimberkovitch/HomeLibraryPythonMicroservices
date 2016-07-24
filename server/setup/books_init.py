import sqlite3

conn = sqlite3.connect('books.db')
c = conn.cursor()

f = open("books.csv")
lines = f.readlines()
first_line = True
for line in lines:
    if first_line:
        first_line = False
        continue
    tokens = line.strip(',').strip('\r\n').split(',')
    writers = tokens[0]
    title = tokens[1]
    series = tokens[2]
    if len(tokens)>3:
        copies = tokens[3]
        if copies=='':
            copies = 1
        volumes = tokens[4]
        if volumes=='':
            volumes = 1
    else:
        copies = 1
        volumes = 1
    cmd = "INSERT INTO books(writers,title,series,copies,volumes) VALUES('%s','%s','%s',%s,%s)" % \
            (writers,title,series,copies,volumes)
    c.execute(cmd)

conn.commit()
conn.close()