# coding: utf-8
from generator import Generator
from view import View
from controller import Controller
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


if __name__ == "__main__":
    root = tk.Tk()
   
    model = Generator()
    view = View(root)
    view.create_grid(8)
    view.layout()

    model.attach(view)
    model.generate()

    control = Controller(model=model, view=view)
    # control.layout()
    root.mainloop()

