import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from main_window_py import MAIN_TEMPLATE
from dict_window import DictWindow
from di import di
from change_di import change_di
from ai import call_da_ai_for_word, call_da_ai_for_sentence


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(MAIN_TEMPLATE)
        uic.loadUi(f, self)
        self.dictionary_button.clicked.connect(self.open_dict)
        self.dict_search.clicked.connect(self.distribution)


    def distribution(self):
        if self.sentence_button.isChecked():
            self.translate_sentence()
        else:
            self.translate_word()


    def translate_sentence(self):
        ai_reply = call_da_ai_for_sentence(self.main_text_edit.text())
        self.translated_text.setText(ai_reply)
        
    
    def translate_word(self):
        if di.get(self.main_text_edit.text().lower()):
            self.translated_text.setText(di.get(self.main_text_edit.text()))
        else:
            ai_reply = call_da_ai_for_word(self.main_text_edit.text())
            change_di(self.main_text_edit.text().lower(), ai_reply)
            self.translated_text.setText(ai_reply)

    def open_dict(self):
        self.dict_window = DictWindow()
        self.dict_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())