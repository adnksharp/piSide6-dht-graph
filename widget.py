import sys
from pymata4 import pymata4 as arduino

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPalette
from PySide6.QtCore import QTimer

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


colors = {
        'high': '#5bf2fa',
        'low': '#2c3e7f',
        'on': '#f75d54',
        'off': '#812b2d'
        }
SPin = 2
SType = 11

class Canvas(FigureCanvas):
    def __init__(self, *args):
        fig = Figure(facecolor=QPalette().color(QPalette.Window).name())
        fig.set_tight_layout(True)

        self.axes = fig.add_subplot(111, facecolor=QPalette().color(QPalette.Window).name())
        self.axes.tick_params(labelcolor=colors['off'], color=colors['on'])

        for spine in self.axes.spines.values():
            spine.set_edgecolor(colors['high'])

        super(Canvas, self).__init__(fig)

    def update(self, xp, data, lim):
        self.axes.clear()
        self.axes.plot(xp, data, color=QPalette().color(QPalette.Text).name(), linewidth=2)
        self.axes.set_xlim([lim[0], lim[1]])

class Board():
    def __init__(self):
        self.data = []
        self.ino = arduino.Pymata4()
        self.ino.set_pin_mode_dht(SPin, sensor_type=SType, callback=self.update)
        
    def update(self, data):
        self.data = [data[4], data[5], (data[5]* 9 / 5) + 32]

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.board = Board()
        
        
    def closeEvent(self, event):
        self.board.ino.shutdown()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
