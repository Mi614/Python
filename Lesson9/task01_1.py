import sys
from PyQt5.QtWidgets import QFrame, QApplication, QWidget
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from itertools import cycle


class TrafficLight(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)

        self.square = QFrame(self)
        self.square.setGeometry(90, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Traffic Light')
        self.show()

        self.my_dict = {5: (255, 0, 0), 2: (204, 168, 60), 3: (100, 200, 0)}
        self.my_iter = cycle(self.my_dict)
        self.timer = QTimer()
        self.timer.start(1)
        self.timer.timeout.connect(self.on_timeout)

    def on_timeout(self):
        ti = next(self.my_iter)
        color = self.my_dict[ti]
        self.timer.start(ti * 1000)
        self.col.setRgb(*color)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TrafficLight()
    sys.exit(app.exec_())