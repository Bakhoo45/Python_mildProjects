# Digital Clock

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__() 

        self.label = QLabel(self)
        self.Timer = QTimer(self)
        self.initUI()
        self.Timer.timeout.connect(self.update_time)

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(700, 500, 500, 200)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 100px; font-weight: bold;font-family : Arial; color: #5ff545; background-color: black; ")
        current_dir = os.path.dirname(os.path.realpath(__file__))
        font_path = os.path.join(current_dir, "DS-DIGIT.TTF")
        if os.path.exists(font_path):
            font_id = QFontDatabase.addApplicationFont(font_path)
            if font_id != -1 and QFontDatabase.applicationFontFamilies(font_id):
                font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            else:
                font_family = "Arial"
        else:
            print(f"Font file not found at: {font_path}")
            font_family = "Arial"  
        my_font = QFont(font_family, 100)
        self.label.setFont(my_font)
        self.Timer.timeout.connect(self.update_time)
        self.Timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime()
        display_text = current_time.toString('hh:mm:ss AP')
        self.label.setText(display_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())