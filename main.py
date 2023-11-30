from PyQt5 import uic
from sys import argv, exit
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Ui.ui', self)
        self.show()


class Main(Ui, QMainWindow):
    def __init__(self):
        super().__init__()
        self.a = randint(1, 100)
        self.draw = False
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black']
        self.circle = QPushButton("press", self)
        self.circle.resize(50, 50)
        self.circle.move(175, 300)
        self.circle.show()
        self.circle.clicked.connect(self.click)

    def click(self):
        self.draw = True
        self.a = randint(1, 100)

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def drawing(self, qp):
        qp.setBrush(QColor("Yellow"))

        qp.drawEllipse(100, 100, self.a, self.a)
        self.update()


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())
