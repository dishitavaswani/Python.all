class Vehicle:
    def __init__(self, vehicle_type, rent_per_day, stock, agency):
        """Initialize vehicle details."""
        self.vehicle_type = vehicle_type
        self.rent_per_day = rent_per_day
        self.stock = stock
        self.agency = agency

    def display_details(self):
        """Display the available vehicle details."""
        print(
            f"The available {self.vehicle_type}s with {self.agency} agency are {self.stock} units, "
            f"with a rent of Rs {self.rent_per_day} per day."
        )

class RentalTransaction(Vehicle):
    def __init__(self, vehicle_type, rent_per_day, stock, agency):
        """Initialize rental transaction details."""
        super().__init__(vehicle_type, rent_per_day, stock, agency)

    def rent_vehicle(self, quantity):
        """Handle the rental process for vehicles."""
        if quantity <= 0:
            print("Invalid quantity. Please select at least one vehicle.")
            return False

        if quantity > self.stock:
            print(f"Sorry, we only have {self.stock} {self.vehicle_type}s available.")
            return False

        self.stock -= quantity
        print(f"Successfully rented {quantity} {self.vehicle_type}(s). Remaining stock: {self.stock}.")
        return True

    def calculate_amount(self, quantity, rental_period):
        """Calculate total rental cost."""
        return quantity * rental_period * self.rent_per_day


def main():
    print("==================================== CAR AND BUS RENTAL SYSTEM ====================================")
    print("===============================================================================================")

    
    car_inventory = RentalTransaction("Car", 25, 200, "Star")
    bus_inventory = RentalTransaction("Bus", 50, 100, "Royal")

    while True:
        print("\nPlease select an option:")
        print("1. Rent a Car")
        print("2. Rent a Bus")
        print("3. View Inventory")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:  
            car_inventory.display_details()
            try:
                quantity = int(input("Enter the number of cars you want to rent: "))
                rental_period = int(input("Enter the rental period in days: "))
                if car_inventory.rent_vehicle(quantity):
                    total_cost = car_inventory.calculate_amount(quantity, rental_period)
                    print(f"Please pay Rs {total_cost} for renting {quantity} car(s) for {rental_period} day(s).")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 2:  # Rent a Bus
            bus_inventory.display_details()
            try:
                quantity = int(input("Enter the number of buses you want to rent: "))
                rental_period = int(input("Enter the rental period in days: "))
                if bus_inventory.rent_vehicle(quantity):
                    total_cost = bus_inventory.calculate_amount(quantity, rental_period)
                    print(f"Please pay Rs {total_cost} for renting {quantity} bus(es) for {rental_period} day(s).")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 3:  
            print("\n--- Current Inventory ---")
            car_inventory.display_details()
            bus_inventory.display_details()

        elif choice == 4:  
            print("Thank you for using the Car and Bus Rental System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()


