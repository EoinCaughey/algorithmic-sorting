import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
import sys
import time

lst = list(map(int, input("Input a list of integers:").split(",")))
n = len(lst)

app = QtWidgets.QApplication([])
win = pg.GraphicsLayoutWidget(show=True)
plot = win.addPlot()
plot.setYRange(0, max(lst) + 5)

bar_item = pg.BarGraphItem(x=range(n), height=lst, width=0.6, brush='c')
plot.addItem(bar_item)

def update_bars():
    global bar_item
    plot.removeItem(bar_item)
    bar_item = pg.BarGraphItem(x=range(n), height=lst, width=0.6, brush='c')
    plot.addItem(bar_item)
    QtWidgets.QApplication.processEvents()
    time.sleep(0.00)

def bubblesort():
    j = 0
    while j < 100:
        for i in range(n-1):
            first = lst[i]
            second = lst[i+1]
            if second == [None]:
                i = 0                
            elif (first <= second):
                continue
            elif first > second:
                mem = second
                lst[i+1] = first
                lst[i] = mem
                update_bars()
            i =+ 1

bubblesort()

sys.exit(app.exec())
