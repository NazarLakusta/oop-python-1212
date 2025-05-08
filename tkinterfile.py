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
        pass

def add_game():
    pass

def remove_game():
    pass

def view_game_details():
    pass



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








window.mainloop()