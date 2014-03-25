class Beverage(object):
	"""docstring for Beverage"""
	description = 'unKnow beverage'
	def __init__(self):
		pass
	def cost(self):
		pass
	def getDescription(self):
		return self.description

# condiment

class Condiment(Beverage):
	"""docstring for Condiment"""
	def getDescription(self):
		pass

# concrete beveage
	
class Expresso(Beverage):
	description = 'Expresson'

	def cost(self):
		return 1.99

class HouseBlend(Beverage):
	description = 'House Blend'

	def cost(self):
		return	0.89	
	
class DarkRoast(Beverage):
	description = 'DarkRoast'

	def cost(self):
		return	1.19

# decorate

class Mocha(Condiment):
	beverage = Beverage()
	def __init__(self, beverage):
		self.beverage = beverage
		self.description = '%s + Mocha' % self.beverage.description
	def getDescription(self):
		return '%s + Mocha' % self.beverage.description
	def cost(self):
		return beverage.cost()+0.2
		
class Milk(Condiment):
	beverage = Beverage()
	def __init__(self, beverage):
		self.beverage = beverage
		self.description = '%s + Milk' % self.beverage.description
	def getDescription(self):
		return '%s + Milk' % self.beverage.description
	def cost(self):
		return self.beverage.cost()+0.5

class Soy(Condiment):
	beverage = Beverage()
	def __init__(self, beverage):
		self.beverage = beverage
		self.description = '%s + Soy' % self.beverage.description
	def getDescription(self):
		return '%s + Soy' % self.beverage.description
	def cost(self):
		return self.beverage.cost()+0.3

class Whip(Condiment):
	beverage = Beverage()
	def __init__(self, beverage):
		self.beverage = beverage
		self.description = '%s + Whip' % self.beverage.description
	def getDescription(self):
		return '%s + Whip' % self.beverage.description
	def cost(self):
		return self.beverage.cost()+0.19

# Cafe Shop

class TTCoffee(object):
	
	def __init__(self):
		pass

	def testOrder(self):
		# Cappuccino = Expresso + whip
		cappuccino = Whip(Expresso())
		print cappuccino.getDescription()
		print cappuccino.cost()

		# black coffee
		blackcoffee = HouseBlend()
		print blackcoffee.getDescription()
		print blackcoffee.cost()

		# special coffee
		special = Whip(Whip(Soy(Expresso())))
		print special.getDescription()
		print special.cost()


shop = TTCoffee()

shop.testOrder()
























