class Pizza(object):
	
	description = 'unknow pizza'
	def __init__(self):
		pass

	def prepare(self):
		print 'prepare pizza'

	def bake(self):
		print 'bake pizza'

	def cut(self):
	 	print 'cut pizza'

	def box(self):
	  	print 'box pizza'

class CheesePizza(Pizza):
	def __init__(self):
		self.description = 'Cheese Pizza'

class NYStyleCheesePizza(Pizza):
	def __init__(self):
		self.description = 'NY Style Cheese Pizza'	

class GreekPizza(Pizza):
	def __init__(self):
		self.description = 'Greek Pizza'

class NYStyleGreekPizza(Pizza):
	def __init__(self):
		self.description = 'NYStyle Greek Pizza'

class PepperoniPizza(Pizza):
	def __init__(self):
		self.description = 'Pepperoni Pizza'

class NYStylePepperoniPizza(Pizza):
	def __init__(self):
		self.description = 'NYStyle Pepperoni Pizza'


# create Factory
'''
class SimplePizzaFactory(object):

	def __init__(self):
		pass

	def createPizza(self, type):
		pizza = Pizza()
		if(type == 'cheese'):
			pizza = CheesePizza()
		elif(type == 'greek'):
			pizza = GreekPizza()
		elif(type == 'pepperoni'):
			pizza = PepperoniPizza()

		return pizza
'''
class PizzaStore(object):

	def __init__(self):
		#self.simpleFactory = factory
		pass

	def orderPizza(self, type):
	
		#pizza = self.simpleFactory.createPizza(type)
		pizza = self.createPizza(type)
		pizza.prepare()
		pizza.bake()
		pizza.cut()
		pizza.box()
		return pizza

	def createPizza(self, type):	
		return Pizza()

class NYStylePizzaStore(PizzaStore):

	def __init__(self):
		pass

	def createPizza(self, type):
		pizza = Pizza()
		if(type == 'cheese'):
			pizza = NYStyleCheesePizza()
		elif(type == 'greek'):
			pizza = NYStyleGreekPizza()
		elif(type == 'pepperoni'):
			pizza = NYStylePepperoniPizza()

		return pizza


nystore = NYStylePizzaStore()
print nystore.orderPizza('cheese').description










