# -*- coding: utf-8 -*-
import sys
import os
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Annotation Tool'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 640
        self.curdir = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.loadImageDialog()
        # self.openFileNameDialog()
        # self.openFileNamesDialog()
        # self.saveFileDialog()

        self.show()

    def loadImageDialog(self):
        self.label = QLabel("", self)
        self.label.move(20, 20)
        self.label.resize(450, 450)

        load_btn = QPushButton("Load", self)
        load_btn.move(20, 600)
        load_btn.clicked.connect(self.openFileNameDialog)

        next_btn = QPushButton("Prev", self)
        next_btn.move(140, 600)
        next_btn.clicked.connect(self.clicked_prev)

        prev_btn = QPushButton("Next", self)
        prev_btn.move(260, 600)
        prev_btn.clicked.connect(self.clicked_next)

    def load_file_list_curdir(self):
        file_list = sorted(os.listdir(self.curdir))
        p = re.compile(".*[.](?=png$|jpg$|jpeg$|PNG$|JPG$|JPEG$).*$")

        #return [os.path.join(self.curdir, file_name) for file_name in file_list if p.search(file_name)]
        return [self.curdir + '/' + file_name for file_name in file_list if p.search(file_name)]

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Image Files (*.jpg, *.jpeg, *.png, *JPG)", options=options)
        self.curdir = os.path.dirname(fileName)

        if fileName:
            self.curdir_file_list = self.load_file_list_curdir()
            print(self.curdir_file_list)
            print(fileName)
            self.label.setPixmap(QPixmap(fileName))
            self.idx = self.curdir_file_list.index(fileName)
            self.num_file = len(self.curdir_file_list)

    def clicked_next(self):
        if self.curdir:
            self.idx = self.check_minmax(self.idx + 1)
            self.label.setPixmap(QPixmap(self.curdir_file_list[self.idx]))
            print(self.curdir_file_list[self.idx])

    def clicked_prev(self):
        if self.curdir:
            self.idx = self.check_minmax(self.idx - 1)
            self.label.setPixmap(QPixmap(self.curdir_file_list[self.idx]))
            print(self.curdir_file_list[self.idx])

    def check_minmax(self, _idx):
        if _idx < 0:
            return 0
        elif _idx >= self.num_file:
            return self.num_file-1
        else:
            return _idx

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())