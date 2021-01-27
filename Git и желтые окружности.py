import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import QRect,Qt
from PyQt5.QtGui import QPainter,QBrush, QPen
from PyQt5 import QtCore


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.should_paint_circle = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            s = random.randint(5, 100)
            painter = QtGui.QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(QPen(Qt.yellow, s, Qt.SolidLine))
            painter.drawEllipse(640 // 2, 480 // 2, s, s)

    def run(self):
        self.should_paint_circle = True
        self.update()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
