from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton, QWidget


class IconButton(QPushButton):
    def __init__(self, parent: QWidget = None):
        super(IconButton, self).__init__(parent)
        self.setAutoDefault(False)
        self.setFlat(True)

    def paintEvent(self, event: QPaintEvent):
        event.accept()
        if self.testAttribute(Qt.WA_Disabled):
            mode = QIcon.Disabled
        elif self.testAttribute(Qt.WA_UnderMouse):
            mode = QIcon.Selected if self.isDown() else QIcon.Active
        else:
            mode = QIcon.Normal
        qp = QPainter(self)
        self.icon().paint(qp, self.rect(), Qt.AlignCenter, mode)
        qp.end()












