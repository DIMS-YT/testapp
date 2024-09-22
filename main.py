from PyQt6.QtWidgets import (QApplication, QWidget,
                              QLabel, QPushButton, 
                              QVBoxLayout, QHBoxLayout,
                              QMessageBox, QRadioButton)

app = QApplication([])
win = QWidget()

win.setWindowTitle('секрет')
win.resize(400,300)

question = QLabel("Яка найменша країна світу?")

answer_1 = QRadioButton("Непал")
answer_2 =  QRadioButton("Андорра")
answer_3 =  QRadioButton("Ватикан")
answer_4 =  QRadioButton("Єгипет")
answer_5 =  QRadioButton("Ліхтенштейн")
answer_6 =  QRadioButton("Йорданія")


main_layout = QVBoxLayout()

main_layout.addWidget(question)

h_line_1 = QHBoxLayout()
h_line_1.addWidget(answer_1)
h_line_1.addWidget(answer_2)
h_line_1.addWidget(answer_3)

main_layout.addLayout(h_line_1)

h_line_2 = QHBoxLayout()
h_line_2.addWidget(answer_4)
h_line_2.addWidget(answer_5)
h_line_2.addWidget(answer_6)

main_layout.addLayout(h_line_2)


def show_winner():
    message_box = QMessageBox()
    message_box.setText("Правильно! Ти виграв 100гривень")
    message_box.exec()  

def show_lose():
    message_box = QMessageBox()
    message_box.setText("Неправильно! Ти програв 100гривень")
    message_box.exec()  

answer_1.clicked.connect(show_lose)
answer_2.clicked.connect(show_lose)
answer_3.clicked.connect(show_winner)
answer_4.clicked.connect(show_lose)
answer_5.clicked.connect(show_lose)
answer_6.clicked.connect(show_lose)





win.setLayout(main_layout)
win.show()
app.exec()