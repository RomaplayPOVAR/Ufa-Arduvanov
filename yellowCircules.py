import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 800
        self.height = 600
        self.isCanPaint = False

        self.setGeometry(0, 0, self.width, self.height)
        self.btn = QPushButton('Click me', self)
        self.btn.setGeometry(self.width // 2 - 50, self.height // 2 - 25, 100, 50)
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.isCanPaint = True
        self.update()

    def paintEvent(self, event):
        if self.isCanPaint:
            self.paint = QPainter()
            self.paint.begin(self)
            self.DrawYellowCircule()
            self.paint.end()
        self.isCanPaint = False

    def DrawYellowCircule(self):
        x0 = random.randint(0, self.width)
        y0 = random.randint(0, self.height)

        self.paint.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        d = random.randint(20, min(self.width, self.height) // 2)
        self.paint.drawEllipse(x0, y0, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()

    w.show()
    sys.exit(app.exec_())
