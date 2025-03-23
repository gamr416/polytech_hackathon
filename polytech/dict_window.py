import io
import sys


from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from di import di
from dict_py import DICT_TEMPLATE


class DictWindow(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(DICT_TEMPLATE)
        uic.loadUi(f, self)
        string_for_di =  [f'{list(di.keys())[i]}: {di[list(di.keys())[i]]}' for i in range(len(di.keys()))]

        self.main_dict.setText('\n'.join(string_for_di))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DictWindow()
    ex.show()
    sys.exit(app.exec_())