class CaffeineBeverage(object):

	def prepareRecipe(self):
		self.boilWater()
		self.brew()
		self.poutInCup()
		self.addCondiments()

	def boilWater(self):
		print 'Boiling Water'
	def brew(self):
		pass
	def poutInCup(self):
		print 'Pouring in cup'
	def addCondiments(self):
		pass

class Coffee(CaffeineBeverage):
	def brew(self):
		print 'brew coffee'
	def addCondiments(self):
		print 'add sugar & milk'

cafe = Coffee()
cafe.prepareRecipe()

class Tea(CaffeineBeverage):
	def brew(self):
		print 'brew tea bag'
	def addCondiments(self):
		print 'add lemon'

tea = Tea()
tea.prepareRecipe()