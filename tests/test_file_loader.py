# tests/test_file_loader.py

import pytest
from viewer.file_loader import FileLoader


def test_load_obj_valid_file():
    data = FileLoader.load_obj("tests/test.obj")
    assert data is not None


def test_load_obj_invalid_file():
    with pytest.raises(ValueError):
        FileLoader.load_obj("tests/test.txt")


def test_parse_obj():
    data = "v 1.0 1.0 1.0\nv 2.0 2.0 2.0\nf 1 2 3\n"
    vertices, faces = FileLoader.parse_obj(data)
    assert len(vertices) == 2
    assert len(faces) == 1
