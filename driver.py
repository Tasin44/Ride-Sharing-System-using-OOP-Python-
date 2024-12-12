from user import User
class Driver(User):
    def __init__(self, name, contact,vehicle):
        super().__init__(name, contact)
        self.vehicle=vehicle
    def accept_ride(self,Ride):
        Ride.assign_driver(self)
        print(f'{self.get_contact()} accepted the ride.')