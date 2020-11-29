import csv


class work:
    def __init__(self, okna, vremya, raboti, tovari):
        self.ok = okna
        self.vr = vremya
        self.rb = raboti
        self.tv = tovari
        self.data_csv_dict = []
        self.data_csv_list = []

    def __return__(self):
        return "\n Количество работ в час = {} \n Количество окон = {} \n Время обслуживания одного клиента = {} \n  Продаваемых товаров в час = {}".format(
            self.rb, self.ok, self.vr, self.tv)

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


a1 = work(8, 5, 60, 81)
a1.read_csv_variant1('lab3.csv')
a2 = work(12, 8, 97, 169)
a2.read_csv_variant2('lab3.1.csv')  
print(a1.virab())
print(a1.bolsheokon())
print(a2.virab())
print(a2.bolsheokon())
