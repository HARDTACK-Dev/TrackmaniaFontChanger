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
form_class = uic.loadUiType("GUI/CustomList.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class CustomlistClass(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #Window Title
        self.setWindowTitle('TM Fonter - Custom Fonts')
        #Window Icon
        self.setWindowIcon(QIcon('Icons/Icon.ico'))
        #Fix Window Size
        self.setFixedSize(520, 275)

        #Setup Icons    
        self.AlphabetIcon.setPixmap(QtGui.QPixmap("Icons/Alphabet.png"))

        #Setup Icon - Buttons
        self.Btn_FontListDone.setIcon(QtGui.QIcon('Icons/Check.png'))
        self.Btn_FontListDone.setIconSize(QtCore.QSize(16,16))


        #Triggers - 실행함수들
        self.Btn_AddList.clicked.connect(self.OpenCustomAdd)

    def OpenCustomAdd(self):
        CustomAdd.CustomAddClass().showCustomAdd()


        


        

    #메인 윈돋우에서 불러올 함수
    def showCustomList(self):
        # 모달 (다이얼로그) ? 표시 지우기    
        super().setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        return super().exec_()