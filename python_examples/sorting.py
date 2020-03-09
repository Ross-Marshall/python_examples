
earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]

earth_metals.sort()
print(str(earth_metals))

earth_metals.sort(reverse=True)
print(str(earth_metals))

earth_metals_tuple = ("Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")

""" Can't sort tuples
earth_metals.sort()
print(str(earth_metals))

earth_metals.sort(reverse=True)
print(str(earth_metals))
"""

planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
]

size = lambda planets: planets[1]
planets.sort(key=size, reverse=True)

print(str(planets))

density = lambda planets: planets[2]
planets.sort(key=density)

print('---- sorted plants ----')
print(str(planets))

data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)

print('---- sorted data tupple -----')
print(str(sorted(data)))

print('---- original data tupple ----')
print(str(data))

print(sorted("Alphabetical"))
