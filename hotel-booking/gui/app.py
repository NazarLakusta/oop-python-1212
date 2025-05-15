import tkinter as tk

from tkinter import messagebox, ttk
from ..models_pack.room import EconomyRoom, LuxuryRoom
from ..models_pack.client import Client
from ..models_pack.hotel import Hotel
from ..models_pack.booking import Booking



class HotelBookingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Готельна система")
        self.root.geometry("600x400")
        self.hotel = Hotel("Чорне море")


        self.hotel.add_room(LuxuryRoom(101))
        self.hotel.add_room(LuxuryRoom(102))
        self.hotel.add_room(EconomyRoom(103))
        self.hotel.add_room(EconomyRoom(104))

        self.client = Client("Руслан")

        self.create_widgets()

    def create_widgets(self):
        self.tabs = ttk.Notebook(self.root)

        self.tab_rooms = ttk.Frame(self.tabs)
        self.tab_booking = ttk.Frame(self.tabs)
        self.tab_my_bookings = ttk.Frame(self.tabs)


        self.tabs.add(self.tab_rooms, text = "Вільні кімнати")
        self.tabs.add(self.tab_booking, text = "Забронювати")
        self.tabs.add(self.tab_my_bookings, text = "Мої бронювання")
        self.tabs.pack(expand=1, fill = "both")

        self.rooms_list = tk.Listbox(self.tab_rooms, font = ("Arial",12))
        self.rooms_list.pack(pady=10,fill = "both" , expand = True)

        self.update_rooms_list()

        self.booking_label = tk.Label(self.tab_booking, text="Введіть номер кімнати:")
        self.booking_label.pack(pady=10)
        self.room_entry = tk.Entry(self.tab_booking)
        self.room_entry.pack()

        self.book_button = tk.Button(self.tab_booking, text="Забронювати", command=self.book_room)
        self.book_button.pack(pady=10)

        self.my_bookings_list = tk.Listbox(self.tab_my_bookings, font=("Arial", 12))
        self.my_bookings_list.pack(pady=10, fill="both", expand=True)
        self.update_bookings_list()

    def update_rooms_list(self):
        self.rooms_list.delete(0, tk.END)
        for room in self.hotel.list_available_rooms():
            self.rooms_list.insert(tk.END, room.get_info())

    def update_bookings_list(self):
        self.my_bookings_list.delete(0, tk.END)
        for booking in self.client.get_bookings():
            self.my_bookings_list.insert(tk.END, booking.get_info())

    def book_room(self):
        try:
            number = int(self.room_entry.get())
        except ValueError:
            messagebox.showerror("Помилка", "Номер кімнати має бути числом")
            return
        room = self.hotel.find_room_by_number(number)
        if room and room.book():
            booking = Booking(self.client, self.hotel, room)
            self.client.add_booking(booking)
            messagebox.showinfo("Успіх", "Кімнату заброньовано успішно!")
            self.update_rooms_list()
            self.update_bookings_list()
        else:
            messagebox.showerror("Помилка", "Кімната зайнята або не існує")

