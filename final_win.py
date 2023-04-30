# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import (QApplication, QWidget, 
QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QPushButton, QListWidget, QLineEdit
)

#создаём объект приложения
app = QApplication([])
# создаём объект главного окна
my_win = QWidget()

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.txt_index)
        self.l_line.addWidget(self.txt_workheart)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
