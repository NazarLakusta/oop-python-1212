class Client:
    def __init__(self, name):
        self._name = name
        self._bookings = []

    def add_booking(self, booking):
        self._bookings.append(booking)

    def get_bookings(self):
        return self._bookings

    def get_name(self):
        return self._name
