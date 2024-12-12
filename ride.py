class Ride:
    def __init__(self,rider,destination,distance):
       self.__rider = rider
       self.__destination= destination
       self.__distance=distance
       self.__driver=None
       self.__status ="Booked" #default status is booked

    def assign_driver(self,driver):
        self.__driver = driver
        self.__status="In Progress" # Ride is now in progress

    def get_ride_details(self):
         return{
             "rider": self.__rider.get_name(),
             "driver":self.__driver.get_name() if self.__driver else "Not assigned",
             "destination":self.__destination,
             "distance":self.__distance,
             "status":self.__status
         }
    def cancel_ride(self):
        if self.__status=="Booked":
            self.__status="Cancelled"
            print(f"The ride to {self.__destination} has been cancelled")
            if self.__driver:
                print(f"Notifying {self.__driver.get_name()} about cancellation.")
            return True
        else:
            print(f"Impossible to cancel now,Current Statufs:{self.__status}")
            return False
    
    def calculate_total_fare(self):
        if self.__driver and self.__driver.vehicle:
            return self.__driver.vehicle.calculate_fare(self.__distance)
        return 0