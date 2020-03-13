# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides have the same length.
# Equalateral triangle: All sides are equal.

a = int(raw_input("The length of side a = "))
b = int(raw_input("The length of side b = "))
c = int(raw_input("The length of side c = "))

if a != b and b != c and a != c:
  print("This is a scalene triangle.")
elif a == b and b == c and a == c:
  print("This is a equlateral triangle.")
else:
  print("This is a isosceles triangle.")

