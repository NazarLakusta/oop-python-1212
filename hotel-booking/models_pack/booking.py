import datetime

class Booking:
    def __init__(self,client,hotel,room):
        self._client = client
        self._hotel  = hotel
        self._room = room
        self._date = datetime.date.today()

    def get_info(self):
        return f"{self._client.get_name()} забронював кімнату {self._room.get_number()} в {self._hotel._name} на {self._date}"


