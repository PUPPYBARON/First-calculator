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
        self.lcdNumber.value()
        global answ
        #e = Engine()
        #window properties of the main class
   #Разберитесь с 47 и 48 строками     
        for n in range(0, 10):
            getattr(self, 'btn%s' % n).pressed.connect(lambda v=n: self.on_click(v))
        
        self.btn_clear.pressed.connect(self.clear)
        self.btn_plus.pressed.connect(self.plus)
        self.btn_minus.pressed.connect(self.minus)
        self.btn_div.pressed.connect(self.div)
        self.btn_mult.pressed.connect(self.mult)
        self.btn_eq.pressed.connect(self.eq)
        
        #test
        print('init completed');

    
    
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
    
    def plus(self):
        global answ
        e = Engine()
        answ = e.compute(memory,self.btn_plus.text())
        
    def minus(self):
        global answ
        e = Engine()
        answ = e.compute(memory,self.btn_minus.text())
        
    def div(self):
        global answ
        e = Engine()
        answ = e.compute(memory,self.btn_div.text())
        
    def mult(self):
        global answ
        e = Engine()
        answ = e.compute(memory,self.btn_mult.text())
    
    def eq(self):
        self.display(answ)
    
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
