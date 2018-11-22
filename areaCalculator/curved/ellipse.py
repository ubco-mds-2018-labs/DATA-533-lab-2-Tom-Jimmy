
# coding: utf-8

# In[1]:


from math import pi
class ellipse:
    def __init__(self, ax_A=0, ax_B=0):
        self.ax_A = ax_A
        self.ax_B = ax_B
    
    def setvalues(self):
        self.ax_A = float(input("Enter the major axis length: "))
        self.ax_B = float(input("Enter the minor axis length: "))
        
    def area(self):
        return(pi*self.ax_A*self.ax_B)
    
    def display(self):
        print("The area of this ellipse is: ", self.area())

