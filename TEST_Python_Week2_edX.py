import math 
'''
Function is expected to receive n (number of sides) and s (side lenght).
Both numbers must be > 0.
Function sums the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.'''

def polysum(n,s):
  area = (0.25*n*s**2) / (math.tan(math.pi/n))
  perimeter_square = (n*s)**2
  result = round(area + perimeter_square, 4)

  return result