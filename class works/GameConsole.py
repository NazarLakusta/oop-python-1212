class GameConsole:

    def __init__(self):
        self.__batery_level = 50
        self.__game_library = []
        self.__is_on = False



    def turn_on(self):
        if self.__batery_level > 0:
            self.__is_on = True
            print("Консоль увімкнена")
        else:
            print("Немає заряду. Зарядіть консоль")


    def turn_off(self):
        self.__is_on = False
        print("Консоль вимкнена")

    def install_game(self,name):
        if name not in self.__game_library:
            self.__game_library.append(name)
            print(f"Гра {name}  встановлена")
        else:
            print("Гра вже є в бібліотеці")


    def play_game(self,name):
        if not self.__is_on:
            print("Спочатку увімкніть консоль")
            return

        if self.__batery_level < 5:
            print("Замало заряду для гри")
            return

        if name in self.__game_library:
            print(f"Граємо {name}")
            self.__batery_level -= 5
        else:
            print("Гра не встановлена")

    def charge_battery(self,amount):
        if amount > 0:
            self.__batery_level += amount
            if self.__batery_level > 100:
                self.__batery_level = 0
            print(f"Консоль заряджена на {self.__batery_level}%")

        else:
            print("неправильне значення заряду")

    def get_battery(self):
        return self.__batery_level

    def list_game(self):
        if len(self.__game_library) == 0:
            return "Бібліотека порожня"

        return ", ".join(self.__game_library)



console = GameConsole()
console.turn_on()
console.install_game("Fifa 25")
console.install_game("Dota 2")
console.install_game("Roblox")
console.play_game("Dota 2")
console.play_game("Dota 2")
console.play_game("Dota 2")
console.play_game("Dota 2")
console.play_game("Dota 2")
console.play_game("Dota 2")
console.play_game("Dota 2")
console.play_game("Dota 2")
console.play_game("Dota 2")
console.play_game("Dota 2")
console.play_game("Dota 2")
console.play_game("Dota 2")

print(console.get_battery())
console.turn_off()