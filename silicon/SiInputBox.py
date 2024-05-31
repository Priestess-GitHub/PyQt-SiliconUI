from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from .SiFont import *


class SiInputBoxLineEdit(QLineEdit):
    focus_changed = QtCore.pyqtSignal(bool)

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.focus_changed.emit(True)

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.focus_changed.emit(False)

class SiInputBox(QLabel):

    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('')
        self.parent = parent

        self.highlight_bg = QLabel(self)
        self.bg = QLabel(self)

        self.line_edit = SiInputBoxLineEdit(self)
        self.line_edit.setFont(font_L1)
        self.line_edit.setStyleSheet('''
            QLineEdit {
                background-color: transparent;
                color: #ffffff;
                border: 0px
            }
            QLineEdit::selection {
                background-color: #493F4E;
            }
            ''')
        self.line_edit.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.line_edit.setFocusPolicy(Qt.ClickFocus)
        self.line_edit.focus_changed.connect(self.focus_handler)
        self.line_edit.returnPressed.connect(self.line_edit.clearFocus)

        self.highlight_bg.setStyleSheet('background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #52389a, stop:1 #9c4e8b); border-radius:4px')
        self.bg.setStyleSheet('''background-color:#252229;
                    border-top-left-radius:4px;
                    border-top-right-radius:4px;
                    border-bottom-left-radius:2px;
                    border-bottom-right-radius:2px
                    ''')

    def mousePressEvent(self, event):
        self.line_edit.clearFocus()

    def focus_handler(self, status):
        geo = self.geometry()
        w, h = geo.width(), geo.height()
        if status == True:
            self.bg.resize(w, h - 2)
        else:
            self.bg.resize(w, h - 1)

    def resizeEvent(self, event):
        w = event.size().width()
        h = event.size().height()

        self.bg.resize(w, h - 1)
        self.highlight_bg.resize(w, h)
        self.line_edit.setGeometry(8, 0, w - 16, h)