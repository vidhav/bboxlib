from bboxlib import BoundingBox


def test_alias():
    bbox = BoundingBox(1.0, 2.0, 3.0, 4.0)

    assert bbox.left == bbox.west
    assert bbox.bottom == bbox.south
    assert bbox.right == bbox.east
    assert bbox.top == bbox.north


def test_extend():
    bbox = BoundingBox(1.0, 2.0, 3.0, 4.0)
    bbox.extend(0.9, 2.1, 2.9, 4.1)

    assert bbox.left == 0.9
    assert bbox.bottom == 2.0
    assert bbox.right == 3.0
    assert bbox.top == 4.1
