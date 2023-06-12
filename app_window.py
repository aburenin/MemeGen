from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt6.QtCore import QTimer, QThread
from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi

from mem_gen_request import generate_meme, list_meme
import sys, time

class Memgen(QDialog):
    def __init__(self):
        super(Memgen, self).__init__()
        loadUi('dialog_memgen.ui', self)
        self.lb_memimage.hide()
        self.lb_wait.hide()
        #self.resize(self.width(), 200)

        self.setWindowTitle("Meme Generator... apimeme.com")

        # Добавляем элементы в QComboBox
        for item in list_meme():
            self.box_meme.addItem(item)

        self.bt_generate.clicked.connect(self.generate_mem_image)

    def generate_mem_image(self):
        top_text = self.le_toptext.text()
        bottom_text = self.le_bottomtext.text()
        meme = self.box_meme.currentText()
        generate_meme(top_text=top_text,bottom_text=bottom_text,meme=meme)
        self.lb_memimage.show()
        self.lb_memimage.setPixmap(QPixmap('meme.png'))
        self.adjustSize()  # Автоматически подгоняем размер окна под размер изображения

def main():
    app = QApplication(sys.argv)
    ui = Memgen()
    ui.show()
    app.exec()

if __name__ == '__main__':
    main()
