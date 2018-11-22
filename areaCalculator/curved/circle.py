
# coding: utf-8

# In[1]:


from math import pi
class circle:
    def __init__(self,radius=0):
        self.radius = radius
        
    def setvalues(self):
        self.radius = float(input("Enter the radius: "))
        
    def area(self):
        return pi*self.radius**2
    
    def display(self):
        print("The area for this circle is: ", self.area())

