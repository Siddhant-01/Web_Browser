# pip install PyQtWebEngine
# pip install PyQt5

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_bn = QAction('<-', self)
        back_bn.triggered.connect(self.browser.back)
        navbar.addAction(back_bn)

        forward_bn = QAction('->', self)
        forward_bn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_bn)

        reload_bn = QAction('Reload', self)
        reload_bn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_bn)

        home_bn = QAction('Home', self)
        home_bn.triggered.connect(self.navigate_home)
        navbar.addAction(home_bn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('My Cookie Free Browser')
window = Window()
app.exec_()