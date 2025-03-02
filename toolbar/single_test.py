""" 
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QToolBar, QPushButton, QDialog
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个 QVBoxLayout
        layout = QVBoxLayout(self)

        # 创建 QWebEngineView
        self.webView = QWebEngineView(self)
        self.webView.setUrl(QUrl("https://www.baidu.com/"))  # 加载默认页面
        layout.addWidget(self.webView)

        # 创建工具栏
        self.toolbar = QToolBar("Toolbar", self)
        self.toolbar.setFloatable(False)
        self.toolbar.setMovable(False)

        # 添加按钮到工具栏
        self.openButton = QPushButton("Open New Window", self)
        self.openButton.clicked.connect(self.openNewWindow)
        self.toolbar.addWidget(self.openButton)

        # 将工具栏添加到布局中
        layout.addWidget(self.toolbar)

        # 设置窗口属性
        self.setWindowTitle("PyQt5 WebEngineView with Toolbar")
        self.resize(800, 600)

    def openNewWindow(self):
        #打开一个新的窗口加载另一个 HTML 页面
        new_window = QDialog(self)
        new_window.setWindowTitle("New Window")
        new_window.resize(600, 400)

        # 创建新的 QWebEngineView
        new_web_view = QWebEngineView(new_window)
        new_web_view.setUrl(QUrl("https://www.baidu.com/"))  # 加载新的页面

        # 创建布局并添加 QWebEngineView
        new_layout = QVBoxLayout(new_window)
        new_layout.addWidget(new_web_view)

        # 显示新窗口
        new_window.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    from PyQt5.QtWebEngineWidgets import QWebEngineProfile
    QWebEngineProfile.defaultProfile()

    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())
"""

""" 
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDialog
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建主布局
        main_layout = QVBoxLayout(self)

        # 创建自定义工具栏（使用 QWidget 和 QHBoxLayout）
        self.toolbar = QWidget(self)
        toolbar_layout = QHBoxLayout(self.toolbar)

        # 添加按钮到工具栏
        self.openButton = QPushButton("Open New Window", self)
        self.openButton.clicked.connect(self.openNewWindow)
        toolbar_layout.addWidget(self.openButton)

        # 设置工具栏布局
        self.toolbar.setLayout(toolbar_layout)
        self.toolbar.setFixedHeight(30)  # 固定高度为 60 像素
        main_layout.addWidget(self.toolbar)

        # 创建 QWebEngineView
        self.webView = QWebEngineView(self)
        self.webView.setUrl(QUrl("https://www.baidu.com/"))  # 加载默认页面
        main_layout.addWidget(self.webView)

        # 设置窗口属性
        self.setWindowTitle("PyQt5 WebEngineView with Custom Toolbar")
        self.resize(800, 600)

    def openNewWindow(self):
        #打开一个新的窗口加载另一个 HTML 页面
        new_window = QDialog(self)
        new_window.setWindowTitle("New Window")
        new_window.resize(600, 400)

        # 创建新的 QWebEngineView
        new_web_view = QWebEngineView(new_window)
        new_web_view.setUrl(QUrl("https://www.baidu.com/"))  # 加载新的页面

        # 创建布局并添加 QWebEngineView
        new_layout = QVBoxLayout(new_window)
        new_layout.addWidget(new_web_view)

        # 显示新窗口
        new_window.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    from PyQt5.QtWebEngineWidgets import QWebEngineProfile
    QWebEngineProfile.defaultProfile()

    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建主布局
        main_layout = QVBoxLayout(self)

        # 创建自定义工具栏（使用 QWidget 和 QHBoxLayout）
        self.toolbar = QWidget(self)
        toolbar_layout = QHBoxLayout(self.toolbar)

        # 添加按钮到工具栏
        self.openButton = QPushButton("Open New Window", self)
        self.openButton.clicked.connect(self.openNewWindow)
        toolbar_layout.addWidget(self.openButton)

        # 设置工具栏的布局
        self.toolbar.setLayout(toolbar_layout)
        main_layout.addWidget(self.toolbar)

        # 创建 QWebEngineView
        self.webView = QWebEngineView(self)
        self.webView.setUrl(QUrl("https://www.baidu.com/"))  # 加载默认页面
        main_layout.addWidget(self.webView)

        # 设置窗口属性
        self.setWindowTitle("PyQt5 WebEngineView with Custom Toolbar")
        self.resize(800, 600)

    def openNewWindow(self):
        """打开一个新的窗口加载另一个 HTML 页面"""
        # 创建一个新的 QFrame 作为弹出窗口
        new_window = QFrame(self)
        new_window.setWindowTitle("New Window")
        new_window.resize(600, 400)

        # 设置窗口标志，使其表现得像一个独立窗口
        new_window.setWindowFlags(Qt.Window)

        # 创建新的 QWebEngineView
        new_web_view = QWebEngineView(new_window)
        new_web_view.setUrl(QUrl("https://www.baidu.com/"))  # 加载新的页面

        # 创建布局并添加 QWebEngineView
        new_layout = QVBoxLayout(new_window)
        new_layout.addWidget(new_web_view)

        # 设置新窗口的布局
        new_window.setLayout(new_layout)

        # 显示新窗口
        new_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    from PyQt5.QtWebEngineWidgets import QWebEngineProfile
    QWebEngineProfile.defaultProfile()

    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())