class Dog:
    animal = "dog"
    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    
  
    def display_details(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        print("-" * 20)



dog1 = Dog( "Golden Retriever", "Golden")
dog2 = Dog( "German Shepherd", "Black and Tan")


print("Details of First Dog:")
dog1.display_details()

print("Details of Second Dog:")
dog2.display_details()