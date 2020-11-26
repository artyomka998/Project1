class work:
	def __init__(self,okna,vremya,raboti,tovari):
		self.ok=okna
		self.vr=vremya
		self.rb=raboti
		self.tv=tovari
	def __return__(self):
		return "\n Количество работ в час = {} \n Количество окон = {} \n Время обслуживания одного клиента = {} \n  Продаваемых товаров в час = {}".format (self.rb,self.ok,self.vr,self.tv)
	def display_info(self):
		print("Среднее количество выполняемых работ в час:",self.rb)
		print("Количество окон для обслуживания:",self.ok)
		print("Среднее время обслуживания одного клиента:",self.vr)
		print("Среднее количество продаваемых товаров в час:",self.tv)
	def virab(self):
		self.virab=self.rb // self.vr
		return "\n Выработка предприятия за %s часа(ов) составляет %s" % (self.vr,self.virab)
	def bolsheokon(self):
		self.bolsheokon=self.ok + 1
		self.rb=self.rb * 1.33 
		self.virab=self.rb // self.vr	
		return "\n Выработка предприятия за %s часа(ов) составляет %s" % (self.vr,self.virab)
a1 = work(8, 5,60, 81)
a2 = work(12, 8,97,169)
print (a1.virab())
print (a1.bolsheokon())
print (a2.virab())
print (a2.bolsheokon())

	