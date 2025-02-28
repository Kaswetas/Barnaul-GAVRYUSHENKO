import random
import sys

from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    def __init__(self, size):
        super().__init__()
        self.setWindowTitle('Git и случайные окружности')
        self.setGeometry(0, 0, *size)
        self.push_btn = QPushButton(self)
        self.push_btn.setText('Push me!')
        self.push_btn.setGeometry(259, 5, 250, 50)
        self.push_btn.clicked.connect(self.update)

    def paintEvent(self, event):
        self.painter = QPainter(self)
        self.painter.setBrush(QBrush(QColor(random.randint(0, 255), random.randint(0, 255),
                                             random.randint(0, 255))))
        a = random.randint(10, 100)
        self.painter.drawEllipse(random.randint(0, 768), random.randint(0, 768), a, a)
        self.painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example((768, 768))
    ex.show()
    sys.exit(app.exec())