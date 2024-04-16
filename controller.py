# coding: utf-8
from math import pi, sin, radians
import sys
import math
major = sys.version_info.major
minor = sys.version_info.minor
if major == 2 and minor == 7:
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major == 3:
    import tkinter as tk
    from tkinter import filedialog
else:
    if __name__ == "__main__":
        print("Your python version is : ", major, minor)
        print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog
from generator import Generator
from view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.name = "control"
        self.actions_binding()


    

    def actions_binding(self):
        print("Generator.actions_binding()")
        self.screen.bind("<Configure>", self.resize)
        self.scaleA.bind("<B1-Motion>", self.on_magnitude_action)
    # callbacks (on_<name>_action(...) )

    def on_magnitude_action(self, event):
        print("Generator.on_magnitude_action()")
        if self.m != self.var_mag.get():
            self.m = self.var_mag.get()
            self.model.generate()
            self.update()


if __name__ == "__main__":
    root = tk.Tk()
    model = Generator()
    view = View(root)
    model.attach(view)
    view.create_grid(8)
    view.layout()
    control = Controller(model, view)
    root.mainloop()


