from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ThreadSecundario(QThread):
    sec_values = QtCore.pyqtSignal(QPoint, QPainter, int, int)

    def __init__(self, point, draw, angle, energy):
        super().__init__()
        self.point = point
        self.draw = draw
        self.angle = angle
        self.energy = energy

    @QtCore.pyqtSlot()
    def run(self):
        while(True):
            self.sec_values.emit(self.point, self.draw, self.angle, self.energy)
