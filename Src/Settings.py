import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui #include QIcon nand QPixmap
from PyQt5.QtGui import * 
from PyQt5 import uic
from PyQt5 import QtCore
# from PyQt5 import QtCore, QtGui, QtWidgets #include QtGui

#import Other Form/py Files
import Settings
import CustomAdd
import CustomList



#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("GUI/Settings.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class SettingClass(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


        #Window Title
        self.setWindowTitle('TM Fonter - Settings')
        #Window Icon
        self.setWindowIcon(QIcon('Icons/Icon.ico'))
        #Fix Window Size
        self.setFixedSize(519, 154)


        #Icons - label
        self.GearIcon.setPixmap(QtGui.QPixmap("Icons/Gear.png"))

        self.DiscordIcon.setPixmap(QtGui.QPixmap("Icons/Discord.png"))
        
        #Icons - Buttons
        self.Btn_Gamepath.setIcon(QtGui.QIcon('Icons/Browse.png'))
        self.Btn_Gamepath.setIconSize(QtCore.QSize(16,16))
        


        
        
        # 모달 (다이얼로그) ? 표시 지우기
        # super().setWindowFlags(QtCore.Qt.WindowCloseButtonHint)


    #메인 윈돋우에서 불러올 함수
    def showSettings(self):
        # 모달 (다이얼로그) ? 표시 지우기
        super().setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        return super().exec_()