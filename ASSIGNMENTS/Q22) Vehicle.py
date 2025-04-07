
class Vehicle:
    def __init__(self, vt, models, agency):
        self.vt = vt  
        self.models = models  
        self.agency = agency

    def display_models(self):
        print(f"\nAvailable {self.vt} from {self.agency} agency:")
        for index, (model, details) in enumerate(self.models.items(), start=1):  # Adding numbers to models
            print(f"{index}. {model}: Rent = Rs {details['rent']} per day, Number of Vehicles = {details['num_vehicles']}")

    def update_model_inventory(self, model_name, rented_quantity):
        if model_name in self.models:
            self.models[model_name]["num_vehicles"] -= rented_quantity



class RentalTransaction(Vehicle):
    def __init__(self, vt, models, agency):
        super().__init__(vt, models, agency)

    def rental_period(self):
        while True:
            try:
                days = int(input("Enter the rental period (in days): "))
                if days > 0:
                    return days
                else:
                    print("The rental period must be a positive number. Try again.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def process_booking(self, model_name, rental_days, quantity):
        if model_name in self.models:
            num_vehicles_available = self.models[model_name]["num_vehicles"]
            rent_price = self.models[model_name]["rent"]

            if quantity <= num_vehicles_available:
                self.update_model_inventory(model_name, quantity)
                total_amount = rent_price * quantity * rental_days
                print(f"\n--- Booking Confirmation ---")
                print(f"Your order for {quantity} {model_name}(s) of {self.agency} agency is confirmed.")
                print(f"Total rent for {rental_days} days: Rs {total_amount}")
                print(f"Remaining Number of Vehicles for {model_name}: {self.models[model_name]['num_vehicles']}")
            else:
                print(f"Sorry, only {num_vehicles_available} {model_name}(s) are available right now.")
        else:
            print(f"{model_name} is not a valid model.")



def main():
    print("              Welcome to the Enhanced CAR and BUS Rental System!              ")
    print("-------------------------------------------------------------------------------")

    
    car_models = {
        "Toyota Corolla": {"rent": 30, "num_vehicles": 10},
        "Honda Civic": {"rent": 40, "num_vehicles": 8},
        "Suzuki Swift": {"rent": 25, "num_vehicles": 12},
        "Toyota Fortuner": {"rent": 80, "num_vehicles": 5},
        "Ford Endeavour": {"rent": 90, "num_vehicles": 4},
        "Tesla Model X": {"rent": 150, "num_vehicles": 3},
    }

    bus_models = {
        "Volvo Bus": {"rent": 100, "num_vehicles": 6},
        "Mini Bus": {"rent": 60, "num_vehicles": 10},
    }

    
    car_rental = RentalTransaction("Cars", car_models, "Star Rentals")
    bus_rental = RentalTransaction("Buses", bus_models, "Royal Bus Service")

    while True:
        print("\nMenu Options:")
        print("1: View Available Cars")
        print("2: View Available Buses")
        print("3: Rent a Car")
        print("4: Rent a Bus")
        print("5: Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            car_rental.display_models()

        elif choice == "2":
            bus_rental.display_models()

        elif choice == "3":
        
            car_rental.display_models()
            try:
                car_choice = int(input("\nEnter the number of the car you want to rent: "))
                if 1 <= car_choice <= len(car_rental.models):
                    model_name = list(car_rental.models.keys())[car_choice - 1]  # Get model name by number
                    quantity = int(input(f"Enter the number of {model_name}(s) to rent: "))
                    if quantity > 0:
                        rental_days = car_rental.rental_period()
                        car_rental.process_booking(model_name, rental_days, quantity)
                    else:
                        print("Please enter a valid quantity.")
                else:
                    print("Invalid choice! Please select a valid car number.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == "4":
        
            bus_rental.display_models()
            try:
                bus_choice = int(input("\nEnter the number of the bus you want to rent: "))
                if 1 <= bus_choice <= len(bus_rental.models):
                    model_name = list(bus_rental.models.keys())[bus_choice - 1]  # Get model name by number
                    quantity = int(input(f"Enter the number of {model_name}(s) to rent: "))
                    if quantity > 0:
                        rental_days = bus_rental.rental_period()
                        bus_rental.process_booking(model_name, rental_days, quantity)
                    else:
                        print("Please enter a valid quantity.")
                else:
                    print("Invalid choice! Please select a valid bus number.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == "5":
            print("Thank you for using our rental system. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")


main()
