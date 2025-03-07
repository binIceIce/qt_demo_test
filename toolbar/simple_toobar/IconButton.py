from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton, QWidget


class IconButton(QPushButton):
    def __init__(self, parent: QWidget = None):
        super(IconButton, self).__init__(parent)
        self.setAutoDefault(False)
        self.setFlat(True)

    def paintEvent(self, event: QPaintEvent):
        event.accept() # 在此处理，不要向上传递
        if self.testAttribute(Qt.WA_Disabled):
            # QIcon.Disabled: 图标的禁用模式, 通常图标的颜色会灰色或者淡化方式来显示,表示控键不可用
            # 只需要通过 QIon.Disabled 即可达到置灰的目的
            mode = QIcon.Disabled
        elif self.testAttribute(Qt.WA_UnderMouse):
            mode = QIcon.Selected if self.isDown() else QIcon.Active
        else:
            mode = QIcon.Normal
        qp = QPainter(self)
        self.icon().paint(qp, self.rect(), Qt.AlignCenter, mode)
        qp.end()












