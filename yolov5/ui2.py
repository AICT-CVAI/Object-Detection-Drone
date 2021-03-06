import os
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
import threading
import cv2
from PyQt5.QtCore import QCoreApplication, QThread
from subprocess import call
form_class = uic.loadUiType("gui.ui")[0]
import tkinter as tk
from tkinter import messagebox

class WindowClass(QMainWindow, form_class) :
    def __init__(self):
    
        super().__init__()
        self.setupUi(self)
        
        # self.work = Worker()

        
        
        self.gpspath = "gps/"
        self.slicepath = "ui_test/"
        
        self.btn_1.clicked.connect(self.btn_videoslice)
        self.btn_2.clicked.connect(self.btn_yolo)
        self.btn_3.clicked.connect(self.btn_potholemap)
        self.btn_5.clicked.connect(self.btn_clear)
        self.btn_4.clicked.connect(QCoreApplication.instance().quit)

    def btn_videoslice(self):
        self.textBrowser_2.append("Slice Start")
        fname = QFileDialog.getOpenFileName(self)
        print(fname[0])

        vidcap = cv2.VideoCapture(fname[0])
        success,image = vidcap.read()
        
        count = 1
        success = True
        
        while success:
            cv2.imwrite("ui_test/%d.jpg" % count, image)
            success,image = vidcap.read()
            print("saved image %d.jpg" % count)
            
            count += 1
            
        self.textBrowser_2.append("Slice Finish")
            
        vidcap.release()
        
        
    def btn_yolo(self):
        self.textBrowser_2.append("Detect start!!")
        time.sleep(1)
        os.system('python3 detect_result.py --source data/test.mp4 --weights weights/drone_survivor.pt --classes 0 --project ui_test --img 3840 --conf 0.6 --save-txt')
        QApplication.processEvents()
        self.textBrowser_2.append("Detect Finish!!")
        self.textBrowser_2.append("Go to ui_test folder")
        # self.work.start()
        fname = QFileDialog.getOpenFileName(self)
        
    
    def btn_potholemap(self):
        self.textBrowser_2.append("신고되었습니다!")
        root = tk.Tk()
        msg = messagebox.showwarning(title='Person Detect!', message='Notification')
        if msg == 'ok':
            root.destroy()
        # time.sleep(1)
        #os.system('python3 matching.py')    # Shin Go
        #self.textBrowser_2.append("Mapping file save!!")
        
        
    def btn_clear(self) :
        self.textBrowser_2.append("Data Clear Start")
        if os.path.isdir(self.gpspath):
            filelist1 = os.listdir(self.gpspath)
            for file in filelist1:
                os.remove(self.gpspath + file)
        else:
            self.textBrowser_2.append("GPS Folder not exist!")
        
        if os.path.isdir(self.slicepath):
            filelist2 = os.listdir(self.slicepath)
            for file in filelist2:
                os.remove(self.slicepath + file)
        else:
            self.textBrowser_2.append("Slice Folder not exist!")
        self.textBrowser_2.append("GPS and Slice Data clear")
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
