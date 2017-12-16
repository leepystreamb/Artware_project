"""
The loading page has a track that takes 18 second,
you can skip it at line62 if you do not want to wait.

"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QColor, QBrush, QPainter, QIcon, QPixmap, QCursor, QFont
from PyQt5.QtMultimedia import QSound

loading_logo = 'chrome_logo.png'

class MyWin(QWidget):


    def __init__(self):
        super(MyWin, self).__init__()

        #load & set cursor look
        CursorN = QPixmap("cursor_norm.png")
        CursorC = QPixmap("cursor_click.png")
        cursor00 = QCursor(CursorN)
        cursor01 = QCursor(CursorC)

        white = QColor(0, 0, 0)



        #set timer for 'laoding' the page
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.setCursor(cursor01)

        self.initGUI()


    def initGUI(self):
        self.setWindowTitle("Chrome: True Path to Eternal Blue Sky")
        #set the background to be transparent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        drum = QLabel(self)
        chrome = QLabel(self)
        chrome.setFont(QFont("Monaco", 30, QFont.Bold))
        chrome.setText('Loading...')

        loaddrum = QPixmap(loading_logo)
        drum.setPixmap(loaddrum)
        width = loaddrum.width()
        height = loaddrum.height()

        drum.setGeometry(0,0,loaddrum.width(), loaddrum.height())
        chrome.setGeometry(width/2-100, height/2-50, 200, 100)
        self.resize(loaddrum.width(), loaddrum.height())
        self.show()

        self.bgm_start = QSound('bgm_start.wav')
        self.bgm_start.play()
        self.timer.start(18000) # you can change the loading time here
        self.timer.timeout.connect(self.hide)
        self.timer.timeout.connect(self.browse)




    def browse(self):

        bg = QPixmap('layout.png')
        google = QPixmap('google.png')

        # you can make the following 3 codes as comment if you find it too annoying
        self.bgm_loop = QSound('bgm_loop.wav')
        self.bgm_loop.setLoops(-1)
        self.bgm_loop.play()

        self.layout = QLabel(self)

        self.layout.setPixmap(bg)
        self.layout.setGeometry(0, 0, bg.width(), bg.height())
        self.resize(self.layout.width(), self.layout.height())


        self.logo = QLabel(self)
        self.logo.setPixmap(google)
        self.logo.setGeometry(0, 0, google.width(), google.height())

        self.searchbar = QLineEdit(self)
        self.searchbar.setText("What do you desire to learn?")
        self.searchbar.setGeometry(50, self.layout.height()/2, 500, 30)

        drumim = QPixmap('go.png')
        self.icon  = QIcon('go.png')

        self.sdrum = QPushButton("Go!", self)
        self.sdrum.setCheckable(True)
        self.sdrum.setIcon(self.icon)
        self.sdrum.setGeometry(280, 450, 80, 30)

        self.show()
        self.sdrum.clicked.connect(self.hide)
        self.sdrum.clicked.connect(self.search)


    def search(self):
        result = QPixmap('result.png')
        self.searchResult = QLabel(self)
        self.searchResult.setPixmap(result)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWin()
    sys.exit(app.exec_())
