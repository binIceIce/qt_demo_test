from PyQt5.QtCore import Qt, pyqtSignal, QSignalBlocker, QPoint, QObject, QEvent
from PyQt5.QtGui import QMovie, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

#from .ui_form_test import Ui_Form

from ui_form_test import Ui_Form


class MainTitleBar(QWidget):
    need_show_user_profile_widget = pyqtSignal(name='need_show_user_profile_widget')

    def __init__(self, parent: QWidget = None):
        super(MainTitleBar, self).__init__(parent=parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        profile_image_path = 'D://github//qt_demo_test//toolbar//Cropped_Image.png'
        self.ui.user_profile_button = QPushButton()
        self.ui.user_profile_button.setObjectName('user_profile_button')
        self.ui.user_profile_button.setFixedSize(40, 40)  # Set button size
        self.ui.user_profile_button.setStyleSheet(f"""
                            QPushButton {{
                                border-radius: 20px;
                                border: 2px solid #CCC;
                                background-image: url({profile_image_path});
                                background-position: center;
                                background-repeat: no-repeat;
                                background-size: cover;
                            }}
                            QPushButton:hover {{
                                border: 2px solid #3498db;
                            }}
                        """)

        self.ui.horizontalLayout_2.addWidget(self.ui.user_profile_button)
        self.ui.user_profile_button.clicked.connect(self.need_show_user_profile_widget)

    #def __get_bottom_right__(self, widget: QWidget):
    #    return self.mapToGlobal(widget.geometry().bottomRight())

    #def get_user_profile_widget_pos(self):
    #    return self.__get_bottom_right__(self.ui.user_profile_button)

    def set_user_profile_loading_visible(self, visible: bool):
        #self.ui.user_profile_button.set_loading_visible(visible)
        pass




