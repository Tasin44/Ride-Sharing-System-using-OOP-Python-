'''
Explanation:
1.why __used before name and contact in User class:

The use of a double underscore (__) before attributes like __name and __contact 
is a way of implementing name mangling in Python, which helps to achieve a form of encapsulation. 

Here's why it is used:
Name Mangling:
When a variable or method starts with a double underscore (__), 
Python changes its name internally by adding _ClassName to the beginning of the variable name. 
For example, __name in the class User will be internally changed to _User__name.

Encapsulation:
By using double underscores, the attributes __name and __contact are not directly accessible from outside the class. 
Must use methods like get_name() or get_contact() to access them.

Example:

In the User class:
code:
self.__name = name
self.__contact = contact

The attributes __name and __contact are protected, meaning they can't be accessed like this:

code:
user = User("John", "12345")
print(user.__name)  # This will raise an AttributeError

But you can access them through the provided methods:
code:
print(user.get_name())  # This will work, as it's the intended interfa


2.@staticmethod:
This method doesn't need access to any instance or class-specific attributes, 
like: Classname.methodname()

so it’s defined as a static method. 
It's just a utility function to process a payment based on the given arguments 
(payment_method and amount).
Thus, it can be called directly from the class without needing to create an instance,like:
code:
Payment.process_payment("Credit Card", 150)


Example of @staticmethod:
Code:

class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

# Call static method using class
result = MathOperations.add_numbers(5, 3)#Classname.methodname()
print(result)  # Output: 8

# Call using an instance(It's the general way of calling any method of the class)
math_ops = MathOperations()
result = math_ops.add_numbers(10, 7)
print(result)  # Output: 17



3.raise NotImplementedError("Subclasses must implement fare calculation")
The line raise NotImplementedError("Subclasses must implement fare calculation") 
is used in a method to indicate that the method is intentionally left unimplemented in the 
base class and must be implemented by any subclass that inherits from it. 
It's commonly used in abstract methods within a base class to enforce certain behaviors 
in subclasses.

Detailed Explanation:
Why Use NotImplementedError?
(i)In OOP, sometimes you want to define a general concept in a base class but leave specific 
details to be implemented by subclasses. In this case, the base class (Vehicle) 
defines the structure of a method (calculate_fare), 
but it doesn't know how to compute the fare because different vehicles (like cars, bikes, or vans)
will have different fare structures.

(ii)To ensure that any subclass that inherits from Vehicle implements this method, 
we raise NotImplementedError. This prevents the base class from being used directly 
without overriding the method in a subclass.


What Happens If You Don’t Implement It in Subclasses?

If a subclass (like Car, Bike, or Van) does not override the calculate_fare method,
and you attempt to call it, Python will raise the NotImplementedError, for example:

code:
class Airplane(Vehicle):
    pass  # Did not implement calculate_fare

plane = Airplane("XYZ123")
plane.calculate_fare(10)  # This will raise NotImplementedError

Output:
NotImplementedError: Subclasses must implement fare calculation


Why Is This Useful?
Forcing Subclasses to Implement Essential Methods:
Abstract Base Class Behavior:
   


4."driver": self.__driver.get_name() if self.__driver else "Not assigned"

is a conditional (or ternary) expression in Python,which is used to assign a value based on a condition.

Meaning of This Line:
The goal of this line is to display the name of the driver associated with the ride, 
but only if a driver has been assigned. If no driver has accepted the ride yet, 
it will display "Not assigned".


This is a one-line if-else expression,where:
self.__driver.get_name() is executed if self.__driver is not None(i.e.,a driver has been assigned).

"Not assigned" is used if self.__driver is None (i.e.,no driver has been assigned yet).

Example:

When a ride is created but no driver has accepted it yet:

code:

ride = Ride(rider, "Downtown", 15)
print(ride.get_ride_details())

Output (since no driver is assigned):
{
  "rider": "John Doe",
  "driver": "Not assigned",
  "destination": "Downtown",
  "distance": 15
}


After a driver accepts the ride:
code:

driver1.accept_ride(ride)
print(ride.get_ride_details())

Output (now a driver is assigned):
{
  "rider": "John Doe",
  "driver": "Alex Rider",
  "destination": "Downtown",
  "distance": 15
}



5.if self.__driver and self.__driver.vehicle:
            return self.__driver.vehicle.calculate_fare(self.__distance)


(i)The if self.__driver and self.__driver.vehicle: condition checks if both:

A driver has been assigned (self.__driver is not None).
The assigned driver has a vehicle.

If both conditions are true, it proceeds to the next line.


self.__driver.vehicle.calculate_fare(self.__distance):
This line calls the calculate_fare() method on the driver's vehicle object.

self.__driver.vehicle: Refers to the vehicle object (which could be a Car, Bike, or Van) associated with the driver.

calculate_fare(self.__distance): The vehicle's calculate_fare() method is called with the distance of the ride (self.__distance). This method is polymorphic, meaning the fare calculation is different for each type of vehicle:
        A car may charge more per kilometer than a bike.
        A van may charge even more due to its capacity.
Example:
If it's a car and the distance is 15 km, the fare might be 15 * 10 = 150.


Return 0 if No Driver or Vehicle:
If either self.__driver or self.__driver.vehicle is None (i.e., there is no driver or no vehicle associated with the driver), the method returns 0.

This means if no driver has accepted the ride, or if the driver doesn't have a vehicle, the system assumes no fare should be calculated.

'''

