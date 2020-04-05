from os import chdir
from bs4 import BeautifulSoup
import sqlite3

chdir('webpages/')

conn = sqlite3.connect('0database.db')
conn.execute('''CREATE TABLE NAMES_DOC
         (ID INT PRIMARY KEY     NOT NULL,
         NAME   TEXT);''')

for i in range(1,10828):    
    f = open(str(i)+'.html', encoding='latin-1')
    soup = BeautifulSoup(f, "html.parser")
    a=[]
    for name in soup.find('div'):
        if 'Server Error' in str(name):
            break
        else:
            name=str(name).strip()
            conn.execute('''INSERT INTO NAMES_DOC (ID, NAME) VALUES(?,?)''',(i,name))
            break
    if not i%500:
            print(i, name)
conn.commit()
conn.close()
