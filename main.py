import sys
import io
import PyQt5.uic as uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randrange


ui = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>10</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Нарисовать</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Painter(QMainWindow):
    def __init__(self):
        super().__init__()
        temp = io.StringIO(ui)
        uic.loadUi(temp, self)
        self.need_new = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.need_new = True
        self.update()

    def paintEvent(self, event):
        if self.need_new:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            count = randrange(1, 10)
            for _ in range(count):
                x, y, r = randrange(50, 700), randrange(50, 500), randrange(10, 100)
                qp.drawEllipse(x, y, r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Painter()
    ex.show()
    sys.exit(app.exec_())
