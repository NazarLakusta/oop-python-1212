import sqlite3

conn = sqlite3.connect("university.db")

cursor = conn.cursor()


cursor.execute(''' CREATE TABLE IF NOT EXISTS groups   (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL )
''')
conn.commit()

cursor.execute(''' CREATE TABLE IF NOT EXISTS  students   (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
group_id INTEGER,
FOREIGN KEY (group_id) REFERENCES groups(id) )
''')
conn.commit()

cursor.execute("INSERT INTO groups (name) VALUES('1212')")
cursor.execute("INSERT INTO groups (name) VALUES('2422')")
cursor.execute("INSERT INTO groups (name) VALUES('1411')")
cursor.execute("INSERT INTO groups (name) VALUES('2121')")
conn.commit()

cursor.execute("INSERT INTO students (name,group_id) VALUES ('Назар',1)")
cursor.execute("INSERT INTO students (name,group_id) VALUES ('Евеліна',1)")
cursor.execute("INSERT INTO students (name,group_id) VALUES ('Максим',1)")
cursor.execute("INSERT INTO students (name,group_id) VALUES ('Максим 2',1)")
cursor.execute("INSERT INTO students (name,group_id) VALUES ('Руслан',2)")
cursor.execute("INSERT INTO students (name,group_id) VALUES ('Нікіта',2)")
cursor.execute("INSERT INTO students (name,group_id) VALUES ('Дмитро',3)")
cursor.execute("INSERT INTO students (name,group_id) VALUES ('Павло',3)")
conn.commit()



# Видалення значень у таблиці
cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM groups")
conn.commit()


conn.close()