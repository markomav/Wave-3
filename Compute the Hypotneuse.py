import math

def Hypotenuse(side1, side2):
    return math.sqrt(side1**2 + side2**2)

side1 = int(input('Input 1st side length: '))
side2 = int(input('Input 2nd side length: '))

print('Length of hypotenuse: ' + str(round(Hypotenuse(side1, side2), 4)))