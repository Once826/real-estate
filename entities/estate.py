class Estate:
    def __init__(self, id_code, headline, price, rooms, size, location):
        self.id = id_code
        self.headline = headline
        self.price = price
        self.rooms = rooms
        self.size = size
        self.location = location

    def __str__(self):
        return f'{self.headline} ({self.id}) - {self.price} eur. - {self.size} m2 - {self.rooms} rooms - {self.location}'