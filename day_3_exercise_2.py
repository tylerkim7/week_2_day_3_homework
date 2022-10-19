from cmath import pi


def sqft(length, width):
    intlength = int(length)
    intwidth = int(width)
    area = intlength * intwidth
    return f"The square footage of the house is {area}."

def circumference(radius):
    intradius = int(radius)
    circ = 2 * pi * radius
    return f"The circumference of the circle is {circ}."