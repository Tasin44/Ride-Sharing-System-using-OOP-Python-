from rider import Rider
from driver import Driver
from ride import Ride
from car import Car
from bike import Bike
from van import Van

def ask_to_cancel(ride):
    """Checks if the user wants to cancel the ride."""
    cancel_choice = input("Do you want to cancel the ride? (yes/no): ").strip().lower()
    if cancel_choice in ["yes", "y"]:
        if ride.cancel_ride():
            print("Ride cancelled successfully. Thanks for staying with us!")
            return True
        else:
            print("Ride could not be cancelled. You must complete the ride.")
    return False

def main():
    print("Welcome to the Ride-Sharing App!")

    # Create some sample drivers with vehicles
    drivers = [
        Driver("Alex Rider", "55555", Car("ABC123")),  # Car with the license plate "ABC123"
        Driver("Emily Stone", "666666", Bike("XYZ987")),  # Bike with the license plate "XYZ987"
        Driver("Michael Scott", "777777", Van("VAN101"))
    ]

    # Get rider details
    rider_name = input("Enter your name: ")
    rider_contact = input("Enter your contact number: ")
    payment_method = input("Enter your payment method (e.g., Bkash, Nagad): ")
    rider = Rider(rider_name, rider_contact, payment_method)

    # Get ride details
    destination = input("Enter your destination: ")
    distance = float(input("Enter the distance to your destination (in km): "))
    ride = Ride(rider, destination, distance)

    # Rider books a ride
    rider.book_ride(ride)

    # Allow cancellation
    if ask_to_cancel(ride):
        return

    # Display available drivers and assign one
    print("\nAvailable drivers:")
    for idx, driver in enumerate(drivers, start=1):
        print(f"{idx}. {driver.get_name()} (Vehicle: {type(driver.vehicle).__name__}, License Plate: {driver.vehicle.license_plate})")

    driver_choice = int(input("Choose a driver (enter the number): ")) - 1
    if 0 <= driver_choice < len(drivers):
        chosen_driver = drivers[driver_choice]
        chosen_driver.accept_ride(ride)
    else:
        print("Invalid choice. Exiting the application.")
        return

    # Allow cancellation after driver assignment
    if ask_to_cancel(ride):
        return

    # Display ride details
    print("\nRide Details:")
    print(ride.get_ride_details())

    # Calculate and process payment
    fare = ride.calculate_total_fare()
    print(f"Total Fare: {fare}")

    # Inform user that ride must be completed if cancellation is not possible
    print("Since the ride is in progress, cancellation is no longer possible. Please complete your ride.")

    # Process payment
    rider.make_payment(fare)

    # Display final ride details
    print("\nFinal Ride Details:")
    print(ride.get_ride_details())

if __name__ == "__main__":
    main()
