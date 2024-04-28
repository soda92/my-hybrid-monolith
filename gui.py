from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import *

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setBaseSize(800, 600)
        self.browser.setUrl(QUrl("http://127.0.0.1:8000/"))
        self.setCentralWidget(self.browser)
        self.show()


def gui_main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()


if __name__ == "__main__":
    gui_main()
