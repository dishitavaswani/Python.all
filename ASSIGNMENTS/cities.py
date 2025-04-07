with open("cities.txt", "r") as file:
    data = file.read()
    cities = [city.strip() for city in data.split("\n") if city.strip()]  # Remove empty lines and extra spaces
    cities.sort()

for city in cities:
    print(city)
