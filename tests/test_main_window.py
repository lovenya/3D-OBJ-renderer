# tests/test_main_window.py

import pytest
from PySide6.QtWidgets import QApplication
from viewer.main_window import MainWindow


@pytest.fixture
def app():
    return QApplication([])


@pytest.fixture
def main_window(app):
    return MainWindow()


def test_main_window_init(main_window):
    assert main_window.windowTitle() == "3D OBJ Viewer"
    assert main_window.viewer_widget is not None
    assert main_window.toolbar is not None
