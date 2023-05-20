import sys

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.setWindowTitle("tieba-thread-archive-simple-pyside-ui")
    window.show()
    sys.exit(app.exec())
