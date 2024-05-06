# coding: utf-8
from generator import Generator
from generator2 import Generator2
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
    root.configure(background="black")
    root.title("Simulateur")
    # root.option_readfile("oscillo.opt")

    view = View(root)
    model_x = Generator()
    model_y = Generator2()
    view.create_grid(8)
    view.layout()

    model_x.attach(view)
    model_x.generate()
    model_y.attach(view)
    model_y.generate()

    control = Controller(model=model_x, model_y=model_y,
                         mode=view.signal_type, view=view)
    # control.layout()
    root.mainloop()
