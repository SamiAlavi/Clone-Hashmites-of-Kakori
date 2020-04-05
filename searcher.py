from os import chdir
import sqlite3
import webbrowser

chdir('webpages/')


go=True

while go:
    conn = sqlite3.connect('0database.db')
    cur = conn.cursor()
    
    search=input('Enter name: ')
    if len(search)>1:
        search='%'+search+'%'
    else:
        print('Search character length must be greater 1')
        continue
    cur.execute("SELECT ID, NAME FROM NAMES_DOC WHERE NAME LIKE ?",(search,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    print()
    conn.close()
    a=input('Type q/Q to quit: ')
    if a=='q' or a=='Q':
        go=False
