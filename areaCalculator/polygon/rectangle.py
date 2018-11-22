
# coding: utf-8

# In[1]:


class rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
    
    def setvalues(self):
        self.length = float(input("Enter the length: "))
        self.width = float(input("Enter the width: "))
        
    def area(self):
        return self.length * self.width
    
    def display(self):
        print("The area of this rectangle is: ", self.area())

