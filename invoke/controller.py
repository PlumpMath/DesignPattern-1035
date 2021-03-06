class Command(object):

	def execute(self):
		pass
	def undo(self):
		pass

class NoCommand(Command):

	def execute(self):
		print 'is nocommand'
	def undo(self):
		print 'is nocommand'
# light
class Light(object):

	def on(self):
		print 'light on'
	def off(self):
		print 'light off'

class LightOnCommand(Command):
	
	def __init__(self, light):
		self.light = light
	def execute(self):
		self.light.on()
	def undo(self):
		self.light.off()

class LightOffCommand(Command):
	
	def __init__(self, light):
		self.light = light
	def execute(self):
		self.light.off()
	def undo(self):
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
	
	def __init__(self, tv):
		self.tv = tv
	def execute(self):
		self.tv.on()
	def undo(self):
		self.tv.off()

class TVOffCommand(Command):
	
	def __init__(self, tv):
		self.tv = tv
	def execute(self):
		self.tv.off()
	def undo(self):
		self.tv.on()

# stereo

class Stereo(object):

	def on(self):
		print 'stereo on'
	def off(self):
		print 'stereo off'
	def setCD(self):
		print 'set CD'
	def setVolume(self, volume):
		print 'set volume: %d' % volume

class StereoOnCommand(Command):
	
	def __init__(self, stereo):
		self.stereo = stereo
	def execute(self):
		self.stereo.on()
		self.stereo.setCD()
		self.stereo.setVolume(11)
	def undo(self):
		self.stereo.off()

class StereoOffCommand(Command):
	
	def __init__(self, stereo):
		self.stereo = stereo
	def execute(self):
		self.stereo.off()
	def undo(self):
		self.stereo.on()
		self.stereo.setCD()
		self.stereo.setVolume(11)

# CeilingFan
class CeilingFan(object):
	high = 3
	median = 2
	low = 1
	off = 0
	speed = 0

	def __init__(self):
		self.speed = self.off
	def setHigh(self):
		self.speed = self.high
		print 'set ceilingfan high'
	def setMedian(self):
		self.speed = self.median
		print 'set ceilingfan median'
	def setLow(self):
		self.speed = self.low
		print 'set ceilingfan low'
	def off(self):
		self.speed = self.off
		print 'set ceilingfan off'
	def getSpeed(self):
		return self.speed

class CeilingFanCommand(Command):
	def __init__(self, ceilingFan):
		self.ceilingFan = ceilingFan
	def undo(self):
		if(self.prevSpeed == self.ceilingFan.high):
			self.ceilingFan.setHigh()
		elif(self.prevSpeed == self.ceilingFan.median):
			self.ceilingFan.setMedian()
		elif(self.prevSpeed == self.ceilingFan.low):
			self.ceilingFan.setLow()
		else:
			self.ceilingFan.off()

class CeilingFanHigh(CeilingFanCommand):

	def execute(self):
		self.prevSpeed = self.ceilingFan.speed
		self.ceilingFan.setHigh()

class CeilingFanMedian(CeilingFanCommand):

	def execute(self):
		self.prevSpeed = self.ceilingFan.speed
		self.ceilingFan.setMedian()

class CeilingFanLow(CeilingFanCommand):

	def execute(self):
		self.prevSpeed = self.ceilingFan.speed
		self.ceilingFan.setLow()

class CeilingFanOff(CeilingFanCommand):

	def execute(self):
		self.prevSpeed = self.ceilingFan.getSpeed()
		self.ceilingFan.off()


# Macro Command
class MacroCommand(Command):

	def __init__(self, commands):
		self.commands = commands
	def execute(self):
		for item in self.commands:
			item.execute()
	def undo(self):
		for item in self.commands:
			item.undo()

# simple remote control
class simpleRemoteControl(object):

	def __init__(self, slot):
		self.slot = slot

	def setCommand(self, command):
		self.slot = command

	def buttonPressed(self):
		self.slot.execute()

'''
remote = simpleRemoteControl(LightOnCommand())
remote.buttonPressed()
remote.setCommand(TVOnCommand())
remote.buttonPressed()
'''
# remote
class RemoteControl(object):

	def __init__(self):
		self.onCommand = [NoCommand() for i in range(0, 7)]
		self.offCommand = [NoCommand() for i in range(0, 7)]
		self.lastCommand = NoCommand()

	def setCommand(self, slot, onCommand, offCommand):
		self.onCommand[slot] = onCommand
		self.offCommand[slot] = offCommand

	def onButtonWasPressed(self, slot):
		self.onCommand[slot].execute()
		self.lastCommand = self.onCommand[slot]
	def offButtonWasPressed(self, slot):
		self.offCommand[slot].execute()
		self.lastCommand = self.offCommand[slot]
	def undoButtonWasPressed(self):
		self.lastCommand.undo()


'''
remote = RemoteControl()
remote.setCommand(0, LightOnCommand(), LightOffCommand())
remote.setCommand(1, TVOnCommand(), TVOffCommand())
remote.setCommand(2, StereoOnCommand(), StereoOffCommand())


remote.undoButtonWasPressed()
for i in range(0, 3):
	remote.onButtonWasPressed(i)
	remote.undoButtonWasPressed()
	remote.offButtonWasPressed(i)
	remote.undoButtonWasPressed()
'''
remoteLoader = RemoteControl()
ceilingFan = CeilingFan()
remoteLoader.setCommand(0, CeilingFanHigh(ceilingFan), CeilingFanOff(ceilingFan))
remoteLoader.setCommand(1, CeilingFanMedian(ceilingFan), CeilingFanOff(ceilingFan))
remoteLoader.setCommand(2, CeilingFanLow(ceilingFan), CeilingFanOff(ceilingFan))

remoteLoader.onButtonWasPressed(2)
remoteLoader.onButtonWasPressed(1)
remoteLoader.undoButtonWasPressed()

light = Light()
tv = TV()
stereo = Stereo()

macroOnCommand = MacroCommand([LightOnCommand(light), TVOnCommand(tv), StereoOnCommand(stereo)])
macroOffCommand = MacroCommand([LightOffCommand(light), TVOffCommand(tv), StereoOffCommand(stereo)])
remoteLoader.setCommand(3, macroOnCommand, macroOffCommand)

remoteLoader.onButtonWasPressed(3)
remoteLoader.offButtonWasPressed(3)
remoteLoader.undoButtonWasPressed()
