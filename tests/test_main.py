from bboxlib import BoundingBox


def test_alias():
    bbox = BoundingBox(1.0, 2.0, 3.0, 4.0)

    assert bbox.left == bbox.west == bbox.minx
    assert bbox.bottom == bbox.south == bbox.miny
    assert bbox.right == bbox.east == bbox.maxx
    assert bbox.top == bbox.north == bbox.maxy


def test_extend():
    bbox = BoundingBox(1.0, 2.0, 3.0, 4.0)
    bbox.extend(0.9, 2.1, 2.9, 4.1)

    assert bbox.left == 0.9
    assert bbox.bottom == 2.0
    assert bbox.right == 3.0
    assert bbox.top == 4.1


def test_iter():
    bbox = BoundingBox(1.0, 2.0, 3.0, 4.0)

    assert dict(bbox) == {"left": 1.0, "bottom": 2.0, "right": 3.0, "top": 4.0}


def test_repr():
    bbox = BoundingBox(1.0, 2.0, 3.0, 4.0)

    assert repr(bbox) == "BoundingBox(1.0, 2.0, 3.0, 4.0)"
