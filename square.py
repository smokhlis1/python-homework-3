from math import pi

def find_area():
    print("Please input the dimensions of the house:")
    length = float(input("Length: "))
    width = float(input("Height: "))

    square_area = length * width
    print("The square footage of the house is", square_area, "square feet")

def find_circumference():
    print("Let me help you figure out the radius of a circle: ")
    radius = float(input("Please input the radius:"))

    circumference = 2 * pi * radius

    print("If you were to do it yourself instead of asking me, it's 2 * pi * radius, however you've asked me so here it is: ", circumference, "sq ft.")
    


find_area()

find_circumference()
