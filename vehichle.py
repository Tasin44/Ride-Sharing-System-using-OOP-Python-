class Vehicle:
    def __init__(self,licence_plate):
        self.license_plate =licence_plate
    def calculate_fare(self,distance):
        raise NotImplementedError("Subclasses must implement fare calculation")