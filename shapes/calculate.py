class Rectangle():
    def __init__(self, length, width, height=0):
        self.length = length
        self.width = width
        self.height = height

    def __repr__(self):
        if not self.height:
            return (f"{self.__class__.__name__}("
                    f"{self.length!r}, {self.width!r})")
        else:
            return (f"{self.__class__.__name__}("
                    f"{self.length!r}, {self.width!r}, {self.height!r})")

    def __str__(self):
        if not self.height:
            return (f"A {self.__class__.__name__} "
                    f"of length: {self.length!r}, and width: {self.width!r}")
        else:
            return (f"A {self.__class__.__name__} "
                    f"of length: {self.length!r}, width: {self.width!r}, "
                    f"height: {self.height!r}")

    def area(self):
        if not self.height:
            return self.length * self.width
        else:
            return self.length * self.width * self.height

    def perimeter(self):
        if not self.height:
            return 2 * (self.length + self.width)
        else:
            return 6 * (self.length + self.width + self.height)

    def volume(self):
        if not self.height:
            return 0
        else:
            return self.length * self.width * self.height


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Cube(Rectangle):
    def __init__(self, length):
        super().__init__(length, length, length)

    def surface_area(self):
        face_area = self.area()
        return face_area * 6


class Box(Rectangle):

    def surface_area(self):
        l_w = self.length * self.width
        w_h = self.width * self.height
        l_h = self.length * self.height
        return 2 * (l_w + w_h + l_h)
