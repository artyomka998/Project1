# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication

# Form, Window = uic.loadUiType("lab5.ui")

# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec_()
import sqlite3
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
import design  # Это наш конвертированный файл дизайна

conn=sqlite3.connect("basadannih.db")
cursor=conn.cursor()

class window_design(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.knopka1.clicked.connect(self.add)
        self.knopka2.clicked.connect(self.exit)
        self.table = self.tableWidget
        self.print_rows()
        
    
    def print_rows(self): #Вывод строк из бд в таблицу 
        
        labels = ["Название", "Окна", "Время", "Работы", "Товары", "Выработка"]
        number_labels = len(labels)
        self.table.setColumnCount(number_labels)
        self.table.setHorizontalHeaderLabels(labels)
    
        sql = "SELECT * FROM Predpriyatie"
        cursor.execute(sql)
        rows = cursor.fetchall()
        number_rows = len(rows)
        self.table.setRowCount(number_rows)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))   #item - ячейка со значением
                self.table.setItem(i, j, item)      #устанавливаем значение ячейки
        self.table.resizeColumnsToContents()        


    def virab(self, rb, vr):
        return rb // vr

    def add(self):
        name = self.textEdit
        okna = self.textEdit_2
        vremya = self.textEdit_3
        raboti = self.textEdit_4
        tovari = self.textEdit_5
        virabotka = self.virab(rb=int(raboti.toPlainText()), vr=int(vremya.toPlainText()))


        values = (name.toPlainText(),
                  int(okna.toPlainText()),
                  int(vremya.toPlainText()),
                  int(raboti.toPlainText()),
                  int(tovari.toPlainText()),
                  virabotka)

        cursor.executemany("INSERT INTO Predpriyatie VALUES (?,?,?,?,?,?)", [values]) #добавление значений в БД
        conn.commit()

        self.print_rows()

    def exit(self):
        QtCore.QCoreApplication.instance().quit()       #закрытие
    

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    win = window_design() # Создаём объект класса ExampleApp
    win.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()