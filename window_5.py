# file:mywindow_5.py
# time:2022/11/8 16:40
import datetime
import os
import sys
import time

from PyQt5.QtCore import QObject , pyqtSignal
import xlrd
from PyQt5 import QtCore
import xlsxwriter
import xlwt
from xlutils.copy import copy
import pymysql
import pyautogui as g
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, QObject, QTimer, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMessageBox
import PyQt5
import log_in  # log_in为 一个label
import qtuntitled1  # untitled1 为登录界面
import qtuntitled1_1
import qtuntitled3_3
import demoChangePassword
import new_message
import qtuntitled33
# encoding:utf8
# ui_1 为主程序
import qtuntitled2
import qtuntitled3
import qtuntitled4  # untitled4 为个人设置
#num = 1
#import mywindow_4
class mywindow_5(QtWidgets.QWidget, qtuntitled4.Ui_Form):
    #signal_2 = pyqtSignal(str) #定义信号
    def __init__(self):
        super(mywindow_5, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.label_8.setPixmap(QPixmap('1413012235-43G.png'))  # 图片路径
        self.label_8.setScaledContents(True)
        #self.person_message()
    def person_message(self,name):
        db = pymysql.connect(host='localhost', port=3306, user='root', password="20021123czx", db="注册表", charset='utf8')
        cursor = db.cursor()
        sql = "SELECT * FROM 已注册"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for it in results:
                List = list(it)
                if List[0] == (name):
                    print(List)
                    a = '姓名：'+str(List[2])
                    b = '科室：'+str(List[3])
                    c = '性别：'+str(List[4])
                    d = '医院：'+str(List[5])
                    self.setupUi(self)
                    self.label_10.setText(a)
                    self.label_11.setText(b)
                    self.label_12.setText(c)
                    self.label_13.setText(d)
                    #QApplication.processEvents()
                    print(self.label_10.text())
                    print(self.label_11.text())
                    print(self.label_12.text())
                    print(self.label_13.text())
        except:
            g.alert('错误')

    def change_head(self):
        head_picture = QFileDialog.getOpenFileName(self,
                                                   "选择头像图片",
                                                   "./输出图片/",
                                                   "Txt files(*.png)")
        #print(head_picture)
        self.label_8.setPixmap(QPixmap(head_picture[0]))
        self.label_8.setScaledContents(True)
        #print(head_picture[0])
        #self.signal_2.emit(head_picture[0])
        self.mywindow_4 = mywindow_4()

        self.mywindow_4.head(head_picture[0])

        #print(1)
    def message(self):
        new_message.show()
    def changepassword(self):
        changepassword.show()