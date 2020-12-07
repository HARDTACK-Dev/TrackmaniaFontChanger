

![](https://img.shields.io/badge/Game-Trackmania-lightgrey) ![](https://img.shields.io/badge/Version-2.0-orange) ![](https://img.shields.io/badge/License-GPL-blue)

## <pre>Trackmania Fonter  (v2.0) </pre>



###### 															  A Program that can change displayed fonts on TrackMania United <img src="https://cdn.discordapp.com/attachments/465451394032336896/785418360706957322/TMUF.png" width=18/> / Nations<img src="https://cdn.discordapp.com/attachments/465451394032336896/785418359763238922/TMNF.jpeg" width=16/>

​																			        									
​                                                                                                                                 
![image-20201207123801321](https://cdn.discordapp.com/attachments/465451394032336896/785416925181640714/Preview.png)

 



[View Changlog]( Readme.md "Changelog")

<br><br><br>

### What can I change?

---

- Clock on menu bar
- Scoreboard on Ladder
- Speed meter
- In-game Timer


<br><br><br>



### Dependencies 

---

Program Written in <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" alt="파일:Python-logo-notext.svg - 위키백과, 우리 모두의 백과사전" width=30 />Python3,  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Qt_logo_2016.svg/1024px-Qt_logo_2016.svg.png" alt="파일:Qt logo 2016.svg - 위키백과, 우리 모두의 백과사전"  width=30 />Pyqt5, *You can also see all source code on GitHub repo*



<br><br><br>

#### How It's Work

----

The working principle of this program is to transfer the custom font file to the TrackMania installation folder 

 ```python
 \GameData\Interface\media\fonds\RedTexture\Led_00.dds
 ```

It replacing the `Led_00.dds` file to Customized Font file, So that game read.

So if you want to restore, just backup Default dds file or Copy it From `Fonts\Original\Default`  :)




<br><br><br>

### Changelog 

---

### [ v2.0 ](https://github.com/HARDTACK-Dev/TrackmaniaFontChanger/releases/tag/v2.0)  - 2020-12-07

### Added

- **Remade with Python3 / PyQt5**
- UI/UX Redesigned
- Support Add Custom .DDS(font) file
- **`17`** Font Added 



<br><br>

----



#### [ v1.0 ](https://github.com/HARDTACK-Dev/TrackmaniaFontChanger/releases/tag/v1.0)  - 2020-04-13

#### Added

- First Release

- Written with AHK Script
- **`17`** Font Added 



<br><br><br>



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





