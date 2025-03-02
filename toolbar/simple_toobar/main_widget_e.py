from PyQt5.QtWidgets import QWidget, QSizePolicy, QApplication
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

from main_title_bar import MainTitleBar
from user_profile_widget import UserProfileWidget, QVBoxLayout


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()

        self.ext_title_bar = MainTitleBar()

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.ext_title_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.ext_title_bar.setObjectName('title_bar')
        self.layout().addWidget(self.ext_title_bar)
        #self.ext_title_bar.update_button()

        self.__user_profile_widget__ = UserProfileWidget(parent=self)
        #self.__user_profile_widget__.setWindowFlags(self.__user_profile_widget__.windowFlags() | Qt.Popup)
        self.__user_profile_widget__.setWindowFlags(Qt.Window)

        self.browser = QWebEngineView(self)
        self.browser.setGeometry(10, 10, 800, 600)
        self.layout().addWidget(self.browser) # 注意一下，这个也要添加进来， 否则bar 界面和 html 界面先显示会有异常。
        url = QUrl("https://www.baidu.com/")
        self.browser.load(url)

        def load_user_profile_page():
            print('clicked ')
            self.__user_profile_widget__.reload_page()
            #self.ext_title_bar.set_user_profile_loading_visible(True)

        self.ext_title_bar.need_show_user_profile_widget.connect(load_user_profile_page)

app = QApplication(sys.argv)
window = MainWidget()  # Directly instantiate MainWidget as the main window
window.show()
sys.exit(app.exec_())










