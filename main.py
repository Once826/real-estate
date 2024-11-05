from entities.estate import Estate
from entities.location import Location
from repository.repository import Repository

if __name__ == '__main__':
	repository = Repository()
	while True:
		print("\nReal Estate App")
		print("1. Add Property")
		print("2. Delete Property")
		print("3. Modify Property")
		print("4. Display All Properties")
		print("5. Exit")

		choice = input("Enter your choice: ")

		if choice == '1':
			id_code = input("Enter id: ")
			headline = input("Enter headline: ")
			price = input("Enter price: ")
			size = input("Enter size: ")
			rooms = input("Enter rooms: ")
			zip_code = input("Enter zip code: ")
			city = input("Enter city: ")
			street = input("Enter street: ")
			number = input("Enter number: ")
			country = input("Enter country: ")
			repository.add(Estate(id_code, headline, price, size, rooms, Location(zip_code, city, street, number, country)))
		elif choice == '2':
			id_code = input("Enter id: ")
			repository.delete(id_code)
		elif choice == '3':
			id_code = input("Enter id: ")
			estate = repository.get_by_id(id_code)
			if estate is None:
				print(f'Estate with id {id_code} not found')
			else:
				print(estate)
				estate.headline = input("Enter headline: ")
				estate.price = input("Enter price: ")
				estate.size = input("Enter size: ")
				estate.rooms = input("Enter rooms: ")
				estate.location.zip = input("Enter zip code: ")
				estate.location.city = input("Enter city: ")
				estate.location.street = input("Enter street: ")
				estate.location.number = input("Enter number: ")
				estate.location.country = input("Enter country: ")
				repository.update(estate)
		elif choice == '4':
			for estate in repository.get_all():
				print(estate)
		elif choice == '5':
			break
		else:
			print("Invalid choice")
