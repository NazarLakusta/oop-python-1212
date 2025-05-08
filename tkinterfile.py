import tkinter as tk
from tkinter import messagebox


class Game:
    def __init__(self, title, genre, platform, year, description=""):
        self.title = title
        self.genre = genre
        self.platform = platform
        self.year = year
        self.description = description


class GameLibrary:
    def __init__(self):
        self.games = []

    # Додавання гри у список
    def add_game(self, game):
        self.games.append(game)

    # Видалення гри зі списку
    def remove_game(self, title):
        for game in self.games:
            if game.title == title:
                self.games.remove(game)
                return True

        return False

    # отримання всіх ігор
    def get_games(self):
        return self.games

    # отримання гри зі списку за назвою
    def get_game_by_title(self, title):
        for game in self.games:
            if game.title == title:
                return game

        return None


    def filter_games(self, genre=None, platform=None):
        result = []
        for game in self.games:
            if (genre == "Усі" or game.genre == genre) and (platform == "Усі" or game.platform == platform):
                result.append(game)

        return result




def update_game_list():
        game_listbox.delete(0, tk.END)
        genre_filter = genre_filter_var.get()
        platform_filter = platform_filter_var.get()
        games = library.filter_games(genre_filter,platform_filter)

        for game in games:
            game_listbox.insert(tk.END,f"{game.title} ({game.platform})")

def add_game():
     title = title_entry.get()
     genre = genre_var.get()
     platform = platform_var.get()
     year = year_entry.get()
     description = description_text.get("1.0",tk.END).strip()

     if not title or not year:
         messagebox.showerror("Помилка","Назва та рік - обовязкові!")
         return

     game = Game(title,genre,platform,year,description)
     library.add_game(game)
     update_game_list()

     #Очищення
     title_entry.delete(0,tk.END)
     year_entry.delete(0,tk.END)
     genre_var.set(genre_options[0])
     platform_var.set(platform_options[0])
     description_text.delete("1.0",tk.END)



def remove_game():
    selected = game_listbox.curselection()
    if selected:
        title = game_listbox.get(selected[0].split(" ("))[0]

        if library.remove_game(title):
            update_game_list()
        else:
            messagebox.showerror("Помилка","Гру не знайдено!")

    else:
        messagebox.showerror("Помилка", "Оберіть гру для видалення!")


def view_game_details():
    selected = game_listbox.curselection()
    if selected:
        title = game_listbox.get(selected[0].split(" ("))[0]
        game = library.get_game_by_title(title)

        if game:
            detail_window = tk.Toplevel(window)
            detail_window.title(f"Інформація про {game.title}")

            info = (
                f"Назва: {game.title}\n"
                f"Жанр: {game.genre}\n"
                f"Платформа: {game.platform}\n"
                f"Рік: {game.year}\n"
                f"Опис: {game.description}\n"
            )

            label = tk.Label(detail_window, text = info, justify="left")
            label.pack(padx=10,pady=10)

        else:
            messagebox.showerror("Помилка", "Інформацію не знайдено!")

    else:
        messagebox.showerror("Помилка", "Оберіть гру для видалення!")


window = tk.Tk()
window.title("Менджер колекції відеоігор")
window.geometry("300x600+900+300")

library = GameLibrary()

tk.Label(window,text="Назва гри:").pack()
title_entry = tk.Entry(window)
title_entry.pack()

tk.Label(window,text="Жанр:").pack()
genre_options = ["Actions","Adventure","RPG","Strategy","Simulation"]
genre_var = tk.StringVar()
genre_var.set(genre_options[0])
tk.OptionMenu(window,genre_var,*genre_options).pack()

tk.Label(window,text="Платформа:").pack()
platform_options = ["PC","PlayStation","Xbox","Nintendo Switch","Mobile"]
platform_var = tk.StringVar()
platform_var.set(platform_options[0])
tk.OptionMenu(window,platform_var,*platform_options).pack()


tk.Label(window,text="Рік випуску:").pack()
year_entry = tk.Entry(window)
year_entry.pack()


tk.Label(window,text="Опис гри:").pack()
description_text = tk.Text(window,height=4,width=40)
description_text.pack()

tk.Button(window, text = "Додати гру", command=add_game).pack(pady=2)
tk.Button(window, text = "Видалити гру", command=remove_game).pack(pady=2)
tk.Button(window, text = "Переглянути гру", command=view_game_details).pack(pady=2)


tk.Label(window,text = "Фільтр за жанром:").pack()
genre_filter_var = tk.StringVar()
genre_filter_var.set("Усі")
tk.OptionMenu(window,genre_filter_var,"Усі",*genre_options, command=lambda _: update_game_list()).pack()


tk.Label(window,text = "Фільтр за платформою:").pack()
platform_filter_var = tk.StringVar()
platform_filter_var.set("Усі")
tk.OptionMenu(window,platform_filter_var,"Усі",*platform_options, command=lambda _: update_game_list()).pack()

game_listbox = tk.Listbox(window, width=50,height=10)
game_listbox.pack(pady=10)


update_game_list()

window.mainloop()