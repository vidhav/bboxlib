# BoundingBox

A Python class for working with bounding boxes.

## Requirements
- Python 3.10 or higher

## Installation

**bboxlib** is available on [PyPI](https://pypi.org/project/bboxlib/) (the Python Package Index), and can be installed using pip:

```sh
pip install bboxlib
```

## Usage

Import the BoundingBox class and use it to handle bounding boxes.

```python
from bboxlib import BoundingBox

bbox = BoundingBox(1.0, 2.0, 3.0, 4.0)

bbox.extend(0.9, 1.9, 3.1, 4.1)

print(bbox.extent)
# [0.9, 2.0, 3.0, 4.1]
```

## Author
Håvard Vidme [@vidhav](https://github.com/vidhav)
