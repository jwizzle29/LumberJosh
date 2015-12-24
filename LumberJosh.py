#!/usr/bi/env python
from PyQt4 import QtCore, QtGui
import sys
import atexit
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
    
class myTableModel(QtCore.QAbstractTableModel):
    header_labels = ['Length(ft)', 'Diameter(in)', 'Cuft(ft^3)']
    def __init__(self,calculations = [[]], parent = None):
        QtCore.QAbstractTableModel.__init__(self,parent)
        self.__calculations = calculations
        self.count = 1
    def rowCount(self,parent):
        return len(self.__calculations) 

    def columnCount(self,parent):
        try:
            l = len(self.__calculations[0])
        except:
            l = 0
        return l
    

   # def flags(self,index):
     #   return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
    #def setData(self,index,value,role = QtCore.Qt.EditRole):
     #   if role ==QtCore.Qt.EditRole:
     #       row = index.row()
     #       col = index.column()
     #       new = value
            #if row.isValid():
     #       self.__calculations[row][col] = value
      #      x = self.dataChanged.emit(index,index)
       #     return True
            
        #return False

    def data(self,index,role):

        if role == QtCore.Qt.EditRole:
            row = index.row()
            col = index.column()
            value = self.__calculations[row][col]
            return value
        if role == QtCore.Qt.DisplayRole: 
            row = index.row()
            col = index.column()
            value = self.__calculations[row][col]
            return value
       
    def headerData(self,section,orientation,role):
        if role == QtCore.Qt.DisplayRole:
            
            if orientation == QtCore.Qt.Horizontal:
                return self.header_labels[section]
            else:
                return QtCore.QString("#%1").arg(section + 1)
class One:

    def calcCubicFt(self,lengthInFeet,DiameterInInches):
        pi = 3.14
        conversion = 1728
        self.lengthInFeet = float(lengthInFeet)
        self.DiameterInInches = float(DiameterInInches)
        lengthToInches = self.lengthInFeet*12
        Radius = float(self.DiameterInInches / 2)
        RSquared = Radius*Radius
        AreaOfSect = RSquared*pi
        CubicFeet = (AreaOfSect*lengthToInches) / conversion
        
        return CubicFeet




class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.count = 0
        self.tabledata = []
        self.totalFtInDeck = 0
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(392, 560)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 371, 511))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tableView = QtGui.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 351, 401))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableView.setFont(font)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 480, 131, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 450, 61, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 450, 61, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 430, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(80, 430, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lcdNumber = QtGui.QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 450, 101, 51))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(180, 430, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 450, 71, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(100, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nyala"))
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        palette = self.lcdNumber.palette()
        palette.setColor(palette.Light, QtGui.QColor(255, 0, 0))
        self.lcdNumber.setPalette(palette)
        self.setTabOrder(self.lineEdit,self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2,self.pushButton)
        self.pushButton.setAutoDefault(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "LumberJosh", None))
        self.groupBox.setTitle(_translate("Form", "Current deck", None))
        self.tableView.setToolTip(_translate("Form", "Current log display", None))
        self.pushButton.setText(_translate("Form", "Measure log", None))
        self.lineEdit.setToolTip(_translate("Form", "length in ft/inches", None))
        self.lineEdit_2.setToolTip(_translate("Form", "diameter in inches", None))
        self.label.setText(_translate("Form", "Len:", None))
        self.label_2.setText(_translate("Form", "Dia:", None))
        self.lcdNumber.setToolTip(_translate("Form", "Total cuft in deck", None))
        self.label_3.setText(_translate("Form", "cuft:", None))
        self.pushButton_3.setToolTip(_translate("Form", "Create new deck", None))
        self.pushButton_3.setText(_translate("Form", "New Deck", None))
        self.label_7.setText(_translate("Form", "The LumberJosh", None))
        self.pushButton.clicked.connect(self.getCUFT)
        self.pushButton_3.clicked.connect(self.reset)
    def getLength(self):
        LEN = self.lineEdit.text()
        return LEN

    def getDia(self):
        DIA = self.lineEdit_2.text()
        return DIA
    
    def getCUFT(self):
        self.count = self.count + 1
        Cuft = float(One().calcCubicFt(self.getLength(),self.getDia()))
        self.totalFtInDeck = self.totalFtInDeck + Cuft

        k = [self.getLength(),self.getDia(),Cuft]
        self.tabledata.append(k)
        model = myTableModel(self.tabledata)
        self.tableView.setModel(model)
        self.tableView.show()
        self.lcdNumber.display(self.totalFtInDeck)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit.setFocus()
        self.setTabOrder(self.lineEdit,self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2,self.pushButton)
    def reset(self):
        self.tabledata = []
        model = myTableModel(self.tabledata)
        self.tableView.setModel(model)
        self.totalFtInDeck = 0
        self.lcdNumber.display(self.totalFtInDeck)
        ex = Ui_Form()
        ex.show()  
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle("First")
    ex = Ui_Form()
    ex.show()   
    sys.exit(app.exec_())

