import tkinter as tk
from tkinter import messagebox


# Клас для книги
class Book:
    def __init__(self, title, author, year, genre, content=""):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.content = content


# Клас для бібліотеки
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def get_books(self):
        return self.books

    def get_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


# Функція для оновлення списку книг на екран
def update_books_list():
    books_listbox.delete(0, tk.END)
    for book in library.get_books():
        books_listbox.insert(tk.END, f"{book.title} - {book.author} ({book.year})")


# Функція для додавання книги
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    genre = genre_var.get()
    content = content_text.get("1.0", tk.END).strip()

    if not title or not author or not year or not genre:
        messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля!")
        return

    book = Book(title, author, year, genre, content)
    library.add_book(book)
    update_books_list()

    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    genre_var.set(genre_options[0])  # Скидаємо вибір жанру
    content_text.delete("1.0", tk.END)


# Функція для видалення книги
def remove_book():
    selected_book_index = books_listbox.curselection()
    if selected_book_index:
        selected_book = books_listbox.get(selected_book_index)
        title = selected_book.split(" - ")[0]

        if library.remove_book(title):
            update_books_list()
        else:
            messagebox.showerror("Помилка", "Не вдалося знайти книгу для видалення.")
    else:
        messagebox.showerror("Помилка", "Будь ласка, виберіть книгу для видалення.")


# Функція для перегляду інформації про книгу
def view_book_info():
    selected_book_index = books_listbox.curselection()
    if selected_book_index:
        selected_book = books_listbox.get(selected_book_index)
        title = selected_book.split(" - ")[0]
        book = library.get_book_by_title(title)

        if book:
            info_window = tk.Toplevel(window)
            info_window.title(f"Інформація про книгу: {book.title}")

            info_label = tk.Label(info_window,
                                  text=f"Назва: {book.title}\nАвтор: {book.author}\nРік видання: {book.year}\nЖанр: {book.genre}\n\nВміст книги:\n{book.content}")
            info_label.pack(padx=10, pady=10)
        else:
            messagebox.showerror("Помилка", "Не вдалося знайти книгу.")
    else:
        messagebox.showerror("Помилка", "Будь ласка, виберіть книгу для перегляду.")


# Головне вікно
window = tk.Tk()
window.title("Бібліотечний каталог")

library = Library()

# Поля для вводу даних про книгу
title_label = tk.Label(window, text="Назва книги:")
title_label.pack()
title_entry = tk.Entry(window)
title_entry.pack()

author_label = tk.Label(window, text="Автор:")
author_label.pack()
author_entry = tk.Entry(window)
author_entry.pack()

year_label = tk.Label(window, text="Рік видання:")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

genre_label = tk.Label(window, text="Жанр:")
genre_label.pack()

# Варіанти жанрів
genre_options = ["Фантастика", "Детектив", "Роман", "Науково-популярна", "Пригоди"]
genre_var = tk.StringVar(window)
genre_var.set(genre_options[0])  # Встановлюємо початкове значення

genre_menu = tk.OptionMenu(window, genre_var, *genre_options)
genre_menu.pack()

content_label = tk.Label(window, text="Вміст книги:")
content_label.pack()

content_text = tk.Text(window, height=5, width=40)
content_text.pack()

# Кнопки
add_button = tk.Button(window, text="Додати книгу", command=add_book)
add_button.pack()

remove_button = tk.Button(window, text="Видалити книгу", command=remove_book)
remove_button.pack()

view_button = tk.Button(window, text="Переглянути інформацію про книгу", command=view_book_info)
view_button.pack()

# Список книг
books_listbox = tk.Listbox(window, width=50, height=10)
books_listbox.pack()

# Початкове оновлення списку книг
update_books_list()

# Запуск додатка
window.mainloop()
