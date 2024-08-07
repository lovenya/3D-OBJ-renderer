# error_handler.py

from PySide6.QtWidgets import QMessageBox


class ErrorHandler:
    @staticmethod
    def show_error(message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.exec()
