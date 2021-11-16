import sys
import random
from PyQt5 import uic

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.button_draw)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        n = random.randint(10, 20)
        for i in range(1, n):
            x = random.randint(50, 350)
            y = random.randint(100, 450)
            r = random.randint(20, 50)
            qp.drawEllipse(x, y, r, r)

    def button_draw(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())