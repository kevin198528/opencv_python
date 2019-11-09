import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = QWidget()
    win.setWindowTitle('hello')
    win.show()

    sys.exit(app.exec())
