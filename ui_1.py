import datetime
import os
import sys
import time

from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar,
                             QMenu, QAction, QPlainTextEdit)
from PIL import Image, ImageTk
import xlrd
from PyQt5 import QtCore
import cv2
import xlwt
from xlutils.copy import copy
import pymysql
import pyautogui as g
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, QObject, QTimer, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMessageBox
import log_in  # log_in为 一个label
import qtuntitled1_1
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import find
import demoChangePassword
import new_message
import qtuntitled2
import qtuntitled3
import qtuntitled4  # untitled4 为个人设置
import Display_picture
num =1
tupian = 0
class mywindow_1(QtWidgets.QWidget, qtuntitled1_1.Ui_Form):
    signal_1 = pyqtSignal(str) #定义信号
    def __init__(self):
        super(mywindow_1, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setStyleSheet('''QWidget{background-color:rgb(245, 245, 245);}''')
        self.mywindow_4 = mywindow_4()
        self.mywindow_5 = mywindow_5()
        self.ChangePassword = ChangePassword()
        self.NewMessage = NewMessage()
        self.signal_1.connect(self.NewMessage.getname_2)
        self.signal_1.connect(self.ChangePassword.getname)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)#窗口无标题栏
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)#窗口半透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.name_out()
        self.password_out()
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

    def register_1(self, Form):
        myshow_1.show()
        myshow.close()
    def show_message(self):
        QMessageBox.critical(self, "错误", "系统错误")
    def log_in(self, Form):

        db = pymysql.connect(host='localhost', port=3306, user='root', password="20021123czx", db="mysql", charset='utf8')

        cursor = db.cursor()
        if self.lineEdit.text() == '' or self.lineEdit_2.text() == '':
            self.show_message()
        sql = "SELECT * FROM 已注册"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for it in results:
                List = list(it)
                if List[0] == str(self.lineEdit.text()):
                    if List[1] == str(self.lineEdit_2.text()):
                        data_str = self.lineEdit.text()
                        self.signal_1.emit(data_str)
                        self.name_in(self.lineEdit.text())
                        self.password_in(self.lineEdit_2.text())
                        myshow.close()
                        self.mywindow_4.show()
                        self.mywindow_4.username()
                    else:
                        g.alert('用户名或密码不正确')
        except:
            print("Error: unable to log in db")
        cursor.close()
        db.close()

    def name_out(self):
        with open('保存用户名.txt' , 'r', encoding='utf-8') as file:
            content=file.read()
            self.lineEdit.setText(content)
            file.close()
    def name_in(self,name):
        with open('保存用户名.txt','w',encoding='utf-8') as file:
            file.write(name)
            file.close()
    def password_out(self):
        with open('保存密码.txt','r',encoding='utf-8') as file:
            content=file.read()
            self.lineEdit_2.setText(content)
            file.close()
    def password_in(self,password):
        with open('保存密码.txt','w',encoding='utf-8') as file:
            file.write(password)
            file.close()
    def slot1(self,Form):
        myshow.close()
    def slot2(self, Form):
        myshow.close()
    def mousePressEvent(self, event):
        self.pressX = event.x()  # 记录鼠标按下的时候的坐标
        self.pressY = event.y()
    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()  # 获取移动后的坐标
        moveX = x - self.pressX
        moveY = y - self.pressY  # 计算移动了多少

        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY  # 计算移动后主窗口在桌面的位置
        self.move(positionX, positionY)  # 移动主窗口
