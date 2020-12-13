import csv
import sqlite3

conn=sqlite3.connect("basadannih.db")
cursor=conn.cursor()

class work:
    def __init__(self, okna, vremya, raboti, tovari):
        self.ok = okna
        self.vr = vremya
        self.rb = raboti
        self.tv = tovari
        self.data_csv_dict = []
        self.data_csv_list = []

    def display_info(self):
        print("Среднее количество выполняемых работ в час:", self.rb)
        print("Количество окон для обслуживания:", self.ok)
        print("Среднее время обслуживания одного клиента:", self.vr)
        print("Среднее количество продаваемых товаров в час:", self.tv)

    def virab(self):
        self.virab = self.rb // self.vr
        return "\n Выработка предприятия за %s часа(ов) составляет %s" % (self.vr, self.virab)

    def bolsheokon(self):
        self.bolsheokon = self.ok + 1
        self.rb = self.rb * 1.33
        self.virab = self.rb // self.vr
        return "\n Выработка предприятия за %s часа(ов) составляет %s" % (self.vr, self.virab)

    def read_csv_variant1(self, filename):
        with open(filename) as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                self.data_csv_dict.append(row)
            print(self.data_csv_dict)

    def read_csv_variant2(self, filename):
        with open(filename) as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                self.data_csv_list.append(row)
            print(self.data_csv_list)

    def write_csv_variant1(self, filename):
        fieldnames = []
        for data in self.data_csv_dict:
            for field in data:
                fieldnames.append(field)

        with open(filename, 'w') as file:
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
            writer.writeheader()
            for row in self.data_csv_dict:
                writer.writerow(row)

    def write_csv_variant2(self, filename):
        with open(filename, 'w') as file:
            writer = csv.writer(file, delimiter=';')
            for row in self.data_csv_list:
                writer.writerow(row)
cursor.execute("""CREATE TABLE Predpriyatie (name text, okna integer, vremya integer, raboti integer, tovari integer, virab integer) """)
# Predpriyatie = [('Pered Avtomatization', '8','5','60','81'),('Posle Avtmzn','12','8','97','169')]
# cursor.executemany("INSERT INTO Predpriyatie VALUES (?,?,?,?,?)", Predpriyatie)

# sqlupdate="""
# UPDATE Predpriyatie
# SET okna = '10', vremya = '6', raboti = '89', tovari = '149' 
# WHERE name = 'Posle Avtmzn'
# """
# cursor.execute(sqlupdate)
# conn.commit()

# sqldelete="""
# DELETE FROM Predpriyatie
# WHERE name = 'Posle Avtmzn'
# """
# cursor.execute(sqldelete)
# conn.commit()

# sql = "SELECT * FROM Predpriyatie"
# cursor.execute(sql)
# conn.commit()
# print(cursor.fetchall())



a1 = work(8, 5, 60, 81)
a1.read_csv_variant1('lab3.csv')
a1.read_csv_variant2('lab3.csv')
a1.write_csv_variant1('test1.csv')
a1.write_csv_variant2('test2.csv')
a2 = work(12, 8, 97, 169)
a2.read_csv_variant2('lab3.1.csv')  
a2.read_csv_variant1('lab3.1.csv')
a2.write_csv_variant2('a2_test1.csv')
a2.write_csv_variant1('a2_test2.csv')
print(a1.virab())
print(a1.bolsheokon())
print(a2.virab())
print(a2.bolsheokon())
