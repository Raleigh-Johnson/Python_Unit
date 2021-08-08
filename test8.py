import sqlite3

conn = sqlite3.connect('String.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_String( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_file TEXT)") 
    conn.commit()




fileList = ['information.doxc', 'Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']
newList = []

for x in fileList:
    if x.endswith('.txt'):
        newList.append(x)
print(newList)

with conn:
    for x in newList:
        cur.execute("INSERT INTO tbl_String('col_file') Values (?)",(x,))
    conn.commit()
    cur.execute("Select col_file FROM tbl_String")
    print(cur.fetchall())
conn.close()
