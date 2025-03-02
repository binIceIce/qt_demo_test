from PyQt5.QtCore import QUrl, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView


class UserProfileWidget(QFrame):
    def __init__(self, parent: QWidget = None):
        super(UserProfileWidget, self).__init__(parent=parent)

        self.setWindowTitle('new Window')
        self.resize(600, 400)

        self.setLayout(QVBoxLayout(self))
        #self.layout().setContentsMargins(0, 0, 0, 0)
        #self.layout().setSizeConstraint(QVBoxLayout.SetFixedSize)

        self.webview = QWebEngineView(self)
        self.layout().addWidget(self.webview)

        self.webview.setGeometry(10, 10, 80, 60)


        """ 
        self.setWindowTitle('new Window')
        self.resize(600, 400)

        self.webview = QWebEngineView(self)

        new_layout = QVBoxLayout(self)
        new_layout.addWidget(self.webview)

        self.setLayout(new_layout)
        """

    def reload_page(self):
        print('[UserProfileWidget] begin')
        url = QUrl('https://www.baidu.com/')
        self.webview.load(url)
        print('[UserProfileWidget] end')

        self.show()



