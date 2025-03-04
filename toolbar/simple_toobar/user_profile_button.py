from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPaintEvent, QPainter, QPixmap
from PyQt5.QtWidgets import QWidget

from IconButton import IconButton


class UserProfileButton(IconButton):
    def __init__(self, parent: QWidget = None):
        super(UserProfileButton, self).__init__(parent)

        self.__mask_icon__ = QIcon()
        self.loading_visible = False

    def set_loading_visible(self, visible: bool):
        self.loading_visible = visible
        self.update()

    # QPixmap: 主要用于加载，显示和操作图片文件
    #
    def set_user_profile_pixmap(self, pixmap: QPixmap):
        # QPainter 的主要作用是提供一个绘图接口，用于在各种绘图设备（如窗口、图像、打印机等）上进行绘制。
        qp = QPainter()
        # Qt.KeepAspectRatio: 用于指定在调整图像大小时保持图像的宽高比
        # Qt.SmoothTransformation: 用于指定在调整图像大小时使用平滑变换算法
        icon_pixmap = QPixmap('D://github//qt_demo_test//toolbar//Cropped_Image.png').scaled(pixmap.size(),
                                                                                             Qt.KeepAspectRatio,
                                                                                             Qt.SmoothTransformation)
        qp.begin(icon_pixmap)
        qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
        qp.drawPixmap(0, 0, pixmap)
        qp.end()
        self.setIcon(QIcon(icon_pixmap))

        mask_pixmap = QPixmap(r'D://github//qt_demo_test//toolbar//Cropped_Image.png').scaled(pixmap.size(),
                                                                                   Qt.KeepAspectRatio,
                                                                                   Qt.SmoothTransformation)
        qp.begin(mask_pixmap)
        qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
        qp.setOpacity(0.3)
        qp.fillRect(mask_pixmap.rect(), Qt.black)
        qp.end()
        self.__mask_icon__ = QIcon(mask_pixmap)

    # 自定义绘制
    def paintEvent(self, event: QPaintEvent):
        super(UserProfileButton, self).paintEvent(event)
        if self.loading_visible:
            qp = QPainter(self)
            self.__mask_icon__.paint(qp, self.rect(), Qt.AlignCenter)
            qp.end()
