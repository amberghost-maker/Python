class Vehicle:

 def __init__ (self, name, max_speed, mileage):
  self.name = name
  self.max_speed = max_speed
  self.mileage = mileage
class BUS(Vehicle):
     pass
School_bus =BUS("School volvo", 189, 12)
print("Vehicle Name:", School_bus.name, "speed:", School_bus.max_speed,"Mileage:", School_bus.mileage)