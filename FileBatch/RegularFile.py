"""pip install pyqt5"""
# -*- coding: utf-8 -*-

import re
import os

# ---------以下为PyQt5自动生成--------
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 581, 331))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelChaZhao = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelChaZhao.setObjectName("labelChaZhao")
        self.verticalLayout.addWidget(self.labelChaZhao)
        self.lineEditChaZhao = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEditChaZhao.setObjectName("lineEditChaZhao")
        self.verticalLayout.addWidget(self.lineEditChaZhao)
        self.listWidgetChaZhao = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.listWidgetChaZhao.setObjectName("listWidgetChaZhao")
        self.verticalLayout.addWidget(self.listWidgetChaZhao)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTiHuan = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelTiHuan.setObjectName("labelTiHuan")
        self.verticalLayout_2.addWidget(self.labelTiHuan)
        self.lineEditTiHuan = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEditTiHuan.setObjectName("lineEditTiHuan")
        self.verticalLayout_2.addWidget(self.lineEditTiHuan)
        self.listWidgetTiHuan = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.listWidgetTiHuan.setObjectName("listWidgetTiHuan")
        self.verticalLayout_2.addWidget(self.listWidgetTiHuan)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEditLuJing = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEditLuJing.setObjectName("lineEditLuJing")
        self.horizontalLayout_3.addWidget(self.lineEditLuJing)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButtonWenJian = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButtonWenJian.setObjectName("radioButtonWenJian")
        self.horizontalLayout_2.addWidget(self.radioButtonWenJian)
        self.radioButtonMuLu = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButtonMuLu.setObjectName("radioButtonMuLu")
        self.horizontalLayout_2.addWidget(self.radioButtonMuLu)
        self.radioButtonQuanBu = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButtonQuanBu.setObjectName("radioButtonQuanBu")
        self.horizontalLayout_2.addWidget(self.radioButtonQuanBu)
        self.pushButtonYuLan = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButtonYuLan.setObjectName("pushButtonYuLan")
        self.horizontalLayout_2.addWidget(self.pushButtonYuLan)
        self.pushButtonTiHuan = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButtonTiHuan.setObjectName("pushButtonTiHuan")
        self.horizontalLayout_2.addWidget(self.pushButtonTiHuan)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ---------以上为PyQt5自动生成--------

        #获取当前路径为默认路径
        self.lineEditLuJing.setText(os.getcwd())
        #出栈历史记录
        self.listWidgetChaZhao.clicked.connect(lambda index: self.lineEditChaZhao.setText(self.listWidgetChaZhao.takeItem(index.row()).text()))
        self.listWidgetTiHuan.clicked.connect(lambda index: self.lineEditTiHuan.setText(self.listWidgetTiHuan.takeItem(index.row()).text()))
        #执行操作
        self.pushButtonYuLan.clicked.connect(lambda: self.zhixing(0))
        self.pushButtonTiHuan.clicked.connect(lambda: self.zhixing(1))
        #文件默认勾选
        self.radioButtonWenJian.setChecked(1)

    # 默认生成
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "REname"))
        self.labelChaZhao.setText(_translate("MainWindow", "查找"))
        self.labelTiHuan.setText(_translate("MainWindow", "替换"))
        self.label.setText(_translate("MainWindow", "路径"))
        self.radioButtonWenJian.setText(_translate("MainWindow", "文件替换"))
        self.radioButtonMuLu.setText(_translate("MainWindow", "目录替换"))
        self.radioButtonQuanBu.setText(_translate("MainWindow", "全部替换"))
        self.pushButtonYuLan.setText(_translate("MainWindow", "预览"))
        self.pushButtonTiHuan.setText(_translate("MainWindow", "替换"))

    # 核心函数
    def zhixing(self, status):
        os.system("cls")
        #奇技，实现do-while，为真说明可能重命名未能全部执行
        loopStatus = True
        while loopStatus:
            loopStatus = False
            #路径
            path = self.lineEditLuJing.text()
            #遍历所有文件和子目录
            for root, dir, file in os.walk(path):
                for name in file:
                    # print("FILE"+os.path.join(root,name))
                    #正则
                    res=re.sub(re.compile(self.lineEditChaZhao.text()),self.lineEditTiHuan.text(),name)
                    #判断文件
                    if name!=res and (self.radioButtonWenJian.isChecked() or self.radioButtonQuanBu.isChecked()) :
                        print(os.path.join(root,name))
                        #实现↓的位置
                        byts = self.lineEditChaZhao.text().encode('gbk')
                        print(len(root.encode('gbk'))*" "+'\\'+(name.encode('gbk').find(byts)*" ")+"*"*len(byts))
                        print(os.path.join(root,res)+"\n\n")

                        if status:
                            #异常处理，bug很多，放弃
                            try:
                                os.rename(os.path.join(root,name),os.path.join(root,res))
                                loopStatus = True
                                self.statusbar.showMessage("执行结束",0)
                            except:
                                self.statusbar.showMessage("文件重命名存在错误，请检查后重试",0)
                                break
                #同上
                for name in dir:
                    #print("DIR"+os.path.join(root,name))
                    res=re.sub(re.compile(self.lineEditChaZhao.text()),self.lineEditTiHuan.text(),name)
                    if name!=res and (self.radioButtonMuLu.isChecked() or self.radioButtonQuanBu.isChecked()):
                        print(os.path.join(root,name))
                        byts = self.lineEditChaZhao.text().encode('gbk')
                        print(len(root.encode('gbk'))*" "+'\\'+(name.encode('gbk').find(byts)*" ")+"*"*len(byts))
                        print(os.path.join(root,res)+"\n\n")

                        if status :
                            try:
                                os.rename(os.path.join(root,name),os.path.join(root,res))
                                loopStatus = True
                                self.statusbar.showMessage("执行结束",0)
                            except:
                                self.statusbar.showMessage("目录重命名存在错误，请检查后重试",0)
                                break
        #排除重复
        if not self.listWidgetChaZhao.findItems(self.lineEditChaZhao.text(), QtCore.Qt.MatchFlag.MatchExactly):
            self.listWidgetChaZhao.addItem(self.lineEditChaZhao.text())
        if not self.listWidgetTiHuan.findItems(self.lineEditTiHuan.text(), QtCore.Qt.MatchFlag.MatchExactly):
            self.listWidgetTiHuan.addItem(self.lineEditTiHuan.text())
#---以下为自动生成----
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())