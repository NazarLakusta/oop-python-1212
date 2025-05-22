# Імпортуємо бібліотеку
import sqlite3

# 1. Підключення до БД (створиться файл student_data.db)
conn = sqlite3.connect("student_data.db")

# 2. Створюємо об'єкт cursor для SQL-запитів
cursor = conn.cursor()

# 3. Створення таблиці, якщо ще не створена
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')

# Зберігаємо зміни
conn.commit()

# 4. Додаємо кілька учнів
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Оля", 14, "8А"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Іван", 15, "9Б"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Максим", 13, "7В"))

# Підтверджуємо вставку
conn.commit()

# 5. Зчитування всіх учнів
print("📋 Список всіх учнів:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)  # кожен рядок — це кортеж: (id, name, age, grade)

# 6. Оновлення даних (наприклад, змінити клас Олі)
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("9А", "Оля"))
conn.commit()

# 7. Перевіримо, чи оновилось
print("\n🔁 Після оновлення Олі:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# 8. Видалимо одного учня (наприклад, Івана)
cursor.execute("DELETE FROM students WHERE name = ?", ("Іван",))
conn.commit()

# 9. Після видалення
print("\n❌ Після видалення Івана:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# 10. Закриваємо з’єднання
conn.close()
