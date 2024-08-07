# viewer_widget.py

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QWheelEvent
import pyqtgraph.opengl as gl
import numpy as np
from .file_loader import FileLoader


class ViewerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.gl_widget = gl.GLViewWidget()
        self.layout.addWidget(self.gl_widget)

        self.vertices = None
        self.faces = None
        self.mesh_item = None

        self.gl_widget.setCameraPosition(distance=40, elevation=8)

    def load_obj(self, file_path):
        data = FileLoader.load_obj(file_path)
        self.vertices, self.faces = FileLoader.parse_obj(data)
        self.update_viewer()

    def update_viewer(self):
        if self.mesh_item:
            self.gl_widget.removeItem(self.mesh_item)

        vertices = np.array(self.vertices)
        faces = np.array(self.faces) - 1  # OBJ indices are 1-based

        self.mesh_item = gl.GLMeshItem(
            vertexes=vertices, faces=faces, drawEdges=True, edgeColor=(1, 1, 1, 1)
        )
        self.gl_widget.addItem(self.mesh_item)

    def zoom_in(self):
        self.gl_widget.opts["distance"] *= 0.9

    def zoom_out(self):
        self.gl_widget.opts["distance"] /= 0.9

    def enable_pan(self):
        self.gl_widget.pan(0, 0, 0)

    def reset_view(self):
        self.gl_widget.setCameraPosition(distance=40, elevation=8)

    def mousePressEvent(self, event: QMouseEvent):
        if event.modifiers() == Qt.ControlModifier:
            if event.button() == Qt.LeftButton:
                self.enable_pan()
            elif event.button() == Qt.RightButton:
                # Add rotate logic here
                pass

    def wheelEvent(self, event: QWheelEvent):
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()
