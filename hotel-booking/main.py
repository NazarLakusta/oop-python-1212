import tkinter as tk

import request
from app import HotelBookingApp
import sqlite3
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelBookingApp(root)

    root.mainloop()