# імпортуємо бібліотеку бази даних
import sqlite3

# підключення або створення бази даних
conn = sqlite3.connect("school.db")

# для виконання запитів
cursor = conn.cursor()

# створення таблиці, якщо ще не створена
cursor.execute('''
  CREATE TABLE IF NOT EXISTS students(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER,
  grade TEXT ) 
  ''')

# підтвердити зміни
conn.commit()

# додавання інформації у таблицю - INSERT INTO
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?,?,?)", ("Руслан", 13, "7Б"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?,?,?)", ("Евеліна", 13, "7А"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?,?,?)", ("Назар", 21, "502"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?,?,?)", ("Нікіта", 14, "8А"))

# підтвердити зміни
conn.commit()


# Зчитування даних

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)


print("ДОДАТКОВО")

cursor.execute("SELECT name, age FROM students WHERE grade = '7Б' ")
rows = cursor.fetchall()

for row in rows:
    print(row)



# Оновлення даних
cursor.execute("UPDATE students SET grade = ? WHERE name = ?",("8Б", "Руслан"))
print("ОНОВЛЕННЯ ДАНИХ")

cursor.execute("SELECT *  FROM students  ")
rows = cursor.fetchall()
for row in rows:
    print(row)


# Видалення даних
cursor.execute("DELETE FROM students  WHERE name = ?",("Нікіта",))
conn.commit()


print("ПІСЛЯ ВИДАЛЕННЯ")

cursor.execute("SELECT *  FROM students  ")
rows = cursor.fetchall()
for row in rows:
    print(row)



# Видалення значень у таблиці
cursor.execute("DELETE FROM students")
conn.commit()

# завершити зєднання
conn.close()