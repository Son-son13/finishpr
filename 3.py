from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QComboBox, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
import sys
import sqlite3
import random


class FirstForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 200, 350, 200)
        self.setWindowTitle('Добро пожаловать в игру виселица!')
        self.label = QLabel("Добро пожаловать! Выберите тему для игры!", self)
        self.setStyleSheet('background: rgb(250, 231, 173);')
        self.label.resize(300, 100)
        self.label.move(20, 40)

        self.combo = QComboBox(self)
        self.combo.resize(200, 40)
        self.combo.addItem("Темы")
        self.combo.addItem("Растения")
        self.combo.addItem("Животные")
        self.combo.addItem("Компьютеры и техника")
        self.combo.addItem("Кулинария")
        self.combo.currentTextChanged.connect(self.onChanged)

    def onChanged(self, text):
        self.thema = text
        if self.thema != "Темы":
            self.ex1 = AddWindow(self.thema)
            self.ex1.setStyleSheet('background: rgb(250, 231, 173);')
            self.ex1.show()


class AddWindow(QWidget):
    def __init__(self, parent=None):
        self.curtext = parent
        super().__init__()
        self.len = 0
        self.initUI()
        self.db()
        self.error = 0
        self.count = 0


    def initUI(self):
        self.setGeometry(650, 500, 650, 400)
        self.setWindowTitle('Виселица')

        self.pixmap = QPixmap("V1.png")
        self.label = QLabel(self)
        self.label.resize(290, 340)
        self.label.move(350, 10)
        self.label.setPixmap(self.pixmap)

        self.label_len = QLabel("Длина слова:", self)
        self.label_len.resize(100, 20)
        self.label_len.move(165, 10)
        self.label_len.setStyleSheet('background: rgb(252,213,131);')

        self.label_0 = QLabel(self)
        self.label_0.resize(170, 50)
        self.label_0.move(165, 60)

        self.label_len_word = QLabel(self)
        self.label_len_word.resize(50, 10)
        self.label_len_word.move(165, 40)

        self.btn = QPushButton("Закончить игру", self)
        self.btn.resize(140, 30)
        self.btn.move(500, 350)
        self.btn.clicked.connect(self.stop)

        ##############
        self.label_20 = QLabel(self)
        self.label_20.resize(10, 30)
        self.label_20.move(10, 340)

        self.label_21 = QLabel(self)
        self.label_21.resize(10, 30)
        self.label_21.move(30, 340)

        self.label_22 = QLabel(self)
        self.label_22.resize(10, 30)
        self.label_22.move(50, 340)

        self.label_23 = QLabel(self)
        self.label_23.resize(10, 30)
        self.label_23.move(70, 340)

        self.label_24 = QLabel(self)
        self.label_24.resize(10, 30)
        self.label_24.move(90, 340)

        self.label_25 = QLabel(self)
        self.label_25.resize(10, 30)
        self.label_25.move(110, 340)

        self.label_26 = QLabel(self)
        self.label_26.resize(10, 30)
        self.label_26.move(130, 340)

        self.label_27 = QLabel(self)
        self.label_27.resize(10, 30)
        self.label_27.move(150, 340)

        self.label_28 = QLabel(self)
        self.label_28.resize(10, 30)
        self.label_28.move(170, 340)

        self.label_29 = QLabel(self)
        self.label_29.resize(10, 30)
        self.label_29.move(190, 340)

        self.label_30 = QLabel(self)
        self.label_30.resize(10, 30)
        self.label_30.move(210, 340)

        self.label_31 = QLabel(self)
        self.label_31.resize(10, 30)
        self.label_31.move(230, 340)

        self.label_3 = QLabel('Ошибок:', self)
        self.label_3.resize(50, 10)
        self.label_3.move(10, 110)
        self.label_3.setStyleSheet('background: rgb(252,213,131);')
        # self.label_3.setFont(QFont('Ошибок:', 8, QFont.Bold))
        # self.label_3.adjustSize()
        ########################################################
        self.label_error = QLabel(self)
        self.label_error.resize(50, 70)
        self.label_error.move(80, 81)

        self.label_6 = QLabel('Описание:', self)
        self.label_6.resize(60, 10)
        self.label_6.move(10, 127)
        self.label_6.setStyleSheet('background: rgb(252,213,131);')

        self.label_11 = QLabel(self)
        self.label_11.resize(200, 70)
        self.label_11.move(10, 150)

        self.label_8 = QLabel('Слово:', self)
        self.label_8.resize(self.label_8.sizeHint())
        self.label_8.move(10, 300)
        self.label_8.setStyleSheet('background: rgb(252,213,131);')

        self.label_9 = QLabel('Выберите букву:', self)
        self.label_9.resize(100, 25)
        self.label_9.move(10, 10)
        self.label_9.setStyleSheet('background: rgb(252,213,131);')

        self.combo1 = QComboBox(self)
        self.combo1.resize(70, 25)
        self.combo1.move(10, 40)
        letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
        for j in letters:
            self.combo1.addItem(j)
        self.combo1.activated[str].connect(self.onChanged1)
        self.show()

    def stop(self):
        self.close()

    def db(self):
        con = sqlite3.connect('1.db')
        cur = con.cursor()
        num = random.randint(1, 5)
        self.ans = []
        sub = None
        answer1 = None
        ####################################################################################plants
        if self.curtext == 'Растения':
            answer1 = set(cur.execute(f""" select titles from plantes where names_id = {num}""").fetchall())
            sub = cur.execute(f"""select sub from plantes where names_id = {num}""").fetchall()
        elif self.curtext == 'Животные':
            answer1 = set(cur.execute(f""" select titles from animales where names_id = {num}""").fetchall())
            sub = cur.execute(f"""select sub from animales where names_id = {num}""").fetchall()
        elif self.curtext == 'Компьютеры и техника':
            answer1 = set(cur.execute(f""" select titles from computeres where names_id = {num}""").fetchall())
            sub = cur.execute(f"""select sub from computeres where names_id = {num}""").fetchall()
        elif self.curtext == 'Кулинария':
            answer1 = set(cur.execute(f""" select titles from cookes where names_id = {num}""").fetchall())
            sub = cur.execute(f"""select sub from cookes where names_id = {num}""").fetchall()
        if sub != None:
            for i in sub:
                for j in i:
                    self.label_11.setText(j)
        if answer1 != None:
            for tup in answer1:
                for word in tup:
                    self.len = len(word)
                    if len(word) == 3:
                        self.label_20.setStyleSheet('background: rgb(252,213,131);')
                        self.label_21.setStyleSheet('background: rgb(252,213,131);')
                        self.label_22.setStyleSheet('background: rgb(252,213,131);')
                    elif len(word) == 4:
                        self.label_20.setStyleSheet('background: rgb(252,213,131);')
                        self.label_21.setStyleSheet('background: rgb(252,213,131);')
                        self.label_22.setStyleSheet('background: rgb(252,213,131);')
                        self.label_23.setStyleSheet('background: rgb(252,213,131);')
                    elif len(word) == 5:
                        self.label_20.setStyleSheet('background: rgb(252,213,131);')
                        self.label_21.setStyleSheet('background: rgb(252,213,131);')
                        self.label_22.setStyleSheet('background: rgb(252,213,131);')
                        self.label_23.setStyleSheet('background: rgb(252,213,131);')
                        self.label_24.setStyleSheet('background: rgb(252,213,131);')
                    elif len(word) == 6:
                        self.label_20.setStyleSheet('background: rgb(252,213,131);')
                        self.label_21.setStyleSheet('background: rgb(252,213,131);')
                        self.label_22.setStyleSheet('background: rgb(252,213,131);')
                        self.label_23.setStyleSheet('background: rgb(252,213,131);')
                        self.label_24.setStyleSheet('background: rgb(252,213,131);')
                        self.label_25.setStyleSheet('background: rgb(252,213,131);')
                    elif len(word) == 7:
                        self.label_20.setStyleSheet('background: rgb(252,213,131);')
                        self.label_21.setStyleSheet('background: rgb(252,213,131);')
                        self.label_22.setStyleSheet('background: rgb(252,213,131);')
                        self.label_23.setStyleSheet('background: rgb(252,213,131);')
                        self.label_24.setStyleSheet('background: rgb(252,213,131);')
                        self.label_25.setStyleSheet('background: rgb(252,213,131);')
                        self.label_26.setStyleSheet('background: rgb(252,213,131);')
                    elif len(word) == 8:
                        self.label_20.setStyleSheet('background: rgb(252,213,131);')
                        self.label_21.setStyleSheet('background: rgb(252,213,131);')
                        self.label_22.setStyleSheet('background: rgb(252,213,131);')
                        self.label_23.setStyleSheet('background: rgb(252,213,131);')
                        self.label_24.setStyleSheet('background: rgb(252,213,131);')
                        self.label_25.setStyleSheet('background: rgb(252,213,131);')
                        self.label_26.setStyleSheet('background: rgb(252,213,131);')
                        self.label_27.setStyleSheet('background: rgb(252,213,131);')
                    elif len(word) == 9:
                        self.label_20.setStyleSheet('background: rgb(252,213,131);')
                        self.label_21.setStyleSheet('background: rgb(252,213,131);')
                        self.label_22.setStyleSheet('background: rgb(252,213,131);')
                        self.label_23.setStyleSheet('background: rgb(252,213,131);')
                        self.label_24.setStyleSheet('background: rgb(252,213,131);')
                        self.label_25.setStyleSheet('background: rgb(252,213,131);')
                        self.label_26.setStyleSheet('background: rgb(252,213,131);')
                        self.label_27.setStyleSheet('background: rgb(252,213,131);')
                        self.label_28.setStyleSheet('background: rgb(252,213,131);')
                    elif len(word) == 10:
                        self.label_20.setStyleSheet('background: rgb(252,213,131);')
                        self.label_21.setStyleSheet('background: rgb(252,213,131);')
                        self.label_22.setStyleSheet('background: rgb(252,213,131);')
                        self.label_23.setStyleSheet('background: rgb(252,213,131);')
                        self.label_24.setStyleSheet('background: rgb(252,213,131);')
                        self.label_25.setStyleSheet('background: rgb(252,213,131);')
                        self.label_26.setStyleSheet('background: rgb(252,213,131);')
                        self.label_27.setStyleSheet('background: rgb(252,213,131);')
                        self.label_28.setStyleSheet('background: rgb(252,213,131);')
                        self.label_29.setStyleSheet('background: rgb(252,213,131);')
                    elif len(word) == 11:
                        self.label_20.setStyleSheet('background: rgb(252,213,131);')
                        self.label_21.setStyleSheet('background: rgb(252,213,131);')
                        self.label_22.setStyleSheet('background: rgb(252,213,131);')
                        self.label_23.setStyleSheet('background: rgb(252,213,131);')
                        self.label_24.setStyleSheet('background: rgb(252,213,131);')
                        self.label_25.setStyleSheet('background: rgb(252,213,131);')
                        self.label_26.setStyleSheet('background: rgb(252,213,131);')
                        self.label_27.setStyleSheet('background: rgb(252,213,131);')
                        self.label_28.setStyleSheet('background: rgb(252,213,131);')
                        self.label_29.setStyleSheet('background: rgb(252,213,131);')
                        self.label_30.setStyleSheet('background: rgb(252,213,131);')
                    elif len(word) == 12:
                        self.label_20.setStyleSheet('background: rgb(252,213,131);')
                        self.label_21.setStyleSheet('background: rgb(252,213,131);')
                        self.label_22.setStyleSheet('background: rgb(252,213,131);')
                        self.label_23.setStyleSheet('background: rgb(252,213,131);')
                        self.label_24.setStyleSheet('background: rgb(252,213,131);')
                        self.label_25.setStyleSheet('background: rgb(252,213,131);')
                        self.label_26.setStyleSheet('background: rgb(252,213,131);')
                        self.label_27.setStyleSheet('background: rgb(252,213,131);')
                        self.label_28.setStyleSheet('background: rgb(252,213,131);')
                        self.label_29.setStyleSheet('background: rgb(252,213,131);')
                        self.label_30.setStyleSheet('background: rgb(252,213,131);')
                        self.label_31.setStyleSheet('background: rgb(252,213,131);')
                    self.label_len_word.setText(str(len(word)))
                    for letter in word:
                        self.ans.append(letter)
        con.commit()
        con.close()

    def onChanged1(self, text):
        print(self.ans, text)
        if self.error < 5:
                if text.upper() in self.ans or text.lower() in self.ans:
                    for i in range(len(self.ans)):
                        if self.ans[i] == text.upper() or self.ans[i] == text.lower():
                            if i == 0:
                                self.label_20.setText(self.ans[i].upper())
                                self.count += 1
                            elif i == 1:
                                self.label_21.setText(self.ans[i])
                                self.count += 1
                            elif i == 2:
                                self.label_22.setText(self.ans[i])
                                self.count += 1
                            elif i == 3:
                                self.label_23.setText(self.ans[i])
                                self.count += 1
                            elif i == 4:
                                self.label_24.setText(self.ans[i])
                                self.count += 1
                            elif i == 5:
                                self.label_25.setText(self.ans[i])
                                self.count += 1
                            elif i == 6:
                                self.label_26.setText(self.ans[i])
                                self.count += 1
                            elif i == 7:
                                self.label_27.setText(self.ans[i])
                                self.count += 1
                            elif i == 8:
                                self.label_28.setText(self.ans[i])
                                self.count += 1
                            elif i == 9:
                                self.label_29.setText(self.ans[i])
                                self.count += 1
                            elif i == 10:
                                self.label_30.setText(self.ans[i])
                                self.count += 1
                            elif i == 11:
                                self.label_31.setText(self.ans[i])
                                self.count += 1
                else:
                    self.error += 1
                    self.label_error.setText(str(self.error))

        if self.count == self.len:
            self.label_0.setText("Вы победили!!")
        if self.error == 1:
            self.pixmap = QPixmap("V2.png")
            self.label.setPixmap(self.pixmap)

        elif self.error == 2:
            self.pixmap = QPixmap("V3.png")
            self.label.setPixmap(self.pixmap)

        elif self.error == 3:
            self.pixmap = QPixmap("V4.png")
            self.label.setPixmap(self.pixmap)

        elif self.error == 4:
            self.pixmap = QPixmap("V5.png")
            self.label.setPixmap(self.pixmap)
            self.label_0.setText("Осталась одна попытка!")

        elif self.error == 5:
            self.pixmap = QPixmap("V6.png")
            self.label.setPixmap(self.pixmap)
            self.label_0.setText("""Вы проиграли!
Больше нельзя выбирать буквы.""")

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
