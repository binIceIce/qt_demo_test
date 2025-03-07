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
        size = 60
        pixmap = QPixmap('D:\\github\\qt_demo_test\\toolbar\\Cropped_Image.png')
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

        self.setIcon(QIcon(pixmap))
        self.setIconSize(QSize(60, 60))



        """
        mask_pixmap = QPixmap(r'D://github//qt_demo_test//toolbar//Cropped_Image.png').scaled(pixmap.size(),
                                                                                              Qt.KeepAspectRatio,
                                                                                              Qt.SmoothTransformation)
        qp.begin(mask_pixmap)
        qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
        qp.setOpacity(0.3)
        qp.fillRect(mask_pixmap.rect(), Qt.black)
        qp.end()
        self.__mask_icon__ = QIcon(mask_pixmap)
        """

    def paintEvent(self, event: QPaintEvent):
        super(UserProfileButton, self).paintEvent(event)
        if self.loading_visible:
            qp = QPainter(self)
            self.__mask_icon__.paint(qp, self.rect(), Qt.AlignCenter)
            qp.end()
