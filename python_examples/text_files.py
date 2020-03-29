f = open('text_files/guido_bio.txt')
text = f.read()
f.close()
print(text)

with open("text_files/guido_bio.txt") as fobj:
    bio = fobj.read()

print(bio)

try:
    with open("text_files/future_winning_lotto_numbers.txt") as fobj:
        text2 = fobj.read()
except IOError:
    text2 = None

print(text2)


try:
    with open("text_files/guido_bio.txt") as fobj:
        text3 = fobj.read()
except IOError:
    text3 = None

print(text3)

oceans = ['Pacific', 'Atlantic', 'Arctic', 'Indian', 'Southern']

with open('text_files/oceans.txt', 'w') as f:
    for ocean in oceans:
        f.write(ocean)
        f.write('\n')

""" python 3
oceans = ['Pacific', 'Atlantic', 'Arctic', 'Indian', 'Southern']

with open('text_files/oceans2.txt', 'w') as f:
    for ocean in oceans:
        print(ocean, file=f)
"""

with open('text_files/oceans.txt', 'a') as f:
    for ocean in oceans:
        f.write(ocean)
        f.write('\n')