class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    p = Point(1,2)
    print(str(p))
    print(str(p.x))
    print(str(p.y))