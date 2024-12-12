from payment import Payment
from user import User
class Rider(User):
    def __init__(self, name, contact,payment_method):
        super().__init__(name, contact)
        self.payment_method=payment_method
        self.__current_ride =None
    def book_ride(self,ride):
        self.__current_ride=ride
        print(f'{self.get_name()} booked a ride')
    def make_payment(self,amount):
        Payment.process_payment(self.payment_method,amount)
    def get_current_ride(self):
        return self.__current_ride
