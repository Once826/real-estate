class Location:
    def __init__(self, zip, city, street, number, country):
        self.zip = zip
        self.city = city
        self.street = street
        self.number = number
        self.country = country

    def __str__(self):
        return f'{self.street} {self.number}, {self.zip} {self.city}, {self.country}'
