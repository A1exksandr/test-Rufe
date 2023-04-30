# напиши здесь код для второго экрана приложения
#подключаем модуль с направляющими линиями
from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import (QApplication, QWidget, 
QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QPushButton, QListWidget, QLineEdit
)

#создаём объект приложения
app = QApplication([])
# создаём объект главного окна
my_win = QWidget()
from final_win import *
from instr import *

class TextWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_instruction)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.txt_name)
        self.l_line.addWidget(self.txt_hintname)
        self.l_line.addWidget(self.txt_hintage)
        self.l_line.addWidget(self.txt_test1)
        self.l_line.addWidget(self.txt_test2)
        self.l_line.addWidget(self.txt_test3)
        self.l_line.addWidget(self.txt_sendresults)
        self.l_line.addWidget(self.txt_hinttest1)
        self.l_line.addWidget(self.txt_hinttest2)
        self.l_line.addWidget(self.txt_hinttest3)
        self.l_line.addWidget(self.txt_starttest1)
        self.l_line.addWidget(self.txt_starttest2)
        self.l_line.addWidget(self.txt_starttest3)
        self.r_line.addWidget(self.txt_age)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.hide()
        FinalWin()
