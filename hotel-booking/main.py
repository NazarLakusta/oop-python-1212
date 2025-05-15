from .gui.app import HotelBookingApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = HotelBookingApp(root)
    root.mainloop()

if __name__ == "main":
    main()