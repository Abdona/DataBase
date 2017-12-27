from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_DataBase(object):
    def setupUi(self, DataBase):
        DataBase.setObjectName("DataBase")
        DataBase.resize(498, 479)
        self.centralwidget = QtWidgets.QWidget(DataBase)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.Connect = QtWidgets.QPushButton(self.centralwidget)
        self.Connect.setObjectName("Connect")
        self.gridLayout.addWidget(self.Connect, 0, 2, 1, 1)
        self.QueryType = QtWidgets.QComboBox(self.centralwidget)
        self.QueryType.setObjectName("QueryType")
        self.QueryType.addItem("")
        self.QueryType.addItem("")
        self.QueryType.addItem("")
        self.QueryType.addItem("")
        self.gridLayout.addWidget(self.QueryType, 1, 2, 1, 1)
        self.InsCond = QtWidgets.QPushButton(self.centralwidget)
        self.InsCond.setObjectName("InsCond")
        self.gridLayout.addWidget(self.InsCond, 1, 0, 1, 1)
        self.query_table = QtWidgets.QTableWidget(self.centralwidget)
        self.query_table.setObjectName("query_table")
        self.query_table.setColumnCount(3)
        self.query_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.query_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.query_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.query_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.query_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.query_table, 6, 0, 1, 3)
        self.Tables = QtWidgets.QComboBox(self.centralwidget)
        self.Tables.setObjectName("Tables")
        self.Tables.addItem("")
        self.Tables.addItem("")
        self.Tables.addItem("")
        self.Tables.addItem("")
        self.Tables.addItem("")
        self.Tables.addItem("")
        self.gridLayout.addWidget(self.Tables, 2, 2, 1, 1)
        DataBase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataBase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 21))
        self.menubar.setObjectName("menubar")
        self.menuStart = QtWidgets.QMenu(self.menubar)
        self.menuStart.setObjectName("menuStart")
        DataBase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataBase)
        self.statusbar.setObjectName("statusbar")
        DataBase.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(DataBase)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(DataBase)
        self.actionClose.setObjectName("actionClose")
        self.menuStart.addAction(self.actionOpen)
        self.menuStart.addAction(self.actionClose)
        self.menubar.addAction(self.menuStart.menuAction())
        ##########################
        self.Connect.clicked.connect(self.connectto)
        self.Tables.activated.connect(self.TablesT)
        self.QueryType.activated.connect(self.query_type)

        ##########################

        self.retranslateUi(DataBase)
        QtCore.QMetaObject.connectSlotsByName(DataBase)

    def retranslateUi(self, DataBase):
        _translate = QtCore.QCoreApplication.translate
        DataBase.setWindowTitle(_translate("DataBase", "DataBase"))
        self.Connect.setText(_translate("DataBase", "College"))
        self.QueryType.setItemText(0, _translate("DataBase", "Insert"))
        self.QueryType.setItemText(1, _translate("DataBase", "Delete"))
        self.QueryType.setItemText(2, _translate("DataBase", "Update"))
        self.QueryType.setItemText(3, _translate("DataBase", "Query"))
        self.InsCond.setText(_translate("DataBase", "Update/Delete/Insert/Qeuery"))
        #item = self.query_table.verticalHeaderItem(0)
        #item.setText(_translate("DataBase", "New Row"))
        #item = self.query_table.horizontalHeaderItem(0)
        #item.setText(_translate("DataBase", "New Column"))
        self.Tables.setItemText(0, _translate("DataBase", "Student"))
        self.Tables.setItemText(1, _translate("DataBase", "Course"))
        self.Tables.setItemText(2, _translate("DataBase", "Books"))
        self.Tables.setItemText(3, _translate("DataBase", "Borrows"))
        self.Tables.setItemText(4, _translate("DataBase", "Enrolls"))
        self.Tables.setItemText(5, _translate("DataBase", "Professor"))
        self.menuStart.setTitle(_translate("DataBase", "Start"))
        self.actionOpen.setText(_translate("DataBase", "Open"))
        self.actionClose.setText(_translate("DataBase", "Exit"))
    def connectto(self):
        self.valueofinsert=[]
        self.clear()
        print("connect")
        self.conn=sqlite3.connect("College.db")
        self.c=self.conn.cursor()
    def TablesT(self):
        self.clear()
        self.tablename=self.Tables.currentText()
    def query_type(self):
        #print("qeury")
        #c=conn.cursor()
        self.b='select'+''+'*'+''+'from'+" "+self.tablename
        self.qeuery=self.c.execute(self.b)
        self.temp=self.qeuery
        self.num_attr = len(self.c.description)
        self.attr_names = [i[0] for i in self.c.description]
        if(self.QueryType.currentText()=='Insert'):
            self.clear()
            self.create_table(self.attr_names,self.qeuery)
            try:
                self.InsCond.clicked.connect(self.insert)
            except:
                pass
        if(self.QueryType.currentText()=='Delete'):
            self.clear()
            self.create_table(self.attr_names,self.qeuery)
            self.InsCond.clicked.connect(self.delete)
            #self.query_table.itemSelectionChanged.connect(self.selected_change)
            #self.query_table.removeRow(self,self.index)
        #elif(self.QueryType.currentText()=='Update'):
            
        elif(self.QueryType.currentText()=='Query'):
            self.clear()
            self.create_table(self.attr_names,self.qeuery)
            self.InsCond.clicked.connect(self.query)            
    def create_table (self,list1,qeuery):
        print("create table")
        m=len(list1)
        self.query_table.horizontalHeader().setVisible(True)
        #self.query_table.setRowCount(3)
            #self.query_table.insertColumn(i)
            #self.query_table.insertRow(i)
        #self.query_table.setColumnCount(len(list1))
        for i in range(len(list1)):
            print(list1[i])
            #colPosition = self.query_table.columnCount()
            #self.query_table.insertcolumn(colPosition)
            #item = query_tableItem()
            item = self.query_table.horizontalHeaderItem(i)
            item.setText((list1[i]))
        for i in qeuery:
            #print(qeuery)
            #list=qeuery.fetchone()
            rowPosition = self.query_table.rowCount()
            self.query_table.insertRow(rowPosition)
            for j in range(len(i)):
                try:
                    self.query_table.setItem(rowPosition, j,QtWidgets.QTableWidgetItem(str(i[j])))
                except:
                    pass
    def clear(self):
        self.query_table.setRowCount(0)
    def selected_change(self):
        #query_table.currentItem().row()
        self.index = self.query_table.currentRow()
    def insert(self):
        self.rowPosition = self.query_table.rowCount()
        print(self.rowPosition+1)
        self.query_table.insertRow(self.rowPosition)
        self.query_table.cellChanged.connect(self.onClick)
        self.query_table.cellClicked.connect(self.cell_was_clicked)
    def delete(self):
        self.index = self.query_table.currentRow()
        print(self.tablename)
        self.d=self.query_table.item(self.index,0).text()
        print(self.d)
        self.query_table.removeRow(self.index)
        self.delete='Delete'+' '+'from'+" "+self.tablename+" "+"where"+" "+str(self.attr_names[0]) +"=?" ##code=2222
        self.c.execute(self.delete,(self.d,))
        self.conn.commit()
        #self.c.close()
    def query(self):
        self.qeueryin=self.lineEdit.text()
        if(self.qeueryin==""):
            self.clear()
            self.b='select'+''+'*'+''+'from'+" "+self.tablename
            self.qeuery=self.c.execute(self.b)
            self.create_table(self.attr_names,self.qeuery)
        #print(self.qeueryin,self.tablename,self.attr_names)
        else:
            print("mlyan")
            for i in range(len(self.attr_names)):
                self.count='select count(*) from'+' '+self.tablename+' '+'where'+' '+str(self.attr_names[i])+"=?"
                self.qeueryy='select * from' +' '+self.tablename+' '+'where'+' '+str(self.attr_names[i])+"=?"
                self.count=self.c.execute(self.count,(self.qeueryin,))
                #print(self.count.fetchone()[0])
                print(self.attr_names[i])
                if (self.count.fetchone()[0])>0:
                    self.queryout=self.c.execute(self.qeueryy,(self.qeueryin,))
                    self.clear()
                    break
            try:
                self.create_table(self.attr_names,self.queryout)
            except:
                pass
 
    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.query_table.itemAt(row, column)
        self.ID = item.text()
    def onClick(self,row,column):
        #print('Insert')
        try:
            self.valueofinsert.append(str(self.query_table.item(self.rowPosition,column).text()))
            print(self.valueofinsert,self.attr_names)
            if (len(self.valueofinsert)==len(self.attr_names)):
                print(self.tablename)
                self.insertt='insert'+' '+'into'+' '+self.tablename+' '+'values'+'('+",".join(self.valueofinsert)+')'
                #print(self.insertt)
                #self.c.execute('insert into Student values (?,?)', ('1010','Sameh'))
                try:
                    self.c.execute('insert into Student values (?,?)', ('112010','Sameaaah'))
                    #self.c.execute(self.insertt)
                    #self.c.execute("insert into " + self.tablename + " values (" + ('?,' * len(self.valueofinsert))[:-1] + ")", self.valueofinsert)
                except:
                    print("Error")
                print("c.fetchall()")
                self.conn.commit()
        except:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataBase = QtWidgets.QMainWindow()
    ui = Ui_DataBase()
    ui.setupUi(DataBase)
    DataBase.show()
    sys.exit(app.exec_())

