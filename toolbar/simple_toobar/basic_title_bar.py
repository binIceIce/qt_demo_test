from PyQt5.QtCore import pyqtSignal, QEvent, Qt
from PyQt5.QtGui import QIcon, QResizeEvent, QPainter, QPaintEvent, QMouseEvent

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSizePolicy, QStyleOption, QStyle, QLabel


class BasicTitleBar(QWidget):
    need_close = pyqtSignal(name='need_close')
    need_maximize = pyqtSignal(name='need_maximize_or_recover')
    need_recover = pyqtSignal(name='need_recover')
    need_minimize = pyqtSignal(name='need_minimize')
    need_show_full_screen = pyqtSignal(name='need_show_full_screen')

    def __init__(self, ext_title_bar: QWidget = None, parent: QWidget = None):
        super(BasicTitleBar, self).__init__(parent)

        # 若放置到全局的位置(ps 比如说类外面)，会报告: Must construct a QGuiApplication before a QPixmap 错误
        win_minimize_icon = QIcon('D://github//qt_demo_test//toolbar//minimize.png')
        win_maximize_icon = QIcon('D://github//qt_demo_test//toolbar//maximize.png')
        win_restore_icon = QIcon('D://github//qt_demo_test//toolbar//restore.png')
        win_close_icon = QIcon('D://github//qt_demo_test//toolbar//close.png')

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.ext_title_bar = ext_title_bar
        if self.ext_title_bar:
            self.ext_title_bar.setObjectName('ext_title_bar')
            self.layout().addWidget(self.ext_title_bar)

        self.minimize_button = QPushButton(self)
        self.maximize_button = QPushButton(self)
        self.close_button = QPushButton(self)

        self.minimize_button.setObjectName('win_minimize_button')
        self.maximize_button.setObjectName('win_maximize_button')
        self.close_button.setObjectName('win_close_button')

        self.minimize_button.setIcon(win_minimize_icon)
        self.maximize_button.setIcon(win_maximize_icon)
        self.close_button.setIcon(win_close_icon)

        for button in (self.minimize_button, self.maximize_button, self.close_button):
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.setAutoDefault(False)

        self.minimize_button.clicked.connect(self.need_minimize)

        def on_close_button_click():
            self.need_close.emit()

        def on_maximize_button_click():
            if self.parent().isMaximized():
                self.need_recover.emit()
            else:
                self.need_maximize.emit()

        def on_minimize_button_click():
            self.need_minimize.emit()

        self.close_button.clicked.connect(on_close_button_click)
        self.maximize_button.clicked.connect(on_maximize_button_click)
        self.minimize_button.clicked.connect(on_minimize_button_click)

    def update_maximize_button_icon(self, is_maximize: bool):
        # for windows
        self.maximize_button.setIcon(QIcon('D://github//qt_demo_test//toolbar//restore.png') if
                                     is_maximize else QIcon('D://github//qt_demo_test//toolbar//maximize.png'))

    def update_button(self):
        pass

    def paintEvent(self, event: QPaintEvent):
        super(BasicTitleBar, self).paintEvent(event)
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        s = self.style()
        s.drawPrimitive(QStyle.PE_Widget, opt, p, self)

    # for windows set
    def resizeEvent(self, event: QResizeEvent):
        # 可以调整按钮的位置
        self.minimize_button.move(self.width() - self.minimize_button.width() - 65,
                                      (self.height() - self.minimize_button.height()) / 2)
        self.maximize_button.move(self.width() - self.maximize_button.width() - 40,
                                      (self.height() - self.minimize_button.height()) / 2)
        self.close_button.move(self.width() - self.close_button.width() - 15,
                                   (self.height() - self.minimize_button.height()) / 2)
        return super(BasicTitleBar, self).resizeEvent(event)

















