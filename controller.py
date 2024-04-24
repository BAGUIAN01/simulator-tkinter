# coding: utf-8
from view import View
from generator import Generator
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


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.name = "control"
        self.actions_binding()

    def actions_binding(self):

        self.view.screen.bind("<Configure>", self.view.resize)
        self.view.scaleA.bind("<B1-Motion>", self.on_magnitude_action)
        self.view.scaleF.bind("<B1-Motion>", self.on_frequence_action)
        self.view.scaleP.bind("<B1-Motion>", self.on_phasis_action)
        self.view.scaleHarmic.bind("<B1-Motion>", self.on_harmonic_action)
        self.view.pair_harmonic.bind(
            "<Button-1>", self.on_pairharmonic_action)
        self.view.impair_harmonic.bind(
            "<Button-1>", self.on_impairharmonic_action)
        self.view.all_harmonic.bind(
            "<Button-1>", self.on_allharmonic_action)

    def on_magnitude_action(self, event):

        if self.model.m != self.view.var_mag.get():
            self.model.m = self.view.var_mag.get()
            print(f"varmag {self.model.m}")
            self.model.generate()

    def on_frequence_action(self, event):

        if self.model.f != self.view.var_freq.get():
            self.model.f = self.view.var_freq.get()

            self.model.generate()

    def on_phasis_action(self, event):

        if self.model.p != self.view.var_p.get():
            self.model.p = self.view.var_p.get()
            print(f"varmag {self.model.p}")
            self.model.generate()

    def on_harmonic_action(self, event):

        if self.model.harmonics != self.view.var_harmonic.get():
            self.model.harmonics = self.view.var_harmonic.get()
            print(f"varmag {self.model.harmonics}")
            self.model.generate()

    def on_pairharmonic_action(self, event):

        if self.view.pair_var.get() == 1:
            self.model.pair = True
            self.model.impair = False
            self.model.generate()
        else:
            pass

    def on_impairharmonic_action(self, event):

        if self.view.impair_var.get() == 2:

            self.model.pair = False
            self.model.impair = True
            self.model.generate()
        else:
            pass

    def on_allharmonic_action(self, event):

        if self.view.all_var.get() == 3:

            self.model.pair = True
            self.model.impair = True
            self.model.generate()
        else:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    model = Generator()
    view = View(root)
    model.attach(view)
    view.create_grid(8)
    view.layout()
    control = Controller(model, view)
    root.mainloop()
