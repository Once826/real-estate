import csv

from entities.estate import Estate
from entities.location import Location

DATA_FILE = 'data/estates.csv'

class Repository:
    def __init__(self):
        self.__data = []
        self.__load_data()

    def __load_data(self):
        with open(DATA_FILE, 'r') as file:
            reader = csv.DictReader(file, )
            for row in reader:
                try:
                    estate = Estate(row.get('id'), row['headline'], row['price'], row['size'], row['rooms'], Location(row['zip'], row['city'], row['street'], row['number'], row['country']))
                    self.__data.append(estate)
                except KeyError as e:
                    print(f"Missing key {e} in row: {row}")

    def get_all(self):
        return self.__data

    def get_by_id(self, id_code):
        for estate in self.__data:
            if estate.id == id_code:
                return estate
        return None

    def add(self, estate):
        self.__data.append(estate)

    def update(self, estate):
        for i in range(len(self.__data)):
            if self.__data[i].id == estate.id:
                self.__data[i] = estate
                return
        raise ValueError(f'Estate with id {estate.id} not found')

    def delete(self, id_code):
        for i in range(len(self.__data)):
            if self.__data[i].id == id_code:
                del self.__data[i]
                return
        raise ValueError(f'Estate with id {id_code} not found')