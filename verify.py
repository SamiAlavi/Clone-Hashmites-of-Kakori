import sqlite3


def verify_files():
    conn = sqlite3.connect('webpages/0database.db')
    cur = conn.cursor()
    cur.execute("SELECT ID FROM NAMES_DOC")
    rows = cur.fetchall()
    i=1
    for row in rows:
        if i==row[0]:
            i+=1
            continue
        else:
            i+=2
    conn.close()
    print(i)

verify_files()
