from PyQt5.QtCore import Qt, QRectF, QSize
from PyQt5.QtGui import QIcon, QPaintEvent, QPainter, QPixmap, QPainter, QPainterPath, QBrush
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
        qp = QPainter()
        # 此处的分隔符使用 '//' or '\\' 都可以
        icon_pixmap = QPixmap('D://github//qt_demo_test//toolbar//user_profile_mask.png').scaled(pixmap.size(),
                                                                                Qt.KeepAspectRatio,
                                                                                Qt.SmoothTransformation)
        qp.begin(icon_pixmap)
        qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
        qp.drawPixmap(0, 0, pixmap)
        qp.end()
        self.setIcon(QIcon(icon_pixmap))

        mask_pixmap = QPixmap('D://github//qt_demo_test//toolbar//user_profile_mask.png').scaled(pixmap.size(),
                                                                                                 Qt.KeepAspectRatio,
                                                                                                 Qt.SmoothTransformation)
        qp.begin(mask_pixmap)
        qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
        qp.setOpacity(0.3)
        qp.fillRect(mask_pixmap.rect(), Qt.black)
        qp.end()
        self.__mask_icon__ = QIcon(mask_pixmap)

    def paintEvent(self, event: QPaintEvent):
        super(UserProfileButton, self).paintEvent(event)
        if self.loading_visible:  # 如果 loading_visiable 为 True, 头像会变暗
            qp = QPainter(self)
            self.__mask_icon__.paint(qp, self.rect(), Qt.AlignCenter)
            qp.end()
