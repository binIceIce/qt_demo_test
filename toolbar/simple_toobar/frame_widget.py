from PyQt5.QtCore import QByteArray, QEvent, pyqtSignal, Qt, QPoint, QRect
from PyQt5.QtGui import QPaintEvent, QPainter, QMouseEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, qApp, QStyleOption, QStyle

from basic_title_bar import BasicTitleBar


import ctypes.wintypes
import win32con

border_width = 0
native_message_type = QByteArray(b'windows_generic_MSG')


class FrameWidget(QWidget):
    title_bar_clicked = pyqtSignal(name='title_bar_clicked')

    def __init__(self, title_bar: BasicTitleBar, center_widget: QWidget, parent: QWidget = None):
        super(FrameWidget, self).__init__(parent=parent)

        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(border_width, border_width, border_width, border_width)
        self.setLayout(layout)

        self.title_bar = title_bar
        title_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        title_bar.setObjectName('title_bar')
        self.layout().addWidget(title_bar)

        center_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.layout().addWidget(center_widget)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        title_bar.need_close.connect(self.close)
        title_bar.need_minimize.connect(self.showMinimized)
        title_bar.need_maximize.connect(self.showMaximized)
        title_bar.need_recover.connect(self.showNormal)
        title_bar.need_show_full_screen.connect(self.showFullScreen)

        # 增加设置窗口属性，双击titlebar时能够正确的最大化，而不是全屏
        # 在64位的python上（不是64位的系统上）运行时才需要使用GetWindowLongPtr / SetWindowLongPtr
        """ 
        # 若此处设置后，即使设置 FramelessWindowHint ，顶部的标题栏也不会消失
        hwnd = ctypes.wintypes.HWND.from_param(int(self.winId()))
        style = ctypes.windll.user32.GetWindowLongW(hwnd, win32con.GWL_STYLE)
        style |= win32con.WS_CAPTION
        style |= win32con.WS_POPUP
        style |= win32con.WS_SYSMENU
        style |= win32con.WS_MINIMIZEBOX
        style |= win32con.WS_MAXIMIZEBOX
        style |= win32con.WS_THICKFRAME
        style |= win32con.WS_CLIPCHILDREN
        ctypes.windll.user32.SetWindowLongW(hwnd, win32con.GWL_STYLE, style)

        flags = win32con.SWP_FRAMECHANGED | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
        ctypes.windll.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0, flags)
        """

        if self.title_bar.ext_title_bar.objectName() == 'title_text_label':
            self.windowTitleChanged.connect(self.title_bar.ext_title_bar.setText)

    def paintEvent(self, event: QPaintEvent):
        super(FrameWidget, self).paintEvent(event)
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        s = self.style()
        s.drawPrimitive(QStyle.PE_Widget, opt, p, self)


    def __get_device_pixel_ratio__(self):
        return self.devicePixelRatioF()

    def changeEvent(self, event: QEvent):
        if event.type() == QEvent.WindowStateChange:
            self.title_bar.update_maximize_button_icon(self.isMaximized())
        return super(FrameWidget, self).changeEvent(event)

    # ps: 暂时不确定这个具体的用处是什么
    # noinspection PyMethodOverriding
    #def nativeEvent(self, message_type: QByteArray, raw_message):
    #    pass
