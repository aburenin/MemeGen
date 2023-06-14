"""
MemeGen Application
===================
This is a Python PyQt6 application that uses the apimeme.com API to generate memes.
It allows users to input top and bottom texts and select a meme template to generate a custom meme.
The resulting meme is displayed within the application window.

Classes:
-------
- Memgen(QDialog): This is the main class for the user interface. It inherits from PyQt6's QDialog class.

Methods:
-------
- generate_mem_image(self):
    This method captures the user's input for top and bottom text, and the selected meme template.
    It sends these inputs to the apimeme.com API to generate a meme. The meme image is then
    displayed within the application and the window size is adjusted to fit the meme.

- clear(self):
    This method is used to reset the application by clearing the input fields and hiding the displayed meme.

Functions:
---------
- main():
    This function initializes and displays the PyQt6 application.

Usage:
------
Run the main() function to start the application. Once started, input your desired texts, select a meme
template, and click the 'Generate' button to create a meme. You can clear the input fields and the meme image
by clicking the 'Clear' button.
"""

from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi

from mem_gen_request import generate_meme, list_meme
import sys
import os

class Memgen(QDialog):
    def __init__(self):
        super(Memgen, self).__init__()
        loadUi('dialog_memgen.ui', self)
        self.lb_memimage.hide()
        self.lb_wait.hide()

        self.setWindowTitle("Meme Generator... apimeme.com")

        self.bt_clear.hide()
        self.bt_clear.clicked.connect(self.clear)

        self.bt_download.hide()
        self.bt_download.clicked.connect(self.download_img)

        # Adding elements to QComboBox
        for item in list_meme():
            self.box_meme.addItem(item)

        self.bt_generate.clicked.connect(self.generate_mem_image)

    def generate_mem_image(self):

        top_text = self.le_toptext.text()
        bottom_text = self.le_bottomtext.text()
        meme = self.box_meme.currentText()
        generate_meme(top_text=top_text,bottom_text=bottom_text,meme=meme)
        try:
            self.image = QPixmap('meme.png')
            self.lb_memimage.show()
            self.lb_memimage.setPixmap(self.image)
            self.bt_clear.show()
            self.bt_download.show()
            self.adjustSize()  # Automatically adjust the window size to the image size
            os.remove('meme.png')
        except:
            self.clear()

    def clear(self):
        self.le_toptext.clear()
        self.le_bottomtext.clear()
        self.lb_memimage.hide()
        self.bt_clear.hide()
        self.bt_download.hide()
        self.adjustSize()

    def download_img(self):
        fileName, _ = QFileDialog.getSaveFileName(None)  # Opens a dialog window
        if fileName:
            self.image.save(f'{fileName}.png', 'PNG')  # Save the current image to the chosen location with a PNG format


def main():
    app = QApplication(sys.argv)
    ui = Memgen()
    ui.show()
    app.exec()

if __name__ == '__main__':
    main()
