# tests/test_viewer_widget.py

import pytest
from PySide6.QtWidgets import QApplication
from viewer.viewer_widget import ViewerWidget


@pytest.fixture
def app():
    return QApplication([])


@pytest.fixture
def viewer_widget(app):
    return ViewerWidget()


def test_viewer_widget_init(viewer_widget):
    assert viewer_widget.gl_widget is not None


def test_zoom_in(viewer_widget):
    initial_distance = viewer_widget.gl_widget.opts["distance"]
    viewer_widget.zoom_in()
    assert viewer_widget.gl_widget.opts["distance"] < initial_distance


def test_zoom_out(viewer_widget):
    initial_distance = viewer_widget.gl_widget.opts["distance"]
    viewer_widget.zoom_out()
    assert viewer_widget.gl_widget.opts["distance"] > initial_distance
