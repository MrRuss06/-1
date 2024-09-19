
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QVBoxLayout,
                            QHBoxLayout,QRadioButton,QMessageBox,QLabel)


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People')
main_win.resize(400,200)


title =QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')

v_line = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h1.addWidget(title, alignment=Qt.AlignCenter)
h2.addWidget(btn_answer1, alignment=Qt.AlignCenter)
h2.addWidget(btn_answer2, alignment=Qt.AlignCenter)
h3.addWidget(btn_answer3, alignment=Qt.AlignCenter)
h3.addWidget(btn_answer4, alignment=Qt.AlignCenter)

v_line.addLayout(h1)
v_line.addLayout(h2)
v_line.addLayout(h3)
main_win.setLayout(v_line)
main_win.show()

def show_win():
    win = QMessageBox()
    win.setText('Верно! Вы выиграли гироскутер')
    win.exec_()

def show_lose():
    win = QMessageBox()
    win.setText('Нет, в 2015 году. Вы выиграли фирменный плакат')
    win.exec_()   

btn_answer3.clicked.connect(show_win)
btn_answer2.clicked.connect(show_lose)
btn_answer1.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)

main_win.show()
app.exec()