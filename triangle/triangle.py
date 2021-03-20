import sys
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.A = sqrt((x.x - y.x)**2+(x.y - y.y)**2)
        self.B = sqrt((y.x - z.x)**2+(y.y - z.y)**2)
        self.C = sqrt((x.x - z.x)**2+(x.y - z.y)**2)

    def check_triangle(self):
        if (self.B >= self.A + self.C) or (self.A >= self.B + self.C) or (self.C >= self.A + self.B):
            return 0
        else:
            return 1
    def check_isos(self):
        if self.A == self.B or self.A == self.C or self.B == self.C:
            return 1
        else:
            return 0

    def get_square(self):
        p = (self.A + self.B + self.C) / 2
        return sqrt(p * (p - self.A) * (p - self.B) * (p - self.C))

class FileUtils:
    def __init__(self, file_from):
        self.read = open(file_from)

    def get_all_lines(self):
        all_triangle = self.read.readlines()
        for i in range(len(all_triangle)):
            all_triangle[i] = all_triangle[i].split()
        return all_triangle

    def __del__(self):
       self.read.close()

def Write(file_to, text):
    text = str(text)
    f = open(file_to, 'w')
    f.write(text)
    f.close()

def main(file_from, file_to):
    set_of_points = FileUtils(file_from)
    set_of_points = set_of_points.get_all_lines()
    M = 0
    for i in range(len(set_of_points)):
        for j in range(len(set_of_points[i])):
            set_of_points[i][j] = float(set_of_points[i][j])
        x = Point(set_of_points[i][0], set_of_points[i][1])
        y = Point(set_of_points[i][2], set_of_points[i][3])
        z = Point(set_of_points[i][4], set_of_points[i][5])
        Trigle = Triangle(x, y, z)
        if Trigle.check_triangle() and Trigle.check_isos():
            if Trigle.get_square() > M:
                M = Trigle.get_square()

    Write(file_to, M)

if __name__ == "__main__":
     files = sys.argv
     main(files[1], files[2])