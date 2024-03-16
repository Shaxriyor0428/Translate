from PyQt5.QtWidgets import QLabel,QApplication,QPushButton,QLineEdit,QRadioButton,QWidget,QCompleter
from json import load,dump
from uuid import uuid4
class GetUserInfo():
    def __init__(self) :
        with open("fayl.json","r") as f:
            self.data = load(f)

    def getUserEN(self):
        En = [item["en"] for item in self.data]
        if En:
            return En
        else:
            return 

    def getUserUZ(self):
  
        Uz = [item["uz"] for item in self.data]
        if Uz:
            return Uz
        else:
            return 

class Main( QWidget ):
    flag = True
    find = True
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,550)
        self.setWindowTitle("Translate")
        self.radBtn1 = QRadioButton("Search",self)
        self.radBtn1.setStyleSheet("font-size:25px")
        self.radBtn1.move(100,80)
        self.radBtn1.setChecked(True)
        self.radBtn1.clicked.connect(self.SaveSearch)


        self.radBtn2 = QRadioButton("Save",self)
        self.radBtn2.setStyleSheet("font-size:25px")
        self.radBtn2.move(450,80)
        self.radBtn2.clicked.connect(self.SaveSearch)

        self.lbl1 = QLabel("EN",self) 
        self.lbl1.setStyleSheet("font-size:20px")
        self.lbl1.move(40,160)

        obj = GetUserInfo()
        self.qcom1 = QCompleter(obj.getUserEN())
        self.qcom2 = QCompleter(obj.getUserUZ())
        self.lini1 = QLineEdit(self)
        self.lini1.setCompleter(self.qcom1)
        self.lini1.setStyleSheet("font-size:18px")
        self.lini1.move(70,160)

        self.lbl2 = QLabel("UZ",self)
        self.lbl2.setStyleSheet("font-size:20px")
        self.lbl2.move(370,160)

        self.lini2 = QLineEdit(self)
        self.lini2.setStyleSheet("font-size:18px")
        self.lini2.setCompleter(self.qcom2)
        self.lini2.move(400,160)

        self.perevodBtn = QPushButton("<-->",self)
        self.perevodBtn.setStyleSheet("font-size:20px;background-color:green")
        self.perevodBtn.move(275,160)
        self.perevodBtn.clicked.connect(self.Postion)

        self.BtnSaveSerach = QPushButton("Search",self)
        self.BtnSaveSerach.setStyleSheet("font-size:20px;background-color:Violet")
        self.BtnSaveSerach.move(275,250)
        self.BtnSaveSerach.clicked.connect(self.saqlaymiz)
        self.BtnSaveSerach.clicked.connect(self.SaveSaqlaymiz)
    

    def SaveSaqlaymiz(self):
        data = self.JsonFiliRead()
        if self.radBtn1.isChecked():
            for item in data:
                if item["en"] == self.lini1.text():
                    self.lini2.setText(item["uz"])
                elif item["uz"] == self.lini2.text():
                    self.lini1.setText(item["en"])
                else:
                    pass
        with open("fayl.json", "w") as f:
            dump(data, f, indent=4)

    def saqlaymiz(self):
        if self.radBtn2.isChecked():
            self.AddfileJson()
        else:
            pass

    def AddfileJson(self):
        tarjimon = self.JsonFiliRead()
        dct = {}
        dct["en"] = self.lini1.text()
        dct["uz"] = self.lini2.text()
        dct["id"] = str(uuid4())
        exsits = False
        for item in tarjimon:
            if item["en"] == dct["en"] or item["uz"] == dct["uz"]:
                exsits = True
                break
        if not exsits:
            tarjimon.append(dct)
            with open("fayl.json","w") as f:
                    dump(tarjimon,f,indent=4)

    def JsonFiliRead(self):
        with open("fayl.json","r") as f:
            data = load(f)
            if data:
                return data
            else:
                return []
        
    def SaveSearch(self):
        if self.radBtn1.isChecked():
            self.BtnSaveSerach.setText("Search")
        else:
            self.BtnSaveSerach.setText("Save")

            
    def Postion(self):
        if self.flag:
            self.lbl1.move(370,160)
            self.lini1.move(400,160)
            self.lini2.move(70,160)
            self.lbl2.move(40,160)
            self.flag = False
        else:
            self.lbl1.move(40,160)
            self.lbl2.move(370,160)
            self.lini1.move(70,160)
            self.lini2.move(400,160)
            self.flag = True


app = QApplication([])
oyna = Main()
oyna.show()
app.exec()
