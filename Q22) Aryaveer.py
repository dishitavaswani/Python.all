# Base Class
class Vehicle:
    def __init__(self, vehicle_type, rent_per_day, agency, stock):
        self.vehicle_type = vehicle_type
        self.rent_per_day = rent_per_day
        self.agency = agency
        self.stock = stock

    def display_availability(self):
        """Displays available vehicles and details."""
        print(f"The available {self.vehicle_type}s are {self.stock} units with a rent of Rs {self.rent_per_day} per day from {self.agency} agency.")

# Derived Class
class RentalAgency(Vehicle):
    def __init__(self, agency, vehicle_type, rent_per_day, stock):
        super().__init__(vehicle_type, rent_per_day, agency, stock)

    def rent_vehicle(self, num_vehicles):
        """Handles vehicle rental."""
        if num_vehicles <= 0:
            print("Invalid number of vehicles. Please enter a positive number.")
            return False
        if num_vehicles > self.stock:
            print(f"Sorry, only {self.stock} {self.vehicle_type}s are available.")
            return False
        self.stock -= num_vehicles
        print(f"Rented {num_vehicles} {self.vehicle_type}(s) successfully!")
        return num_vehicles

    def calculate_total(self, num_vehicles, rental_period):
        """Calculates the total cost for renting vehicles."""
        return num_vehicles * rental_period * self.rent_per_day

# Main Program
print("================================== Car and Bus Rental System ==================================")
print("==============================================================================================")

# Setting Up Vehicle Inventory
car_agency = RentalAgency("Star", "Car", 25, 200)  # Star agency for cars
bus_agency = RentalAgency("Royal", "Bus", 50, 100)  # Royal agency for buses

while True:
    print("\nPlease enter your choice:")
    print("1: Rent a Car")
    print("2: Rent a Bus")
    print("3: Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if choice == 1:  # Rent a car
        car_agency.display_availability()
        try:
            num_cars = int(input("Enter the number of cars to rent: "))
            rental_period = int(input("Enter the rental period in days: "))
            if car_agency.rent_vehicle(num_cars):
                total_amount = car_agency.calculate_total(num_cars, rental_period)
                print(f"Please pay Rs {total_amount} for renting {num_cars} car(s) for {rental_period} day(s).")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    elif choice == 2:  # Rent a bus
        bus_agency.display_availability()
        try:
            num_buses = int(input("Enter the number of buses to rent: "))
            rental_period = int(input("Enter the rental period in days: "))
            if bus_agency.rent_vehicle(num_buses):
                total_amount = bus_agency.calculate_total(num_buses, rental_period)
                print(f"Please pay Rs {total_amount} for renting {num_buses} bus(es) for {rental_period} day(s).")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    elif choice == 3:  # Exit
        print("Thank you for using the Car and Bus Rental System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

