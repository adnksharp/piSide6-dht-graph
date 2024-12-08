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
    def __init__(self):
        fig = Figure(facecolor=QPalette().color(QPalette.Window).name())
        fig.set_tight_layout(True)

        self.axes = fig.add_subplot(111, facecolor=QPalette().color(QPalette.Window).name())
        self.axes.get_xaxis().set_visible(False)
        self.axes.get_yaxis().set_visible(False)
        
        for spine in self.axes.spines.values():
            spine.set_edgecolor(QPalette().color(QPalette.Window).name())

        super(Canvas, self).__init__(fig)

    def update(self, xp, data):
        self.axes.clear()
        self.axes.plot(xp, data, color=colors['on'], linewidth=2)
        self.axes.set_xlim(0, 29.5)
        if SType == 11:
            self.axes.set_ylim(0, 59)
        else:
            self.axes.set_ylim(-40, 125)

class Board():
    def __init__(self, parent):
        self.parent = parent
        
        self.data = []
        self.ino = arduino.Pymata4()
        self.ino.set_pin_mode_dht(SPin, sensor_type=SType, callback=self.update)
        
    def update(self, data):
        self.data = [data[4], data[5], (data[5]* 9 / 5) + 32]
        self.parent.dhtH.setText(str(self.data[0]))
        self.parent.dhtC.setText(str(self.data[1]))
        self.parent.dhtF.setText(str(self.data[2]))

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.label = [i for i in range(60)]
        self.temp = [0 for _ in range(60)]
        # self.hum = [0 for _ in range(60)]
        
        self.board = Board(self.ui)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.updates)
        self.timer.start(1000)
        
    def clearHeaders(self, layout):
        if layout is not None:
            for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                if item.widget():
                    widget = item.widget()
                    widget.deleteLater()
                elif item.layout():
                    self.clearHeaders(item.layout())
        
    def updates(self):
        self.temp.pop()
        # self.hum.pop()
        self.temp.insert(0, self.board.data[1])
        # self.hum.insert(0, self.sensor.data[1])
        
        graph = Canvas()
        graph.update(self.label, self.temp)
        self.clearHeaders(self.ui.graphs)
        self.ui.graphs.addWidget(graph)
        
    def closeEvent(self, event):
        self.board.ino.shutdown()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
