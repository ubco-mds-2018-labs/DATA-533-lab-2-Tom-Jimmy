
# coding: utf-8

# In[1]:


class trapezoid:
    def __init__(self, top=0, bottom=0, height=0):
        self.top = top
        self.bottom = bottom
        self.height = height
    
    def setvalues(self):
        self.top = float(input("Enter the top length: "))
        self.bottom = float(input("Enter the bottom length: "))
        self.height = float(input("Enter the height: "))
    
    def area(self):
        return (self.top + self.bottom) * self.height/2
    
    def display(self):
        print("The area of this trapezoid is: ", self.area())

