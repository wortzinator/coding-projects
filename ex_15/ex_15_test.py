import sqlite3
import re

conn = sqlite3.connect("autograderEmailDB.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

fname = input("input a file name bruv: ")
if (len(fname)< 1): fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
    domain = re.findall('^From .*@([^ ]*)', line)
    if len(domain) < 1: continue
    else: email = str(domain)
    email = email.strip("'[]'")
    cur.execute("SELECT count FROM Counts WHERE org = ?", (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (email,))

sqlstr = 'SELECT org, count FROM Counts ORDER BY count' #DESC LIMIT 10

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

conn.commit()
cur.close()