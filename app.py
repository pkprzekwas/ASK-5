# -*- coding: windows-1250 -*
import sys
import time
import thread
from PyQt4 import uic
from PyQt4.QtGui import (QMainWindow, QApplication, QMessageBox,
                         QGraphicsScene, QGraphicsPixmapItem, QPixmap)
import matplotlib.pyplot as plt
from random import choice, randint

import colors
import sounds


class MainWin(QMainWindow):
    BLUE = [colors.BLUE1, colors.BLUE2, colors.BLUE3]
    RED = [colors.RED1, colors.RED2, colors.RED3]
    GREEN = [colors.GREEN1, colors.GREEN2, colors.GREEN3]
    COLORS = [x for color in BLUE, RED, GREEN for x in color]
    SOUNDS = [sounds.beep1, sounds.beep2, sounds.beep3]

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('untitled.ui', self)
        self.choice = None
        self.setWindowTitle("Test psychomotoryczny")

        self.isOptic = False
        self.isSound = False
        self.time = []
        self.agregate = []
        self.counter = 0
        self.last_sound = None

        self.close_btn.clicked.connect(self.close_app)
        self.opt_btn.clicked.connect(self.start_opt)
        self.sound_btn.clicked.connect(self.start_sound)
        self.blue_btn.clicked.connect(self.blue)
        self.red_btn.clicked.connect(self.red)
        self.green_btn.clicked.connect(self.green)

        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.hide()

    def hide(self):
        self.graphicsView.hide()
        self.blue_btn.hide()
        self.red_btn.hide()
        self.green_btn.hide()
        self.blue_btn.setText(u"   ")
        self.red_btn.setText(u"   ")
        self.green_btn.setText(u"   ")
        self.blue_btn.setStyleSheet("background-color: transparent")
        self.red_btn.setStyleSheet("background-color: transparent")
        self.green_btn.setStyleSheet("background-color: transparent")

    def reset_meas(self):
        self.time = []
        self.agregate = []
        self.counter = 0
        self.time = []
        self.isOptic = False
        self.isSound = False

    def close_app(self):
        self.close()

    def start_sound(self):
        if not self.isOptic:
            self.isSound = True
            QMessageBox.about(self, "Instrukcja", u"Twoim zadaniem jesy w jak najkrótszym czasie nacisnąć na przycisk "
                                                  u"odpowiadający dzwiękowi który słyszysz. "
                                                  u"Pierwsze 10 prób jest na nauke dzwięków i nie są brane pod uwagę.")
            self.blue_btn.setText(u"Dzwięk 1")
            self.red_btn.setText(u"Dzwięk 2")
            self.green_btn.setText(u"Dzwięk 3")
            self.blue_btn.show()
            self.red_btn.show()
            self.green_btn.show()
            self.st_time = time.time()
            self.init_time = time.time()
            self.last_sound = choice(self.SOUNDS)
            thread.start_new_thread(self.last_sound, ())
            pass

    def start_opt(self):
        if not self.isSound:
            self.isOptic = True
            self.blue_btn.setStyleSheet("background-color: blue")
            self.red_btn.setStyleSheet("background-color: red")
            self.green_btn.setStyleSheet("background-color: green")
            QMessageBox.about(self, "Instrukcja", u"Twoim zadaniem jesy w jak najkrótszym czasie nacisnąć na przycisk "
                                                  u"odpowiadający kolorowi którego nazwa jest wyświetlona na ekranie. "
                                                  u"Pierwsze dziesięć odczytów jest testowych i nie będą brane pod uwagę.")
            self.scene.clear()
            self.choice = choice(self.COLORS)
            item = QGraphicsPixmapItem(QPixmap(self.choice))
            self.scene.addItem(item)
            self.graphicsView.show()
            self.blue_btn.show()
            self.red_btn.show()
            self.green_btn.show()
            self.st_time = time.time()
            self.init_time = time.time()
        pass

    def blue(self):
        if self.isOptic:
            if self.counter > 20:
                self.plot_results()
                self.hide()
            if self.choice in self.BLUE:
                self.scene.clear()
                self.choice = choice(self.COLORS)
                item = QGraphicsPixmapItem(QPixmap(self.choice))
                self.scene.addItem(item)
                self.time.append(time.time()-self.st_time)
                self.agregate.append(time.time()-self.init_time)
                self.st_time = time.time()
                self.counter += 1
        if self.isSound:
            if self.counter > 20:
                self.plot_results()
                self.hide()
            if self.last_sound == sounds.beep1:
                self.last_sound = choice(self.SOUNDS)
                thread.start_new_thread(self.last_sound, ())
                self.time.append(time.time()-self.st_time)
                self.agregate.append(time.time()-self.init_time)
                self.st_time = time.time()
                self.counter += 1
                print(self.counter)
        pass

    def red(self):
        if self.isOptic:
            if self.counter > 20:
                self.plot_results()
                self.hide()
            if self.choice in self.RED:
                self.scene.clear()
                self.choice = choice(self.COLORS)
                item = QGraphicsPixmapItem(QPixmap(self.choice))
                self.scene.addItem(item)
                self.time.append(time.time()-self.st_time)
                self.agregate.append(time.time()-self.init_time)
                self.st_time = time.time()
                self.counter += 1
        if self.isSound:
            if self.counter > 20:
                self.plot_results()
                self.hide()
            if self.last_sound == sounds.beep3:
                self.last_sound = choice(self.SOUNDS)
                thread.start_new_thread(self.last_sound, ())
                self.time.append(time.time()-self.st_time)
                self.agregate.append(time.time()-self.init_time)
                self.st_time = time.time()
                self.counter += 1

        pass

    def green(self):
        if self.isOptic:
            if self.counter > 20:
                self.plot_results()
                self.hide()
            if self.choice in self.GREEN:
                self.green_btn.setStyleSheet("background-color: green")
                self.scene.clear()
                self.choice = choice(self.COLORS)
                item = QGraphicsPixmapItem(QPixmap(self.choice))
                self.scene.addItem(item)
                self.time.append(time.time()-self.st_time)
                self.agregate.append(time.time()-self.init_time)
                self.st_time = time.time()
                self.counter += 1
        if self.isSound:
            if self.counter > 20:
                self.plot_results()
                self.hide()
            if self.last_sound == sounds.beep2:
                self.last_sound = choice(self.SOUNDS)
                thread.start_new_thread(self.last_sound, ())
                self.time.append(time.time()-self.st_time)
                self.agregate.append(time.time()-self.init_time)
                self.st_time = time.time()
                self.counter += 1
        pass

    def plot_results(self):
        plt.figure(1)
        plt.title('Wynik badania')
        plt.subplot(211)
        plt.plot(range(1,11), self.time[11:], 'ro')
        plt.ylabel('Reakcja [s]')
        plt.xlabel(u'Próbka')
        plt.subplot(212)
        plt.plot(range(1,11), self.agregate[11:])
        plt.ylabel('Reakcje [s]')
        plt.xlabel(u'Próbka')
        plt.show()
        i = 1
        with open("test.txt", "a") as f:
            f.write(u"-------------------TEST {} --------------------\n"
                    .format(time.strftime("%Y-%m-%d %H:%M")))
            if self.isOptic:
                f.write(u"Forma badania: wzork\n")
            else:
                f.write(u"Forma badania: dzwiek\n")
            for each in self.time[11:]:
                if each > 3:
                    f.write(u"******************\n")
                f.write(u"->>: {} Czas: {}\n".format(i, each))
                i += 1
        self.reset_meas()


if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    mw = MainWin()
    mw.show()
    sys.exit(qApp.exec_())