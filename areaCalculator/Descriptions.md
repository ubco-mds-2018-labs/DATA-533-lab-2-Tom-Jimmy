
## Package Description
The package areaCalculator aims at providing the users an efficient way to calculate the area of commonly used 2D shapes. This package contains two sub packages, polygon and curved. The polygon sub-package contains the modules for calculating the areas of rectangle, triangle, trapezoid and regular polygon based on dimensions given by the user. The curved sub-package contains the modules for calculating areas of circle and ellipse.

## Function Description
Here is the description of how each type of shape is calculated.
- Regular polygon:
The regular polygon module has similar structure to the rectangle module except that the user is required to provide the length and number of sides. The area is calculated using the formula (num_sides*length**2/(4*tan(pi/self.num_sides).


- Circle:
The circle module has similar structure to the rectangle module except that the user is required to provide the radius of the circle. The area is calculated using the formula (pi*radius*radius).


- Ellipse:
The ellipse module has similar structure to the rectangle module except that the user is required to provide the major (a) and minor (b) axis of the ellipse. The area is calculated using the formula (pi*a*b).


## Test File Description


A user-interactive python test file is provided to allow specifying the type of the shape which directly corresponds to the modules/classes for the calculation. By executing the test file, the user is required to input the name of the shape until "quit" command is provided:

r: Rectangle 

c: Circle 

e: Ellipse 

rp: Regular Polygon 

t: Trapezoid 

tr: Triangle 

q: Quit


