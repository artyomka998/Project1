class work:
	def __init__(okna,vremya,raboti,tovari):
		self.rb=raboti
		self.ok=okna
		self.vr=vremya
		self.tv=tovari
	def display_info(self):
		print("Среднее количество выполняемых работ в час:",self.rb)
		print("Количество окон для обслуживания:",self.ok)
		print("Среднее время обслуживания одного клиента:",self.vr)
		print("Среднее количество продаваемых товаров в час:",self.tv)
	def virab(self):
		self.virab=self.rb // self.vr
		return "\n Выработка предприятия за время %s составляет %s" % (self.vr,self.virab)
	def bolsheokon(self):
		self.bolsheokon=self.ok + 1
		self.rb=self.rb * 1.33 
		self.virab=self.rb // self.vr	
		return "\n Выработка предприятия за время %s составляет %s" % (self.vr,self,virab)
	exmpl1=work("Установка нового рабочего окна", 3,"Количество выполняемых работ в день", 30)
	exmpl2=work("Увеличено количество рабочих окон", 4,"Количество выполняемых работ в день",40)
	print (exmpl1.virab())
	print (exmpl1.bolsheokon())
	elist=list()
	elist.append(exmpl1)
	elist.append(exmpl2)
	print(elist)
	