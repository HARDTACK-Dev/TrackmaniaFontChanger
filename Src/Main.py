 #http://www.gisdeveloper.co.kr/?p=8328 연동 참고
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
from PyQt5.QtCore import QRect, QSize

preview_label = []


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("GUI/Main.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #Fix Window Size
        self.setFixedSize(804, 513)
        #Window Icon
        self.setWindowIcon(QIcon('Icons/Icon.ico'))

        #Window Title
        self.setWindowTitle('TM Fonter - Settings')

        #Setup Icons - QAction
        Settings = QAction(QIcon(QPixmap("Icons/Gear.png")), "Settings        ", self) #./ for Abspath
        AddFonts = QAction(QIcon(QPixmap("Icons/Alphabet.png")), "AddFonts      ", self)

        #Setup Menubar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&Options')
        #Add Menus to Menubar
        filemenu.addAction(Settings)
        filemenu.addAction(AddFonts)

        self.main()




        #Menu Triggers - 메뉴바 트리거
        Settings.triggered.connect(self.OpenSettings) #self.OpenSettings은 함수이름

        AddFonts.triggered.connect(self.OpenAddFonts) 


        
    ### Main Task
    def main(self):

        # OriginList : Array of Displaying Font lists
        # OriginFList: Array of Original fonts Folder below /Fonts

        #set Default Preview when program start
        # self.DefaultPreview.setPixmap(QtGui.QPixmap("Fonts/Original/Default/Default.png"))
        # self.DefaultPreview.resize(540, 290)
        # self.DefaultPreview.move(250, 30)
        

        
            

        # try:
            OriginLIST = open('Fonts/Original/List.dat', 'r').read().split('\n')
            print(OriginLIST)

            loop = len(OriginLIST)
            print(loop)

            OriginFList = os.listdir("Fonts/Original")
            # print(OriginFList)


            for x in OriginLIST:
                self.MainList.addItem(QListWidgetItem(QIcon("Icons/Original.png" ), x))
                self.MainList.setIconSize(QtCore.QSize(7, 7))


                self.previewList = {}
                self.posOfPrev = 250

                # pixmap = QPixmap("Fonts/Original/Default/Default.png")


            for i in range(loop): #[i] 대신 [(i)]e
                self.previewList[(i)] = QLabel("", self)
                # self.previewList[i].resize(540, 290)
                self.previewList[i].move(250, 35)
                self.previewList[i].setPixmap(QtGui.QPixmap("Fonts/Original/Default/Default.png"))
                self.previewList[i].setGeometry(QtCore.QRect(256, 32, 540, 290))
                
                


                
                
                


        # except:
        #     print("Error!")
        #     QMessageBox.warning(self, "Error!", "Failed to read Font lists  :/               \n")
        #     app.exec_
        


    
    def OpenSettings(self):
        Settings.SettingClass().showSettings() #Settings.py파일에 SettingClass클래스에 ShowSettings함수 실행
        
    def OpenAddFonts(self):
        CustomList.CustomlistClass().showCustomList()


        


    


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
    #윈도우창 창 최소화와 닫기만 뜨게
    # myWindow.setWindowFlags( QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)

    #프로그램 화면을 보여주는 코드
    myWindow.show()
    

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

   

   