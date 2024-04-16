# coding: utf-8
from generator import Generator
from observer import Observer
from math import pi, sin, radians
import sys
import math
import logging
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


class View(Observer):
    def __init__(self, parent, bg="white", width=600, height=300):
        self.parent = parent
        self.bg = bg
        self.width, self.height = width, height
        self.name = "Controls"

        self.gui()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def gui(self):
        print("Generator.gui()")
        self.screen = tk.Canvas(self.parent, bg=self.bg,
                                width=self.width, height=self.height)
        self.frame = tk.LabelFrame(self.parent, text=self.name)
        self.var_mag = tk.IntVar()
        self.var_mag.set(1)

        self.scaleA = tk.Scale(self.frame, variable=self.var_mag,
                               label="Amplitude",
                               orient="horizontal", length=250,
                               from_=0, to=5, tickinterval=1)

        self.var_freq = tk.IntVar()
        self.var_freq.set(1)
        self.scaleF = tk.Scale(self.frame, variable=self.var_freq,
                               label="frequence",
                               orient="horizontal", length=250,
                               from_=0, to=5, tickinterval=1)

        self.var_p = tk.IntVar()
        self.var_p.set(1)
        self.scaleP = tk.Scale(self.frame, variable=self.var_p,
                               label="Phase",
                               orient="horizontal", length=250,
                               from_=-50, to=50, tickinterval=1)

        self.var_harmonic = tk.IntVar()
        self.var_harmonic.set(1)
        self.scaleHarmic = tk.Scale(self.frame, variable=self.var_harmonic,
                                    label="Harmonic",
                                    orient="horizontal", length=250,
                                    from_=0, to=5, tickinterval=1)

        self.frame_harmonic = tk.LabelFrame(self.parent, text="harmonic")
        self.pair_var = tk.BooleanVar()
        self.pair_harmonic = tk.Checkbutton(self.frame_harmonic, text="Pair",
                                            variable=self.pair_var)
        self.impair_var = tk.BooleanVar()
        self.impair_harmonic = tk.Checkbutton(
            self.frame_harmonic, text="Impair",
            variable=self.impair_var
        )
        self.all_var = tk.BooleanVar()
        self.all_harmonic = tk.Checkbutton(
            self.frame_harmonic, text="Tout afficher",
            variable=self.all_var
        )

    def update(self, subject):
        print("Generator.update()")
        print("Update signal", self.get_name())
        if subject.signal:

            self.plot_signal(signal=subject.signal)

    def plot_signal(self, name="X", signal=[], color="red"):
        print("Generator.plot_signal()")
        if signal and len(signal) > 1:
            w, h = self.width, self.height
            if self.screen.find_withtag(name):
                self.screen.delete(name)
            plots = [(x*w, (h/self.units)*y+h/2) for (x, y) in signal]
            self.screen.create_line(
                plots, fill=color, smooth=1, width=3, tags=name)
        return

    def create_grid(self, tiles=2):
        print("Generator.create_grid()")
        if self.screen.find_withtag("grid"):
            self.screen.delete("grid")
        self.units = tiles
        tile_x = self.width/tiles
        for t in range(1, tiles+1):
            x = t*tile_x
            self.screen.create_line(x, 0, x, self.height, tags="grid")
            self.screen.create_line(
                x, self.height/2-10, x, self.height/2+10, width=3, tags="grid")
        tile_y = self.height/tiles
        for t in range(1, tiles+1):
            y = t*tile_y
            self.screen.create_line(0, y, self.width, y, tags="grid")
            self.screen.create_line(
                self.width/2-10, y, self.width/2+10, y, width=3, tags="grid")

    def resize(self, event):
        print("Generator.resize()")
        self.width, self.height = event.width, event.height
        print("width,height", self.width, self.height)
        # TO DO  :
        # delete existing grid
        # create grid with new dimension
        # plot signal with new dimension

    def layout(self):
        print("Generator.layout()")
        self.screen.pack()
        # self.screen.pack(fill="x")
        # self.screen.pack(fill="both",padx=10,pady=20)
        # self.screen.pack(expand=True,fill="both",padx=10,pady=20)
        self.frame.pack()
        self.scaleA.grid(row=0, column=0,)
        self.scaleF.grid(row=1, column=0)
        self.scaleP.grid(row=2, column=0)
        self.scaleHarmic.grid(row=3, column=0)

        self.frame_harmonic.pack()
        self.pair_harmonic.grid(row=0, column=0)
        self.impair_harmonic.grid(row=0, column=1)
        self.all_harmonic.grid(row=0, column=3)
        # self.scaleHarmic.pack()


if __name__ == "__main__":
    root = tk.Tk()
    model = Generator()
    view = View(root)
    view.create_grid(8)
    view.layout()
    # model.attach(view)
    model.generate()
    root.mainloop()
