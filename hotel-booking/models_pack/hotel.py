class Hotel:

    def __init__(self,name):
        self._name = name
        self._rooms = []

    def add_room(self,room):
        self._rooms.append(room)

    def list_available_rooms(self):
        return [room for room in self._rooms if room.is_available()]

    def find_room_by_number(self,number):
        for room in self._rooms:
            if room.get_number() == number:
                return room

        return  None

    def get_info(self):
        return f"{self.name} - {len(self._rooms) } кімнат"