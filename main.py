import sys
from PyQt5.QtWidgets import QApplication,QMessageBox,QLineEdit # QPlainTextEdit, ,QWidget
from PyQt5.QtWidgets import QDialog,QMainWindow, QLabel # 14.04.21 added QHBoxLayout, QLabel deleted: , QHBoxLayout, QScrollArea,QVBoxLayout, QAbstractItemView, QListWidget,QListWidgetItem, QPushButton, QFileDialog,
#from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic #, QtGui,QtCore
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QPixmap # 14.04.21 added line 8
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
import os, subprocess, platform #16.04.21 added subprocess and platform
#import numpy as np
import pickle

uifile_0 = os.path.join("ui","main_window.ui");

css_filepath = os.path.join("ui","css","css.css")

form_0, base_0 = uic.loadUiType(uifile_0)


class CssMainWindow(QMainWindow):
    def __init__(self,css_filepath):
        super().__init__();
        ##http://doc.crossplatform.ru/qt/4.5.0/stylesheet-reference.html         
        #set stylesheet
        f = open(css_filepath, 'r');
        css_string = f.read();
        f.closed;     
        self.setStyleSheet(css_string);
        self.output_dictionary={};


class Start(CssMainWindow, form_0):
    def __init__(self,css_filepath):
        super().__init__(css_filepath);
        self.setupUi(self)
        self.css=css_filepath;
        #window properties of the main class
        self.inputWin=[];
        self.outputWin=[];

        #test
        print('init completed');


if __name__ == '__main__':
    pass;
    app = QApplication(sys.argv)
    ex = Start(css_filepath)
    ex.show()
    sys.exit(app.exec_())