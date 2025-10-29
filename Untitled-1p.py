import math  
#class circle():
  
    #def __init__ (self):
       # self.str1 = ""
   # def get_string(self):
      #  self.str1 = input(int('Enter the radius:'))
    #    self.str2 = math.pi*self.str1 
    #def print_string(self):
      #  print('Result is :', self.str2)
Radius = int(input('What is the radius?'))
Perimeter = math.pi*Radius*2
Area = math.pi*Radius**2
print('The perimeter of the circle is',Perimeter)
