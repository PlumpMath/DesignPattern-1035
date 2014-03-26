class Command(object):

	def execute(self):
		pass

# light
class Light(object):

	def on(self):
		print 'light on'

	def off(self):
		print 'light off'

class LightOnCommand(Command):
	
	def __init__(self):
		self.light = Light()

	def execute(self):
		self.light.on()

# TV 
class TV(object):

	def on(self):
		print 'TV on'

	def off(self):
		print 'TV off'

	def setInputChannel(self, channel):
		self.channel = channel
		print 'set channel: %d' % channel
	
	def setVolume(self, volume):
		self.volume = volume
		print 'set volume: %d' % volume

class TVOnCommand(Command):
	
	def __init__(self):
		self.tv = TV()

	def execute(self):
		self.tv.on()


class simpleRemoteControl(object):

	def __init__(self, slot):
		self.slot = slot

	def setCommand(self, command):
		self.slot = command

	def buttonPressed(self):
		self.slot.execute()


remote = simpleRemoteControl(LightOnCommand())
remote.buttonPressed()
remote.setCommand(TVOnCommand())
remote.buttonPressed()




