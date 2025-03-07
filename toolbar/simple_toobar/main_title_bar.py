from PyQt5.QtCore import Qt, pyqtSignal, QSignalBlocker, QPoint, QObject, QEvent, QSize
from PyQt5.QtGui import QMovie, QIcon, QPixmap, QPainter, QBrush, QColor, QFont, QFontMetrics
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

#from .ui_form_test import Ui_Form

from ui_form_test import Ui_Form
from user_profile_button import UserProfileButton


def create_default_profile_icon():
    letter = 'ice'
    color = (QColor(0xff, 0xe1, 0x7b),
             QColor(0xff, 0x73, 0x98),
             QColor(0xff, 0x82, 0x78),
             QColor(0x72, 0xdc, 0xa2),
             QColor(0x8a, 0xa6, 0xf9))[1124 % 5]
    size = 100
    pixmap = QPixmap(size, size)
    pixmap.fill(color)
    qp = QPainter()
    qp.begin(pixmap)
    qp.setRenderHint(QPainter.Antialiasing)
    qp.setRenderHint(QPainter.TextAntialiasing)
    qp.setPen(QColor(255, 255, 255))

    font = QFont('"Microsoft YaHei", '
                 '"PingFang SC", '
                 '"WenQuanYi Micro Hei",')
    font.setPointSize(int(size * 0.3))
    font_metrics = QFontMetrics(font)

    v1 = (size - font_metrics.width(letter)) / 2
    v2 = (size - (font_metrics.ascent() + font_metrics.descent())) / 2 + font_metrics.ascent()

    print('v1 = %s, v2 = %s' % (v1, v2))
    point = QPoint(int(v1), int(v2))
    qp.setFont(font)
    qp.drawText(point, letter)
    qp.end()
    return pixmap


def create_round_pixmap(image_path, size):
    """Load an image and crop it into a circle."""
    pixmap = QPixmap(image_path)
    pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)  # Resize

    # Create a mask for the round shape
    mask = QPixmap(size, size)
    mask.fill(Qt.transparent)

    painter = QPainter(mask)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setBrush(QBrush(Qt.black))
    painter.drawEllipse(0, 0, size, size)  # Draw a circular mask
    painter.end()

    # Apply the mask to the pixmap
    pixmap.setMask(mask.mask())

    return pixmap


class MainTitleBar(QWidget):
    need_show_user_profile_widget = pyqtSignal(name='need_show_user_profile_widget')

    def __init__(self, parent: QWidget = None):
        super(MainTitleBar, self).__init__(parent=parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #profile_image_path = 'D://github//qt_demo_test//toolbar//Cropped_Image.png'
        self.ui.user_profile_button = UserProfileButton()
        self.ui.user_profile_button.setObjectName('user_profile_button')
        self.ui.user_profile_button.setFixedSize(60, 60)  # Set button size

        #self.ui.user_profile_button.setFixedSize(60, 60)  # 这个设置为 40,40 就变为方形
        self.ui.user_profile_button.set_user_profile_pixmap(create_default_profile_icon())

        self.ui.horizontalLayout_2.addWidget(self.ui.user_profile_button)
        self.ui.user_profile_button.clicked.connect(self.need_show_user_profile_widget)

    #def __get_bottom_right__(self, widget: QWidget):
    #    return self.mapToGlobal(widget.geometry().bottomRight())

    #def get_user_profile_widget_pos(self):
    #    return self.__get_bottom_right__(self.ui.user_profile_button)

    #def set_user_profile_loading_visible(self, visible: bool):
    #    self.ui.user_profile_button.set_loading_visible(visible)





