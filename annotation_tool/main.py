# -*- coding: utf-8 -*-
import sys
import os
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Annotation Tool'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 640
        self.lb_size = 500
        self.curdir = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.loadImageDialog()
        self.setMouseTracking(False)

        self.show()

    def loadImageDialog(self):
        self.label = QLabel("", self)
        self.label.move(20, 20)
        self.label.resize(self.lb_size, self.lb_size)

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

        return [self.curdir + '/' + file_name for file_name in file_list if p.search(file_name)]

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Image Files (*.jpg, *.jpeg, *.png, *.JPG)", options=options)
        self.curdir = os.path.dirname(fileName)

        if fileName:
            self.curdir_file_list = self.load_file_list_curdir()
            self.idx = self.curdir_file_list.index(fileName)
            self.num_file = len(self.curdir_file_list)
            self.load_image()

    def clicked_next(self):
        if self.curdir:
            self.idx = self.check_minmax(self.idx + 1)
            self.load_image()

    def clicked_prev(self):
        if self.curdir:
            self.idx = self.check_minmax(self.idx - 1)
            self.load_image()

    def load_image(self):
        print(self.curdir_file_list[self.idx])
        pixmap = QPixmap(self.curdir_file_list[self.idx])
        self.ratio = [float(pixmap.width()/self.lb_size), float(pixmap.height()/self.lb_size)]
        self.org_pixmap = pixmap.scaled(self.lb_size, self.lb_size)
        self.label.setPixmap(self.org_pixmap)

    def check_minmax(self, _idx):
        if _idx < 0:
            return 0
        elif _idx >= self.num_file:
            return self.num_file-1
        else:
            return _idx

    def mousePressEvent(self, e):
        if e.buttons() & Qt.LeftButton and self.curdir:

            print(e.x(), e.y())
            self.label.setPixmap(self.org_pixmap)
            painter = QPainter(self.label.pixmap())

            pen = QPen(Qt.red)
            pen.setWidth(5)
            painter.setPen(pen)
            painter.drawPoint(e.x()-20, e.y()-20)

        self.label.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

#  A  A
# (‘ㅅ‘=)
# J.M.Seo