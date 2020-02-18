from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MicrobialAnalysis(object):
    def setupUi(self, MicrobialAnalysis):

        MicrobialAnalysis.setObjectName("MicrobialAnalysis")
        MicrobialAnalysis.resize(742, 617)
        MicrobialAnalysis.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(MicrobialAnalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.controls = QtWidgets.QGroupBox(self.centralwidget)
        self.controls.setGeometry(QtCore.QRect(10, 8, 241, 514))

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.controls.setFont(font)
        self.controls.setObjectName("controls")

        self.buttonsWidget = QtWidgets.QWidget(self.controls)
        self.buttonsWidget.setGeometry(QtCore.QRect(10, 180, 221, 321))
        self.buttonsWidget.setObjectName("buttonsWidget")

        self.resetButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.resetButton.setGeometry(QtCore.QRect(0, 220, 221, 81))
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")

        self.stopButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.stopButton.setGeometry(QtCore.QRect(0, 120, 221, 75))
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")

        self.startButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.startButton.setGeometry(QtCore.QRect(0, 20, 221, 75))
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")

        self.numberOfSamples = QtWidgets.QSpinBox(self.controls)
        self.numberOfSamples.setGeometry(QtCore.QRect(140, 50, 81, 31))
        self.numberOfSamples.setMaximum(999)
        self.numberOfSamples.setObjectName("numberOfSamples")

        self.spinBoxLabel = QtWidgets.QLabel(self.controls)
        self.spinBoxLabel.setGeometry(QtCore.QRect(10, 30, 121, 64))
        self.spinBoxLabel.setWordWrap(True)
        self.spinBoxLabel.setObjectName("spinBoxLabel")

        self.threshold = QtWidgets.QSpinBox(self.controls)
        self.threshold.setGeometry(QtCore.QRect(140, 110, 81, 31))
        self.threshold.setMaximum(999)
        self.threshold.setObjectName("threshold")

        self.thresholdLabel = QtWidgets.QLabel(self.controls)
        self.thresholdLabel.setGeometry(QtCore.QRect(10, 100, 121, 61))
        self.thresholdLabel.setWordWrap(True)
        self.thresholdLabel.setObjectName("thresholdLabel")

        self.resultsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.resultsGroupBox.setGeometry(QtCore.QRect(260, 8, 471, 234))
        self.resultsGroupBox.setFont(font)
        self.resultsGroupBox.setObjectName("resultsGroupBox")

        self.sampleNumber = QtWidgets.QLabel(self.resultsGroupBox)
        self.sampleNumber.setGeometry(QtCore.QRect(210, 80, 231, 41))
        self.sampleNumber.setFont(font)
        self.sampleNumber.setAutoFillBackground(False)
        self.sampleNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.sampleNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.sampleNumber.setObjectName("sampleNumber")

        self.clientName = QtWidgets.QLabel(self.resultsGroupBox)
        self.clientName.setGeometry(QtCore.QRect(210, 30, 231, 41))  
        self.clientName.setFont(font)
        self.clientName.setAutoFillBackground(False)
        self.clientName.setFrameShape(QtWidgets.QFrame.Box)
        self.clientName.setScaledContents(False)
        self.clientName.setAlignment(QtCore.Qt.AlignCenter)
        self.clientName.setObjectName("clientName")

        self.passFail = QtWidgets.QLabel(self.resultsGroupBox)
        self.passFail.setGeometry(QtCore.QRect(210, 130, 231, 41))
        self.passFail.setFont(font)
        self.passFail.setAutoFillBackground(False)
        self.passFail.setFrameShape(QtWidgets.QFrame.Box)
        self.passFail.setAlignment(QtCore.Qt.AlignCenter)
        self.passFail.setObjectName("passFail")

        self.colonyCount = QtWidgets.QLabel(self.resultsGroupBox)
        self.colonyCount.setGeometry(QtCore.QRect(210, 180, 231, 41))
        self.colonyCount.setFont(font)
        self.colonyCount.setAutoFillBackground(False)
        self.colonyCount.setFrameShape(QtWidgets.QFrame.Box)
        self.colonyCount.setAlignment(QtCore.Qt.AlignCenter)
        self.colonyCount.setObjectName("colonyCount")

        self.clientLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.clientLabel.setGeometry(QtCore.QRect(30, 30, 171, 41))
        self.clientLabel.setObjectName("clientLabel")

        self.sampleNumLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.sampleNumLabel.setGeometry(QtCore.QRect(30, 80, 171, 41))
        self.sampleNumLabel.setObjectName("sampleNumLabel")

        self.passFailLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.passFailLabel.setGeometry(QtCore.QRect(30, 130, 171, 41))
        self.passFailLabel.setObjectName("passFailLabel")

        self.colonycountLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.colonycountLabel.setGeometry(QtCore.QRect(30, 180, 171, 41))
        self.colonycountLabel.setObjectName("colonycountLabel")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 530, 711, 41))
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        progress_max = self.numberOfSamples.value()
        self.progressBar.setMaximum(progress_max)

        self.Image = QtWidgets.QGroupBox(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(260, 250, 471, 272))
        self.Image.setFont(font)
        self.Image.setTitle("")
        self.Image.setObjectName("Image")

        self.sampleImage = QtWidgets.QLabel(self.Image)
        self.sampleImage.setGeometry(QtCore.QRect(10, 10, 451, 251))
        self.sampleImage.setFrameShape(QtWidgets.QFrame.Box)
        self.sampleImage.setText("")
        self.sampleImage.setPixmap(QtGui.QPixmap("test.png"))
        self.sampleImage.setScaledContents(True)
        self.sampleImage.setObjectName("sampleImage")

        MicrobialAnalysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MicrobialAnalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 25))
        self.menubar.setObjectName("menubar")
        MicrobialAnalysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MicrobialAnalysis)
        self.statusbar.setObjectName("statusbar")
        MicrobialAnalysis.setStatusBar(self.statusbar)
        self.retranslateUi(MicrobialAnalysis)
        QtCore.QMetaObject.connectSlotsByName(MicrobialAnalysis)

        self.startButton.clicked.connect(self.start_clicked)
        self.stopButton.clicked.connect(self.stop_clicked) 
        self.resetButton.clicked.connect(self.reset_clicked)
        

    def start_clicked(self):
        thresh_val = self.threshold.value()
        num_samp = self.numberOfSamples.value()
        num_col = self.colonyCount.text()
        cli_name = self.clientName.text()
        test_res = self.passFail.text()

        print ("Start command sent.")
        print ("Threshold: " + str(thresh_val))
        print ("Number of Samples: " + str(num_samp))
        print ("Client Name: " + cli_name)
        print ("Microbial Count: " + str(num_col))
        print ("Pass/Fail Result: " + test_res)

    def stop_clicked(self):
        print ("Stop command sent") 

    def reset_clicked(self):
        print ("Reset command sent")

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + ((maxVal) - curVal) / 100)

    def update_progess_bar(self):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)     

    def retranslateUi(self, MicrobialAnalysis):
        _translate = QtCore.QCoreApplication.translate
        MicrobialAnalysis.setWindowTitle(_translate("MicrobialAnalysis", "Microbial Analysis Tool"))
        self.controls.setTitle(_translate("MicrobialAnalysis", "Controls"))
        self.resetButton.setText(_translate("MicrobialAnalysis", "Reset"))
        self.stopButton.setText(_translate("MicrobialAnalysis", "Stop"))
        self.startButton.setText(_translate("MicrobialAnalysis", "Start"))
        self.spinBoxLabel.setText(_translate("MicrobialAnalysis", "Number of samples"))
        self.thresholdLabel.setText(_translate("MicrobialAnalysis", "Test Threshold"))
        self.resultsGroupBox.setTitle(_translate("MicrobialAnalysis", "Results"))
        self.sampleNumber.setText(_translate("MicrobialAnalysis", "#10011001"))
        self.clientName.setText(_translate("MicrobialAnalysis", "BeerMakers Inc."))
        self.passFail.setText(_translate("MicrobialAnalysis", "Pass"))
        self.colonyCount.setText(_translate("MicrobialAnalysis", "5"))
        self.clientLabel.setText(_translate("MicrobialAnalysis", "Client Name"))
        self.sampleNumLabel.setText(_translate("MicrobialAnalysis", "Sample Number"))
        self.passFailLabel.setText(_translate("MicrobialAnalysis", "Pass/Fail"))
        self.colonycountLabel.setText(_translate("MicrobialAnalysis", "Colony Count"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MicrobialAnalysis = QtWidgets.QMainWindow()
    ui = Ui_MicrobialAnalysis()
    ui.setupUi(MicrobialAnalysis)
    MicrobialAnalysis.show()
    sys.exit(app.exec_())
