# main_window.py

from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox,
)
from .toolbar import ToolBar
from .viewer_widget import ViewerWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("3D OBJ Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.viewer_widget = ViewerWidget(self)
        self.setCentralWidget(self.viewer_widget)

        self.toolbar = ToolBar(self)
        self.addToolBar(self.toolbar)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open OBJ File", "", "OBJ Files (*.obj)"
        )
        if file_name:
            try:
                self.viewer_widget.load_obj(file_name)
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def reset_view(self):
        self.viewer_widget.reset_view()
