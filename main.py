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
from Engine import Engine

signs = 0
signs2 = 0
memory = 0
memory2 = 0
answ = 0
step = 0
symbol = [0, 0]


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
        print('init completed'); #test
        #window properties of the main classи     
        for n in range(0, 10):
            getattr(self, 'btn%s' % n).pressed.connect(lambda v=n: self.on_click(v))
        
        self.btn_plus.pressed.connect(lambda: self.operation(self.btn_plus.text()))
        self.btn_minus.pressed.connect(lambda: self.operation(self.btn_minus.text()))
        self.btn_div.pressed.connect(lambda: self.operation(self.btn_div.text()))
        self.btn_mult.pressed.connect(lambda: self.operation(self.btn_mult.text()))   
        self.btn_eq.pressed.connect(self.equal)
        self.btn_clear.pressed.connect(self.clear)
        
    
    def on_click(self,v):
        global signs, memory
        signs+=1
        if signs > 1:
            memory = memory*10+v
            self.display(memory)
        else:
            memory = v
            self.display(memory)
        print(signs)   
 
    def operation(self,text):
        global memory, first_mem, a_sign
        first_mem = memory
        memory = 0
        self.display(memory)
        a_sign = text
        print(text)
        
    def equal(self):
        global first_mem, memory, sign, a_sign
        e = Engine()
        answ = e.compute(first_mem, memory, a_sign)
        self.display(answ)
        memory = answ
        sign = 0
    def clear(self):
        global signs, memory
        signs = 0
        memory = 0
        print(memory);print(signs)
        self.display(memory)
        
    
    def display(self, memory):
        self.lcdNumber.display(memory)


class Monitor():
    def __init__(self,value):
        self.lcdNumber.display(value)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start(css_filepath)
    ex.show()
    sys.exit(app.exec_())