class mywindow_2(QtWidgets.QWidget, qtuntitled2.Ui_Form):
    def __init__(self):
        super(mywindow_2, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setStyleSheet('''QWidget{background-color:rgb(245, 245, 245);}''')
        self.Train_lineEdit = self.lineEdit.text()
    def register(self, Form):
        db = pymysql.connect(host='localhost', port=3306, user='root', password="20021123czx", db="mysql", charset='utf8')
        cur = db.cursor()
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        d = self.lineEdit_4.text()
        sql1 = "INSERT INTO 已注册(用户名,密码,性别) VALUES (" + a + ",'" + b + "','" + d + "')"
        if self.lineEdit.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' or self.lineEdit_4.text() == '':
            myshow_2.label.setText('error_1：有信息未填写')
        elif self.lineEdit_2.text() != self.lineEdit_3.text():
            myshow_2.label.setText('error_3：确认密码不正确')
        else:
            try:
                cur.execute(sql1)
                db.commit()
                myshow_2.label.setText("注册成功")
            except:
                print("Error: can't register")
        myshow_2.show()
        myshow_1.close()
        cur.close()
        db.close()
class mywindow_3(QtWidgets.QWidget, log_in.Ui_Form):
    def __init__(self):
        super(mywindow_3, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
class mywindow_4(QtWidgets.QWidget, qtuntitled3.Ui_Form):
    def __init__(self):
        super(mywindow_4, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.label_8.setPixmap(QPixmap("t.png"))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.mu = QMenu()
        action1 = self.mu.addAction("选择输出文件夹")
        action2 = self.mu.addAction("切换账号")
        action3 = self.mu.addAction("查找")
        action1.triggered.connect(self.ceshi)
        action2.triggered.connect(self.qiehuan)
        action3.triggered.connect(self.find)
        self.toolButton.setMenu(self.mu)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        global baocun
        baocun = 0
        self.head_picture1()
        self.fileList()
    def fileList(self):
        self.model01 = QFileSystemModel()
        self.model01.setRootPath("")
        # 定义创建窗口
        self.treeView.setModel(self.model01)
        for col in range(1, 4):
            self.treeView.setColumnHidden(col, True)
        fileDir2 = r'C:\Users\czx\Desktop\object1-10、12'
        self.treeView.setRootIndex(self.model01.index(fileDir2))
    def head_picture1(self):
        with open('头像路径.txt', 'r', encoding='utf-8') as file:
            path=file.read()
        self.label_8.setPixmap(QPixmap(path))
    def amplification(self):
        self.display_picture = Display_picture()
        global tupian
        if tupian !=0:
            with open('图片.txt', 'r', encoding='utf-8') as file:
                path = file.read()
            file.close()
            self.display_picture.show()
            self.display_picture.display(path)
        else:
            g.alert('无图片')
        # global tupian
        # if tupian !=0:
        #     with open('图片.txt' , 'r', encoding='utf-8') as file:
        #         path = file.read()
        #         file.close()
        #         print(path)
        #     QtWidgets.QFileDialog.getOpenFileName(self,  "选取文件",path, "All Files (*);;Text Files (*.png)")
        # else:
        #     g.alert('无图片')
    # pilImage = Image.open("512512.png")
        # pilImage.show()
        # print(34)
        # pilImage = cv2.imread("512512.png")
        # cv2.namedWindow("window_name",cv2.WINDOW_NORMAL)
        # cv2.setWindowProperty("window_name", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # cv2.imshow("window_name",pilImage)
        #cv2.waitKey(1000)
        #cv2.setMouseCallback("window_nam
    def startwork(self):
        global baocun

        if baocun == 1:
            reply1 = QMessageBox.question(self,'提示','上一次处理结果未保存！',QMessageBox.Yes | QMessageBox.No)
            if reply1 == QMessageBox.Yes:
                self.Save_result()
                g.alert('结果已保存')
                baocun = 2
            else:
                pass
        else:
            reply = QMessageBox.question(self,'开始处理','确认开始处理？')
            if reply == QMessageBox.Yes:
                g.alert('处理完成')
                #global baocun
                baocun = 1
            else:
                pass
    def username(self):

        with open('保存用户名.txt' , 'r', encoding='utf-8') as file:
            content=file.read()
            file.close()
        self.label_9.setText(content)
    def instructions(self):
        os.system("start wps.exe C:/Users/czx/Desktop/object1-10、12/说明.doc")
    def Save_result(self):
        global data
        reply = QMessageBox.question(self,'提示','确认保存？')
        if reply == QMessageBox.Yes:
            try:
                file_name = 'records.xls'
                sheet_name = 'Sheet1'
                readbook = xlrd.open_workbook(file_name)
                sheet = readbook.sheet_by_name(sheet_name)

                nrows = sheet.nrows#获取excel的行数
                line_current = nrows + 1#nrows代表当前行数，当前行数加一便是下一次要写的行
                book1 = xlrd.open_workbook(file_name)
                book2 = copy(book1)#由于xlrd只能读不能写，xlwt只能写不能读，所以如果通过xlrd读出的表格内容是没办法进行操作的，因此需要拷贝一份原来的excel
                sheet1 = book2.get_sheet(0)#获取第0个sheet页

                a = self.label_4.text().split(' ')[-1]
                b = self.label_3.text().split(' ')[-1]
                c = self.label_5.text().split(' ')[-1]
                d = self.label_6.text().split(' ')[-1]
                x = self.lineEdit.text().split('：')[-1]
                y = self.lineEdit_2.text().split('：')[-1]
                sheet1.write(nrows,0,line_current-1)
                sheet1.write(nrows,1,x)
                sheet1.write(nrows,2,y)
                sheet1.write(nrows,9,self.textEdit.toPlainText())
                sheet1.write(nrows,3,data[0])
                sheet1.write(nrows,4,data[1])
                sheet1.write(nrows,5,xlwt.Formula('HYPERLINK("{}"; "{}")'.format(data[2], data[2].split('\\')[-1])))
                sheet1.write(nrows,6,a)
                sheet1.write(nrows,7,b)
                sheet1.write(nrows,8,c)
                sheet1.write(nrows,9,d)
                book2.save(file_name)
                global baocun
                baocun = 2
            except:
                print("保存失败")
        else:
            pass
    def psettint(self):
        self.mywindow_5 = mywindow_5()
        self.mywindow_5.show()
        self.mywindow_5.person_message()
        self.close()
    def choose_file(self):

        global tupian
        tupian = 1
        file_name = QFileDialog.getOpenFileName(self,
                                                "选择文件",
                                                "./输入图片/",
                                                "Txt files(*.png)")
        name = file_name[0].split('/')[-1]
        time = datetime.datetime.now()
        now_time = str(time).split('.')[0]
        # result = img.scaled(self.label_1.width(), self.label_1.height(),Qt.KeepAspectRatio)
        # self.label_1.setPixmap(result)
        img = QPixmap(file_name[0])
        with open('图片.txt' , 'w', encoding='utf-8') as file:
            file.write(file_name[0])
            file.close()
        if self.isMaximized():
            pix = img.scaled(850, 850, Qt.KeepAspectRatio)
            self.label_1.setPixmap(QPixmap(pix))
            self.label_1.setAlignment(Qt.AlignCenter)
        else:
            pix = img.scaled(512, 512, Qt.KeepAspectRatio)

            self.label_1.setPixmap(QPixmap(pix))
            self.label_1.setAlignment(Qt.AlignCenter)
        self.label_1.setPixmap(QPixmap(pix))
        self.label_1.setAlignment(Qt.AlignCenter)
        global data
        data= [str(now_time),name,file_name[0]]
    def historical_record(self):
        os.system("start wps.exe C:/Users/czx/Desktop/object1-10、12/records.xls")
    def head(self):
        with open('头像路径.txt', 'r', encoding='utf-8') as file:
            path = file.read()
            file.close()
        self.label_8.setPixmap(QPixmap(path))
        self.label_8.setScaledContents(True)
    def output(self):
        with open('文件夹路径.txt' , 'r', encoding='utf-8') as file:
            content=file.read()
        start_directory = r'%s' % content
        os.startfile(start_directory)
    def qiehuan(self):
        self.close()
        myshow.show()
    def ceshi(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None,"选取文件夹","./")  # 起始路径
        with open('文件夹路径.txt' , 'w', encoding='utf-8') as file:
            file.write(directory)
    def find(self):
        find.show()
    def back_(self):
        global num

        if num %2==1:
            self.stackedWidget.setCurrentIndex(1)
            num += 1
        else:
            self.stackedWidget.setCurrentIndex(0)
            num+=1
    def close_(self):
        global baocun

        if baocun == 1:
            reply1 = QMessageBox.question(self,'提示','结果未保存！',QMessageBox.Yes | QMessageBox.No)
            if reply1 == QMessageBox.Yes:
                self.Save_result()
                g.alert('结果已保存')
                baocun = 2
            else:
                pass
        else:
            reply = QMessageBox.question(self,'提示','确认退出？')
            if reply == QMessageBox.Yes:
                self.close()
            else:
                pass
        #myshow_3.close()
    def big_(self):
        global tupian

        if self.isMaximized():

            if tupian == 1:
                with open('图片.txt' , 'r', encoding='utf-8') as file:
                    content=file.read()
                file.close()
                img = QPixmap(content)
                pix = img.scaled(512, 512, Qt.KeepAspectRatio)
                self.label_1.setPixmap(QPixmap(pix))
                self.label_1.setAlignment(Qt.AlignCenter)
            self.showNormal()
        else:
            if tupian == 1:
                with open('图片.txt' , 'r', encoding='utf-8') as file:
                    content=file.read()

                    file.close()


                img = QPixmap(content)
                pix = img.scaled(850, 850, Qt.KeepAspectRatio)
                self.label_1.setPixmap(QPixmap(pix))
                self.label_1.setAlignment(Qt.AlignCenter)
            self.showMaximized()
    def small(self):
        self.showMinimized()
    def mousePressEvent(self, event):
        self.pressX = event.x()  # 记录鼠标按下的时候的坐标
        self.pressY = event.y()
    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()  # 获取移动后的坐标
        moveX = x - self.pressX
        moveY = y - self.pressY  # 计算移动了多少

        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY  # 计算移动后主窗口在桌面的位置
        self.move(positionX, positionY)  # 移动主窗口
class mywindow_5(QtWidgets.QWidget, qtuntitled4.Ui_Form):
    def __init__(self):
        super(mywindow_5, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("用户管理")
        self.label_8.setScaledContents(True)
        self.mywindow_4 = mywindow_4()
        self.head_picture()

    def head_picture(self):

        with open('头像路径.txt', 'r', encoding='utf-8') as file:
            path = file.read()
        self.label_8.setPixmap(QPixmap(path))
    def person_message(self):
        with open('保存用户名.txt' , 'r', encoding='utf-8') as file:
            name = file.read()
            file.close()
        self.label_9.setText("用户名："+name)
        db = pymysql.connect(host='localhost', port=3306, user='root', password="20021123czx", db="mysql", charset='utf8')
        cursor = db.cursor()
        sql = "SELECT * FROM 已注册"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for it in results:

                List = list(it)
                if List[0] == (name):
                    a =0
                    for i in List:
                        if i == None:
                            List[a] ="未设置"
                            a+=1

                    self.label_10.setText('姓名：'+List[2])
                    self.label_11.setText('科室：'+List[3])
                    self.label_12.setText('性别：'+List[4])
                    self.label_13.setText('医院：'+List[5])
        except:
            g.alert('错误')
    def change_head(self):
        head_picture = QFileDialog.getOpenFileName(self,
                                    "选择头像图片",
                                    "./输出图片/",
                                    "Txt files(*.png)")
        self.label_8.setPixmap(QPixmap(head_picture[0]))
        self.label_8.setScaledContents(True)
        path = head_picture[0]
        with open('头像路径.txt', 'w', encoding='utf-8') as file:
            file.write(path)
            file.close()
        self.mywindow_4.head()
    def closeEvent(self, event):
        self.mywindow_4.show()
        self.mywindow_4.username()
    def message(self):
        new_message.show()
    def changepassword(self):
        changepassword.show()
class ChangePassword(QDialog,demoChangePassword.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("修改密码")
    def SearchRows(self):
        a = self.lineEditOldPassword.text()
        b = self.lineEditNewPassword.text()
        c = self.lineEditRePassword.text()
        if a == '' or b == '' or c == '':
            self.labelResponse.setText('未输入完全')
        else:
            if b !=c:
                self.labelResponse.setText('两次密码不一致')
            else:
                reply = QMessageBox.question(self,'提示','确认修改密码？')
                if reply == QMessageBox.Yes:
                    self.Modify()
                else:
                    pass


    def Modify(self):
        #print(self.mywindow_4.label_9.text())

        db = pymysql.connect(host='localhost', port=3306, user='root', password="20021123czx", db="mysql", charset='utf8')
        print(235)
        global name1
        print(name1)
        cur = db.cursor()#建立游标
        print(1)
        password = str(self.lineEditNewPassword.text())
        print(password)

        cur.execute("update 已注册 set 密码='"+password+"' where 用户名='"+name1+"' ")
        print(2)
        db.commit()
        g.alert(text='密码修改成功',title='密码修改成功',button='确定')
        self.close()
    def getname(self,name):
        global name1
        name1 = name
class NewMessage(QDialog,new_message.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("修改个人信息")
        self.changepassword = ChangePassword()
        self.mywindow_4 = mywindow_4()
    def getname_2(self,name):
        global name2
        name2 = name
    def Modify_Message(self):
        reply = QMessageBox.question(self,'提示','确认修改个人信息？')
        if reply == QMessageBox.Yes:
            a = str(self.lineEdit.text())
            b = str(self.lineEdit_2.text())
            c = str(self.lineEdit_3.text())
            d = str(self.lineEdit_4.text())

            db = pymysql.connect(host='localhost', port=3306, user='root', password="20021123czx", db="mysql", charset='utf8')
            global name2

            cur = db.cursor()#建立游标
            cur.execute("update 已注册 set 姓名='"+a+"' where 用户名='"+name2+"' ")

            cur.execute("update 已注册 set 科室='"+b+"' where 用户名='"+name2+"' ")
            cur.execute("update 已注册 set 医院='"+c+"' where 用户名='"+name2+"' ")
            cur.execute("update 已注册 set 性别='"+d+"' where 用户名='"+name2+"' ")

            db.commit()
            g.alert(text='信息修改成功',title='信息修改成功',button='确定')
            self.mywindow_5 = mywindow_5()
            self.mywindow_5.person_message()
            self.close()
        else:
            pass
class Find(QDialog,find.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("查找")
    def picture_show(self):
        with open('文件夹路径.txt' , 'r', encoding='utf-8') as file:
            content=file.read()
        os.startfile(content)
    def find_message(self):
        if self.lineEdit.text() =='':
            g.alert("请输入病历号！")
        a = self.lineEdit.text()
        file_name = 'records.xls'
        sheet_name = 'Sheet1'
        readbook = xlrd.open_workbook(file_name)
        sheet = readbook.sheet_by_name(sheet_name)
        cols = sheet.col_values(2)
        x = 0
        for i in cols:
            if i == int(a):
                data = sheet.row_values(x)

                self.label_2.setText('病历号：'+str(data[2]))

                self.label_3.setText('患者名：'+str(data[1]))
                self.label_4.setText('处理时间：'+str(data[3]))
                self.label_5.setText('备注：'+str(data[11]))
                self.label_6.setText('切片数：'+str(data[6]))
                self.label_7.setText('空洞体积：'+str(data[9]))
                self.label_8.setText('空洞类型：'+str(data[7]))
                self.label_9.setText('空洞数量：'+str(data[8]))
            else:
                x+=1

class Display_picture(QDialog,Display_picture.Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("图片显示")
    def display(self,picture_path):
        self.label_0.setPixmap(QPixmap(picture_path))
        self.label_0.setScaledContents(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = mywindow_1()  # 登录界面
    #myshow.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint )
    myshow_1 = mywindow_2()  # 注册界面
    myshow_2 = mywindow_3()  # label界面
    myshow_3 = mywindow_4()  # 主界面
    myshow_4 = mywindow_5()  # 个人设置
    changepassword = ChangePassword()
    new_message = NewMessage()
    find = Find()
    display_picture = Display_picture()
    myshow.show()
    sys.exit(app.exec_())
