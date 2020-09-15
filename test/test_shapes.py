import shapes.calculate as sc


def test_shapes_rectangle():
    tr = sc.Rectangle(2, 3, 0)
    assert tr.area() == 6
    assert tr.perimeter() == 10
    assert tr.volume() == 0


def test_shapes_square():
    ts = sc.Square(3)
    assert ts.area() == 9
    assert ts.perimeter() == 12
    assert ts.volume() == 0


def test_shapes_cube():
    tc = sc.Cube(3)
    assert tc.perimeter() == 54
    assert tc.volume() == 27


def test_shapes_box():
    tb = sc.Box(2, 3, 1)
    assert tb.area() == 6
    assert tb.perimeter() == 36
    assert tb.volume() == 6
    assert tb.surface_area() == 22
