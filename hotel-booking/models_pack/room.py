class Room:
    def __init__(self,number,price, capacity):
        self._number = number
        self._price = price
        self._capacity = capacity
        self._is_booked = False


    def book(self):
        if not self._is_booked:
            self._is_booked = True
            return True

        return False

    def unbook(self):
        self._is_booked = False


    def is_available(self):
        return not self._is_booked

    def get_info(self):
        return f"Кімната {self.number} - {self._price} грн, {self._capacity} осіб, {'Вільна' if not self._is_booked else 'Зайнята'}"

    def get_number(self):
        return self._number


class LuxuryRoom(Room):
    def __init__(self,number):
        super().__init__(number,price=3000,capacity=2)


class EconomyRoom(Room):
    def __init__(self,number):
        super().__init__(number,price=800,capacity=1)

