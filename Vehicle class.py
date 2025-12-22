class Vehicle:
    def __init__(self, seating_capacity=50):
        self.seating_capacity = seating_capacity
    
    def fare(self):
        """Calculate the base fare: seating_capacity * 100"""
        return self.seating_capacity * 100


class Bus(Vehicle):
    def __init__(self, seating_capacity=50):
        super().__init__(seating_capacity)
    
    def fare(self):
        """Override the fare method to add 10% maintenance charge for Bus"""
        base_fare = super().fare()  # Total fare = seating_capacity * 100
        maintenance_charge = base_fare * 0.10
        final_fare = base_fare + maintenance_charge
        return final_fare


# Example usage
bus = Bus(seating_capacity=50)
print(f"The final fare for the bus is INR {bus.fare()}")  # Output: The final fare for the bus is INR 5500.0