# toolbar.py

from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QIcon, QAction


class ToolBar(QToolBar):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        open_action = QAction(QIcon("resources/icons/open.png"), "Open", self)
        open_action.triggered.connect(self.main_window.open_file)
        self.addAction(open_action)

        zoom_in_action = QAction(QIcon("resources/icons/zoom_in.png"), "Zoom In", self)
        zoom_in_action.triggered.connect(self.main_window.viewer_widget.zoom_in)
        self.addAction(zoom_in_action)

        zoom_out_action = QAction(
            QIcon("resources/icons/zoom_out.png"), "Zoom Out", self
        )
        zoom_out_action.triggered.connect(self.main_window.viewer_widget.zoom_out)
        self.addAction(zoom_out_action)

        pan_action = QAction(QIcon("resources/icons/pan.png"), "Pan", self)
        pan_action.triggered.connect(self.main_window.viewer_widget.enable_pan)
        self.addAction(pan_action)

        reset_view_action = QAction(
            QIcon("resources/icons/reset_view.png"), "Reset View", self
        )
        reset_view_action.triggered.connect(self.main_window.reset_view)
        self.addAction(reset_view_action)
