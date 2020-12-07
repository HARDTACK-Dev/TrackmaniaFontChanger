

![](https://img.shields.io/badge/Game-Trackmania-lightgrey) ![](https://img.shields.io/badge/Version-2.0-orange) ![](https://img.shields.io/badge/License-GPL-blue)

### 																		Trackmania Fonter  (v2.0)

------

###### 															  A Program that can change displayed fonts on TrackMania United<img src="C:\Users\건빵\Desktop\포트폴리오\TM Fonter V2\Icons\TMUF.png" style="zoom:8%;" /> / Nations<img src="C:\Users\건빵\Desktop\포트폴리오\TM Fonter V2\Icons\TMNF.jpeg" style="zoom:5%;" />

​																			        											by <img src="C:\Users\건빵\Pictures\프로필.png" style="zoom:10%;" /> Hardtack

​                                                                                                                                 



![image-20201207123801321](C:\Users\건빵\AppData\Roaming\Typora\typora-user-images\image-20201207123801321.png)

 

#####  																			※ before using, This program is not officially made by Nadeo



​																															[View Changlog]( Readme.md "Changelog")



#### What can I change?

---

- Clock on menu bar
- Scoreboard on Ladder
- Speed meter
- In-game Timer



#### Dependencies

---

Program Written in ![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" = 5x5)Python / Pyqt5, *You can also see all source code on GitHub repo*



#### How It's Work

----

The working principle of this program is to transfer the custom font file to the TrackMania installation folder 

> ```python
> \GameData\Interface\media\fonds\RedTexture\Led_00.dds
> ```

It replacing the `Led_00.dds` file to Customized Font file, So that game read.

So if you want to restore, just backup Default dds file or Copy it From `Fonts\Original\Default`  :)





#### Changelog 

---

### [ v2.0 ](https://github.com/HARDTACK-Dev/TrackmaniaFontChanger/releases/tag/v2.0)  - 2020-12-07

### Added

- **Remade with Python3 / PyQt5**
- UI/UX Redesigned
- Support Add Custom .DDS(font) file
- **`17`** Font Added 



----



#### [ v1.0 ](https://github.com/HARDTACK-Dev/TrackmaniaFontChanger/releases/tag/v1.0)  - 2020-04-13

#### Added

- First Release

- Written with AHK Script
- **`17`** Font Added 







#### Folder Structure

---

```

├── Fonts/
│   ├── Custom/
│   │   ├── FontsFiles
│   │   └── list.dat
│   └── Original/
│       ├── Font Files
│       └── list.dat   
├── GUI/
│   ├── Main.ui
│   ├── Settings.ui
│   ├── CustomList.ui
│   └── CustomAdd.ui
├── Icons/
│   └── Image Resources
└── Src/
    ├── Main.py
    ├── Settings.py
    ├── CustomList.py
    ├── CustomAdd.py
    └── Path.dat
```



- Each .dat files are contained their Paths



 



### 





