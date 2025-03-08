from PyQt5.QtWidgets import QWidget, QSizePolicy, QApplication
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

from main_title_bar import MainTitleBar
from user_profile_widget import UserProfileWidget, QVBoxLayout
from frame_widget import FrameWidget
from basic_title_bar import BasicTitleBar


class MainWidget(FrameWidget):
    def __init__(self):
        self.ext_title_bar = MainTitleBar()
        super(MainWidget, self).__init__(title_bar=BasicTitleBar(ext_title_bar=self.ext_title_bar),
                                         center_widget=QWidget())

        self.__user_profile_widget__ = UserProfileWidget(parent=self)
        self.__user_profile_widget__.setWindowFlags(self.__user_profile_widget__.windowFlags() | Qt.Popup)

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


def main():
    app = QApplication(sys.argv)

    with open(r"D:\github\qt_demo_test\stylesheet.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = MainWidget()  # Directly instantiate MainWidget as the main window
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()










