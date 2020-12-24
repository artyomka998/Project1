import sqlite3
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
import design1  # Это наш конвертированный файл дизайна

conn=sqlite3.connect("basadannih1.db")
cursor=conn.cursor()

class window_design(QtWidgets.QMainWindow, design1.Ui_mainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.delete_row)
        self.pushButton_3.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.change_row)
        self.pushButton_4.clicked.connect(self.exit)
        self.pushButton_5.clicked.connect(self.print_rows_filter)
        self.table = self.tableWidget
        self.list_columns = self.listWidget
        self.list_sorts = self.listWidget_2
        self.table.cellClicked.connect(self.get_id_row)
        self.print_rows()
        self.current_id = 0
        
    def get_id_row(self, number_row, number_column):
        name = self.textEdit_4
        date = self.dateEdit
        srok = self.textEdit_2
        comment = self.textEdit

        date_list = self.table.item(number_row, 2).text().split('-')
        date_obj = QtCore.QDate(int(date_list[0]),int(date_list[1]),int(date_list[2]))
        name.setText(self.table.item(number_row, 1).text())
        date.setDate(date_obj)
        srok.setText(self.table.item(number_row, 3).text())
        comment.setText(self.table.item(number_row, 4).text())
        self.current_id = self.table.item(number_row, 0).text()
    
    def change_row(self):
        name = self.textEdit_4
        date = self.dateEdit.date()
        srok = self.textEdit_2
        comment = self.textEdit

        values = (name.toPlainText(),
                  date.toPyDate(),
                  int(srok.toPlainText()),
                  comment.toPlainText(),
                  self.current_id)

        sqlupdate="""
        UPDATE Raboti
        SET name = ?, date = ?, srok = ?, comment = ? 
        WHERE ID = ?
        """
        cursor.execute(sqlupdate,values)
        conn.commit()

        self.print_rows()
    
    def delete_row(self):

        values = (self.current_id)
        
        sqldelete="""
        DELETE FROM Raboti
        WHERE ID = ?
        """
        cursor.execute(sqldelete,values)
        conn.commit()

        self.print_rows()

    def print_rows_filter(self):
        labels = ["ID", "Название", "Дата", "Срок", "Комментарий"]
        number_labels = len(labels)
        self.table.setColumnCount(number_labels)
        self.table.setHorizontalHeaderLabels(labels)

        columns = {
            'Название':'name',
            'Дата начала':'date',
            'Срок выполнения':'srok'
        }
        sorts = {
            'По убыванию':False,
            'По возрастанию':True,
        }
        item_column = self.list_columns.currentItem().text()
        item_sort = self.list_sorts.currentItem().text()
        column = columns[item_column]
        sort = sorts[item_sort]

        sql = f"SELECT * FROM Raboti ORDER BY {column} " if sort else f"SELECT * FROM Raboti ORDER BY {column} DESC"
        

        cursor.execute(sql)
        rows = cursor.fetchall()
        number_rows = len(rows)
        self.table.setRowCount(number_rows)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))   #item - ячейка со значением
                self.table.setItem(i, j, item)      #устанавливаем значение ячейки
        self.table.resizeColumnsToContents()        


    def print_rows(self): #Вывод строк из бд в таблицу 
        
        labels = ["ID", "Название", "Дата", "Срок", "Комментарий"]
        number_labels = len(labels)
        self.table.setColumnCount(number_labels)
        self.table.setHorizontalHeaderLabels(labels)
    
        sql = "SELECT * FROM Raboti"
        cursor.execute(sql)
        rows = cursor.fetchall()
        number_rows = len(rows)
        self.table.setRowCount(number_rows)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))   #item - ячейка со значением
                self.table.setItem(i, j, item)      #устанавливаем значение ячейки
        self.table.setColumnHidden(0,True)
        self.table.resizeColumnsToContents()        

    def add(self):
        name = self.textEdit_4
        date = self.dateEdit.date()
        srok = self.textEdit_2
        comment = self.textEdit

        values = (name.toPlainText(),
                  date.toPyDate(),
                  int(srok.toPlainText()),
                  comment.toPlainText())

        cursor.executemany("INSERT INTO Raboti (name,date,srok,comment) VALUES (?,?,?,?)", [values]) #добавление значений в БД
        conn.commit()

        self.print_rows()

    def exit(self):
        QtCore.QCoreApplication.instance().quit()       #закрытие

def main():
    # cursor.execute(
    #     """CREATE TABLE Raboti (id integer PRIMARY KEY, name text, date text, srok integer, comment text) """
    #     )
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    win = window_design() # Создаём объект класса ExampleApp
    win.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()