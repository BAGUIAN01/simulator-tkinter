from math import pi

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class TkTimer(object):
	def __init__(self,parent,timeout = 0,startOnCreation=True,callback=lambda : None,*args) -> None:
		assert isinstance(parent,tk.Misc),"Parent should be an instance of <tk.Misc>"
		
		self.running = False #must use this at first because of the setter format

		self.parent = parent

		self.timeout = timeout

		self.__callback = []
		self.callback = callback
		self.callbackArgs = args
		self.running = startOnCreation #running must be set after callback and callbackargs
	
	#Accessors / setters

	def addCallback(self,newCallback):
		self.__callback.append(newCallback)

	parent = property(lambda self : self.__parent,lambda self, val : setattr(self,"_TkTimer__parent",val))

	timeout = property(lambda self : self.__timeout,lambda self, val : setattr(self,"_TkTimer__timeout",val))
	callback = property(lambda self : self.__callback,lambda self, val : setattr(self,"_TkTimer__callback",[val]))
	callbackArgs = property(lambda self : self.__callbackArgs,lambda self, *args : setattr(self,"_TkTimer__callbackArgs",*args))

	#if the timer isn't running, set running to True and call the after function a first time
	running = property(lambda self : self.__running,lambda self, val : setattr(self,"_TkTimer__running",((self.parent.after(self.timeout,self.__internalCallback) or True) if (val == True and self.__running == False) else False)))

	def __internalCallback(self):
		# print("__internalCallback")
		if(not(self.running)):#if shouldn't be running anymore
			return
		self.parent.after(self.timeout,self.__internalCallback)
		for cb in self.callback:
			cb(*self.callbackArgs)
