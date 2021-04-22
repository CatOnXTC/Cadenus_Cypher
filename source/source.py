from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time, sys, traceback, random, re
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

filePath = ""
txtregex = re.compile("^.*\.txt$")

f = open("info.txt", "r",encoding="utf8")
infoText = f.read()
f = open("help.txt", "r",encoding="utf8")
helpText = f.read()

class Validator(QValidator):
    def validate(self, string, pos):
        special = False
        regex = re.compile("^[a-zA-Z]*$")
        if(regex.match(string)):
            special = True
        if(special):
            return QValidator.Acceptable, string.upper(), pos
        else:
            return QValidator.Invalid, string, pos

class Okno(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(Okno, self).__init__(*args,*kwargs)
        self.setWindowTitle("Cadenus")

        titleText = QLabel()
        titleText.setText("Cadenus")
        titleText.setAlignment(Qt.AlignHCenter)
        titleText.setFont(QFont('times',40))
        titleText.setStyleSheet("QLabel { color : rgb(10,50,60); }")

        emptyText = QLabel()
        emptyText.setText("")
        emptyText.setFont(QFont('times',20))

        authorText = QLabel()
        authorText.setText("Karol Sienkiewicz 140774")
        authorText.setAlignment(Qt.AlignHCenter)
        authorText.setFont(QFont('times',10))
        authorText.setStyleSheet("QLabel { color : rgb(10,50,60); }")

        self.subtitleText = QLabel()
        self.subtitleText.setText("ABCDEFGHIJKLMNOPQRSTUVWXZY")
        self.subtitleText.setAlignment(Qt.AlignCenter)
        self.subtitleText.setFont(QFont('times',16))
        self.subtitleText.setStyleSheet("QLabel { color : rgb(10,50,60); }")

        shuffleButton = QPushButton()
        shuffleButton.setText("Stwórz nową permutację dla drugiego klucza")
        shuffleButton.clicked.connect(self.shuffleClicked)

        self.keyField = QLineEdit()
        self.validator = Validator()
        self.keyField.setValidator(self.validator)
        self.keyField.setPlaceholderText("Pierwszy klucz")

        self.messageField = QTextEdit()
        self.messageField.setPlaceholderText("Tekst nieszyfrowany")

        self.cryptedField = QTextEdit()
        self.cryptedField.setPlaceholderText("Tekst szyfrowany")

        textFieldsLayout = QHBoxLayout()
        textFieldsLayout.addWidget(self.messageField)
        textFieldsLayout.addWidget(self.cryptedField)
        textFieldsLayoutW = QWidget()
        textFieldsLayoutW.setLayout(textFieldsLayout)

        encryptButton = QPushButton()
        encryptButton.setText("Zaszyfruj")
        encryptButton.setStyleSheet("background-color : rgb(240,245,245);")
        encryptButton.clicked.connect(self.encryptClicked)

        decryptButton = QPushButton()
        decryptButton.setText("Odszyfruj")
        decryptButton.setStyleSheet("background-color : rgb(240,245,245);")
        decryptButton.clicked.connect(self.decryptClicked)

        selectButton = QPushButton()
        selectButton.setText("Wybierz plik z tekstem")
        selectButton.setMinimumWidth(150)
        selectButton.clicked.connect(self.selectClicked)

        keyButton = QPushButton()
        keyButton.setText("Wybierz plik z kluczem")
        keyButton.setMinimumWidth(150)
        keyButton.clicked.connect(self.keyClicked)

        selectSaveButton = QPushButton()
        selectSaveButton.setMinimumWidth(150)
        selectSaveButton.setText("Zapisz plik z tekstem")
        selectSaveButton.clicked.connect(self.selectSaveClicked)

        keySaveButton = QPushButton()
        keySaveButton.setMinimumWidth(150)
        keySaveButton.setText("Zapisz plik z kluczem")
        keySaveButton.clicked.connect(self.keySaveClicked)

        selectCipherButton = QPushButton()
        selectCipherButton.setMinimumWidth(150)
        selectCipherButton.setText("Wybierz zaszyfrowany plik")
        selectCipherButton.clicked.connect(self.selectCipherClicked)

        selectCipherSaveButton = QPushButton()
        selectCipherSaveButton.setMinimumWidth(150)
        selectCipherSaveButton.setText("Zapisz zaszyfrowany plik")
        selectCipherSaveButton.clicked.connect(self.selectCipherSaveClicked)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(encryptButton)
        buttonsLayout.addWidget(decryptButton)
        buttonsLayoutW = QWidget()
        buttonsLayoutW.setLayout(buttonsLayout)

        selectLayout = QHBoxLayout()
        selectLayout.addWidget(selectButton)
        selectLayout.addWidget(keyButton)
        selectLayout.addWidget(selectCipherButton)
        selectLayoutW = QWidget()
        selectLayoutW.setLayout(selectLayout)

        selectSaveLayout = QHBoxLayout()
        selectSaveLayout.addWidget(selectSaveButton)
        selectSaveLayout.addWidget(keySaveButton)
        selectSaveLayout.addWidget(selectCipherSaveButton)
        selectSaveLayoutW = QWidget()
        selectSaveLayoutW.setLayout(selectSaveLayout)

        selectFinLayout = QVBoxLayout()
        selectFinLayout.setAlignment(Qt.AlignCenter)
        selectFinLayout.addWidget(selectLayoutW)
        selectFinLayout.addWidget(selectSaveLayoutW)
        selectFinLayoutW = QWidget()
        selectFinLayoutW.setLayout(selectFinLayout)

        self.pathText = QLabel()
        self.pathText.setText("")
        self.pathText.setAlignment(Qt.AlignCenter)
        self.pathText.setFont(QFont('times',10))
        self.pathText.setStyleSheet("QLabel { color : rgb(30,70,80); }")

        infoButton = QPushButton()
        infoButton.setText("Informacje")
        infoButton.clicked.connect(self.infoClicked)

        helpButton = QPushButton()
        helpButton.setText("Pomoc")
        helpButton.clicked.connect(self.helpClicked)

        exampleButton = QPushButton()
        exampleButton.setText("Przykład")
        exampleButton.clicked.connect(self.exampleClicked)

        topLayout = QHBoxLayout()
        topLayout.addWidget(infoButton)
        topLayout.addWidget(exampleButton)
        topLayout.addWidget(helpButton)
        topLayoutW = QWidget()
        topLayoutW.setLayout(topLayout)

        mainMenu = QVBoxLayout()
        mainMenu.addWidget(topLayoutW)
        mainMenu.addWidget(titleText)
        mainMenu.addWidget(emptyText)
        mainMenu.addWidget(self.keyField)
        mainMenu.addWidget(self.subtitleText)
        mainMenu.addWidget(shuffleButton)
        mainMenu.addWidget(emptyText)
        mainMenu.addWidget(textFieldsLayoutW)
        mainMenu.addWidget(buttonsLayoutW)
        mainMenu.addWidget(selectFinLayoutW)
        mainMenu.addWidget(self.pathText)
        mainMenu.addWidget(authorText)

        mainMenuW = QWidget()
        mainMenuW.setLayout(mainMenu)

        self.setCentralWidget(mainMenuW)

    def shuffleClicked(self):
        tempS = self.subtitleText.text()
        self.subtitleText.setText(''.join(random.sample(tempS, len(tempS))))
    
    def mousePressEvent(self, QMouseEvent):
        print("cool")
        if QMouseEvent.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=QMouseEvent.globalPos()-self.pos()
            QMouseEvent.accept()
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
                self.move(QMouseEvent.globalPos()-self.m_Position)
        QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    def encryptClicked(self):
        toEncrypt = self.messageField.toPlainText()
        keyText = self.keyField.text()
        if(toEncrypt == ""):
            message = QMessageBox()
            message.setWindowTitle("Błąd")
            message.setIcon(QMessageBox.Critical)
            message.setText("Podany tekst jest za krótki!")
            message.exec_()
        elif(len(keyText)*26 < len(toEncrypt)):
            message = QMessageBox()
            message.setWindowTitle("Błąd")
            message.setIcon(QMessageBox.Critical)
            message.setText("Podany pierwszy klucz jest za krótki!")
            message.exec_()
        else:
            range1 = len(keyText)
            range2 = len(toEncrypt)//range1
            if(len(toEncrypt)%range1 != 0):
                range2 += 1
            tempM = [[" " for y in range(range2)] for x in range(range1)]
            tempL = [ord(letter) for letter in keyText]

            count1 = 0
            count2 = 0
            for letter in toEncrypt:
                tempM[count1][count2] = letter
                count1 += 1
                if(count1 == range1):
                    count1 = 0
                    count2 += 1

            tempLL = tempL.copy()
            tempMM = tempM.copy()
            for i in range(len(tempL)):
                minIndex = 0
                for j in range(len(tempLL)):
                    if(tempLL[minIndex] > tempLL[j]):
                        minIndex = j
                tempL[i] = tempLL[minIndex]
                tempM[i] = tempMM[minIndex]
                tempLL.pop(minIndex)
                tempMM.pop(minIndex)

            checkL = [ord(letter) for letter in self.subtitleText.text()]
            for x in range(range1):
                for i in range(26):
                    if(checkL[i] == tempL[x]):
                        for y in range(i):
                            tempM[x] = tempM[x][1:]+tempM[x][:1]
                        break

            result = ""
            for y in range(range2):
                for x in range(range1):
                    result += str(tempM[x][y])

            self.cryptedField.setText(result)
            
    def decryptClicked(self):
        toDecrypt = self.cryptedField.toPlainText()
        keyText = self.keyField.text()
        if(toDecrypt == ""):
            message = QMessageBox()
            message.setWindowTitle("Błąd")
            message.setIcon(QMessageBox.Critical)
            message.setText("Podany tekst jest za krótki!")
            message.exec_()
        elif(len(keyText)*26 < len(toDecrypt)):
            message = QMessageBox()
            message.setWindowTitle("Błąd")
            message.setIcon(QMessageBox.Critical)
            message.setText("Podany pierwszy klucz jest za krótki!")
            message.exec_()
        else:
            range1 = len(keyText)
            range2 = len(toDecrypt)//range1
            if(len(toDecrypt)%range1 != 0):
                range2 += 1
            tempM = [[" " for y in range(range2)] for x in range(range1)]
            tempL = [ord(letter) for letter in keyText]

            count1 = 0
            count2 = 0
            for letter in toDecrypt:
                tempM[count1][count2] = letter
                count1 += 1
                if(count1 == range1):
                    count1 = 0
                    count2 += 1

            tempLL = tempL.copy()
            tempLL = sorted(tempLL)
            tempMM = tempM.copy()
            for i in range(len(tempL)):
                for j in range(len(tempLL)):
                    if(tempL[i] == tempLL[j]):
                        tempM[i] = tempMM[j]
                        tempLL.pop(j)
                        tempMM.pop(j)
                        break

            checkL = [ord(letter) for letter in self.subtitleText.text()]
            for x in range(range1):
                for i in range(26):
                    if(checkL[i] == tempL[x]):
                        for y in range(i): 
                            tempM[x] = tempM[x][-1:]+tempM[x][:-1]
                        break

            result = ""
            for y in range(range2):
                for x in range(range1):
                    result += str(tempM[x][y])

            self.messageField.setText(result)

    def selectClicked(self):
        filePath = filedialog.askopenfilename()
        if(txtregex.match(filePath)):
            self.pathText.setText(filePath)
            file = open(filePath,'r',encoding="utf8")
            self.messageField.setText(file.read())
        else:
            filePath = ""
            self.pathText.setText(filePath)
            message = QMessageBox()
            message.setWindowTitle("Błąd")
            message.setIcon(QMessageBox.Critical)
            message.setText("Wybrany plik nie jest w formacie .txt!")
            message.exec_()

    def keyClicked(self):
        filePath = filedialog.askopenfilename()
        if(txtregex.match(filePath)):
            self.pathText.setText(filePath)
            with open(filePath,'r',encoding="utf8") as file:
                temp = file.readline()
                temp = temp[: -1]
                regex = re.compile("^[a-zA-Z]*$")
                if(regex.match(temp)):
                    self.keyField.setText(temp)
                temp = file.readline()
                temp2 = ''.join(sorted(temp))
                tempregex = re.compile("^ABCDEFGHIJKLMNOPQRSTUVWXYZ$")
                if(tempregex.match(temp2)):
                    self.subtitleText.setText(temp)
        else:
            filePath = ""
            self.pathText.setText(filePath)
            message = QMessageBox()
            message.setWindowTitle("Błąd")
            message.setIcon(QMessageBox.Critical)
            message.setText("Wybrany plik nie jest w formacie .txt!")
            message.exec_()

    def selectCipherClicked(self):
        filePath = filedialog.askopenfilename()
        if(txtregex.match(filePath)):
            self.pathText.setText(filePath)
            file = open(filePath,'r',encoding="utf8")
            self.cryptedField.setText(file.read())
        else:
            filePath = ""
            self.pathText.setText(filePath)
            message = QMessageBox()
            message.setWindowTitle("Błąd")
            message.setIcon(QMessageBox.Critical)
            message.setText("Wybrany plik nie jest w formacie .txt!")
            message.exec_()

    def keySaveClicked(self):
        filePath = filedialog.asksaveasfilename(filetypes=[("Plik tekstowy","*.txt")], defaultextension = "*.txt")
        if filePath:
            with open(filePath, "w", -1, "utf-8") as file:
                file.write(self.keyField.text() + "\n" + self.subtitleText.text())

    def selectSaveClicked(self):
        filePath = filedialog.asksaveasfilename(filetypes=[("Plik tekstowy","*.txt")], defaultextension = "*.txt")
        if filePath:
            with open(filePath, "w", -1, "utf-8") as file:
                file.write(self.messageField.toPlainText())

    def selectCipherSaveClicked(self):
        filePath = filedialog.asksaveasfilename(filetypes=[("Plik tekstowy","*.txt")], defaultextension = "*.txt")
        if filePath:
            with open(filePath, "w", -1, "utf-8") as file:
                file.write(self.cryptedField.toPlainText())

    def infoClicked(self):
        QMessageBox.about(self, "Informacje", infoText)

    def exampleClicked(self):
        example = QMessageBox()
        example.setWindowTitle("Przykład")
        example.setIconPixmap(QPixmap("example.png"))
        example.exec_()

    def helpClicked(self):
        QMessageBox.about(self, "Pomoc", helpText)

# MAIN
app = QApplication(sys.argv)

window = Okno()
window.setStyleSheet("background-color: rgb(230,235,235);")
window.show()

app.exec_()