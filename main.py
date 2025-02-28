import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QBrush, QColor
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        self.painter = QPainter(self)
        self.painter.setBrush(QBrush(QColor('yellow')))
        a = random.randint(10, 100)
        self.painter.drawEllipse(random.randint(0, 768), random.randint(0, 768), a, a)
        self.painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())