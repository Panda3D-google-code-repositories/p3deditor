from direct.task import Task
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *

class InputHandler(DirectObject):
	def __init__(self):
		#ballancer
		self.scrollSpeed = 2
		#moving camera vars
		self.pressedW = False
		self.pressedS = False
		self.pressedX = False
		self.pressedY = False
		self.pressedZ = False
		self.pressedH = False
		self.pressedP = False
		self.pressedR = False
		self.pressedL = False
		self.pressedD = False
		self.pressedA = False
		self.pressedQ = False
		#setting it active by default
		self.setActive()
		self.oldCoo = []
		#point on surface handling
		self.pointOnSurfaceRequested = False
		
		#DEBUGGING ONLY
		#FROM HERE
		self.accept("m",self.getPointNow)
	
	def getPointNow(self):
		p = myCamera.mc.pickPointOnSurface()
		if p != None:
			print "Point: "+str(p[0])
			print "Normal: "+str(p[1])
		#TO HERE
	
	def requestPointOnSurface(self,caller):
		self.pointOnSurfaceRequested = True
		self.accept("mouse1", self.dropRequestPointOnSurface, [caller])
	
	def dropRequestPointOnSurface(self,caller):
		self.pointOnSurfaceRequested = False
		p = myCamera.mc.pickPointOnSurface()
		caller.pointOnSurface(p)
	
	def modObjects(self,task):
		dt = globalClock.getDt()
		
		#resolving Q event
		if self.pressedQ == True:
			if self.pressedW == True:
				# figure out how much the mouse has moved (in pixels)
				p = myCamera.mc.pickPointOnSurface()
				if p != None:
					for obj in self.objList:
						obj.getModel().setPos(p[0])
						obj.getModel().lookAt(p[0]+p[1])
						obj.getModel().setP(obj.getModel().getP()-90) #small fix to do in order to get a good placement
		
		#resolving L event
		if self.pressedL == True:
			if self.pressedP == True:
				#this is to avoid flood of requests
				#aka the user has to -up the key and then to press it again in order to do an other request
				print "INFO: creating new point light"
				myObjectManager.addPointLight()
				self.pressedP = False
			
			if self.pressedD == True:
				print "INFO: creating new directional light"
				self.pressedD = False
			
			if self.pressedA == True:
				print "INFO: creating new ambient light"
				self.pressedA = False
		
			dt = globalClock.getDt()
		
		#resolving S event
		if self.pressedS == True:
			# figure out how much the mouse has moved (in pixels)
			md = base.win.getPointer(0)
			x = md.getX()
			y = md.getY()
			if base.win.movePointer(0, 300, 300):
				for obj in self.objList:
					if obj.getType() == "StaticMeshObject":
						obj.getModel().setScale(obj.getModel().getScale()+((x-300)*0.01))
		
		#resolving X event
		if self.pressedX == True:
			# figure out how much the mouse has moved (in pixels)
			md = base.win.getPointer(0)
			x = md.getX()
			y = md.getY()
			if base.win.movePointer(0, 300, 300):
				for obj in self.objList:
					obj.setX((x-300)*0.01)
		
		#resolving Y event
		if self.pressedY == True:
			# figure out how much the mouse has moved (in pixels)
			md = base.win.getPointer(0)
			x = md.getX()
			y = md.getY()
			if base.win.movePointer(0, 300, 300):
				for obj in self.objList:
					obj.setY((x-300)*0.01)
		
		#resolving Z event
		if self.pressedZ == True:
			# figure out how much the mouse has moved (in pixels)
			md = base.win.getPointer(0)
			x = md.getX()
			y = md.getY()
			if base.win.movePointer(0, 300, 300):
				for obj in self.objList:
					obj.setZ((x-300)*0.01)
		
		#resolving H event
		if self.pressedH == True:
			# figure out how much the mouse has moved (in pixels)
			md = base.win.getPointer(0)
			x = md.getX()
			y = md.getY()
			if base.win.movePointer(0, 300, 300):
				for obj in self.objList:
					obj.setH((x-300)*0.01)
		
		#resolving P event
		if self.pressedP == True:
			# figure out how much the mouse has moved (in pixels)
			md = base.win.getPointer(0)
			x = md.getX()
			y = md.getY()
			if base.win.movePointer(0, 300, 300):
				for obj in self.objList:
					obj.setP((x-300)*0.01)
		
		#resolving R event
		if self.pressedR == True:
			# figure out how much the mouse has moved (in pixels)
			md = base.win.getPointer(0)
			x = md.getX()
			y = md.getY()
			if base.win.movePointer(0, 300, 300):
				for obj in self.objList:
					obj.setR((x-300)*0.01)
		
		return Task.cont
	
	def setInactive(self):
		# Main Modifier
		self.ignoreAll()
		taskMgr.remove("objectModifierTask")
	
	def setActive(self):
		#custom events
		self.accept("e", myObjectManager.removeSelectedObjects)
		self.accept("f12", myApp.exportScene)
		#used to place and do mouse/geom collision
		self.accept("m", self.getPointNow)
		
		# Main Modifier
		self.accept("w", self.pressKey, ["w"])
		self.accept("w-up", self.releaseKey, ["w"])
		self.accept("q", self.pressKey, ["q"])
		self.accept("q-up", self.releaseKey, ["q"])
		self.accept("s", self.pressKey, ["s"])
		self.accept("s-up", self.releaseKey, ["s"])
		self.accept("x", self.pressKey, ["x"])
		self.accept("x-up", self.releaseKey, ["x"])
		self.accept("y", self.pressKey, ["y"])
		self.accept("y-up", self.releaseKey, ["y"])
		self.accept("z", self.pressKey, ["z"])
		self.accept("z-up", self.releaseKey, ["z"])
		self.accept("h", self.pressKey, ["h"])
		self.accept("h-up", self.releaseKey, ["h"])
		self.accept("p", self.pressKey, ["p"])
		self.accept("p-up", self.releaseKey, ["p"])
		self.accept("r", self.pressKey, ["r"])
		self.accept("r-up", self.releaseKey, ["r"])
		self.accept("l", self.pressKey, ["l"])
		self.accept("l-up", self.releaseKey, ["l"])
		self.accept("d", self.pressKey, ["d"])
		self.accept("d-up", self.releaseKey, ["d"])
		self.accept("a", self.pressKey, ["a"])
		self.accept("a-up", self.releaseKey, ["a"])
		#self.ignore()
		taskMgr.add(self.modObjects, "objectModifierTask")
	
	def releaseKey(self,key):
		myCamera.mm.showMouse()
		#restoring old coo and emptying list
		
		#avoiding crash if someone click outside window
		if base.mouseWatcherNode.hasMouse():
			base.win.movePointer(0, int(self.oldCoo[0]), int(self.oldCoo[1]))
		oldCoo = []
		if key == "w":
			self.pressedW = False
		if key == "s":
			self.pressedS = False
		if key == "q":
			self.pressedQ = False
		if key == "x":
			self.pressedX = False
		if key == "y":
			self.pressedY = False
		if key == "z":
			self.pressedZ = False
		if key == "h":
			self.pressedH = False
		if key == "p":
			self.pressedP = False
		if key == "r":
			self.pressedR = False
		if key == "l":
			self.pressedL = False
		if key == "d":
			self.pressedD = False
		if key == "a":
			self.pressedA = False
	
	def calcUnlockedObjects(self):
		#print"DEBUG: calculating all unlocked objects"
		objList = myCamera.getSelectionTool().listSelected
		unlockedObjList = []
		for obj in objList:
			if obj.getLocking() == False:
				unlockedObjList.append(obj)
		return unlockedObjList
	
	def pressKey(self,key):
		myCamera.mm.hidMouse()
		#lulz system to restore old mouse coordinates after objects modifying
		md = base.win.getPointer(0)
		self.oldCoo = [md.getX(),md.getY()]
		base.win.movePointer(0, 300, 300)
		
		#refreshing unlocked object list
		self.objList = self.calcUnlockedObjects()
		
		if key == "w":
			self.pressedW = True
		if key == "q":
			self.pressedQ = True
		if key == "s":
			self.pressedS = True
		if key == "x":
			self.pressedX = True
		if key == "y":
			self.pressedY = True
		if key == "z":
			self.pressedZ = True
		if key == "h":
			self.pressedH = True
		if key == "p":
			self.pressedP = True
		if key == "r":
			self.pressedR = True
		if key == "l":
			self.pressedL = True
		if key == "d":
			self.pressedD = True
		if key == "a":
			self.pressedA = True
