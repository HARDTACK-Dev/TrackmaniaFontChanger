import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui #include QIcon nand QPixmap
from PyQt5.QtGui import * 
from PyQt5 import uic
from PyQt5 import QtCore

#import Other Form/py Files
import Settings
import CustomAdd
import CustomList


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("GUI/CustomAdd.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class CustomAddClass(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #Window Title
        self.setWindowTitle('TM Fonter - Custom Fonts')
        #Window Icon
        self.setWindowIcon(QIcon('Icons/Icon.ico'))
        #Fix Window Size
        self.setFixedSize(546, 191)

        #Setup Icons    
        self.Btn_Preview.setIcon(QtGui.QIcon("Icons/AddFontPreview.png"))

        #Icons - Buttons
        self.Btn_DDSPath.setIcon(QtGui.QIcon('Icons/Browse.png'))
        self.Btn_DDSPath.setIconSize(QtCore.QSize(16,16))

        


        


    #메인 윈도우에서 불러올 함수
    def showCustomAdd(self):
        # 모달 (다이얼로그) ? 표시 지우기
        super().setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        return super().exec_()