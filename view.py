# coding: utf-8
from generator import Generator
from observer import Observer
from math import pi, sin, radians
import sys
import numpy as np
import math
import logging
from time import strftime
from datetime import date
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
        self.signal_type = 10
        self.signal_x = []
        self.signal_y = []
        self.signals = {}
        self.colors = {
            "X": "red",
            "Y": "blue"
        }
        self.radius = 10
        self.x = 0
        self.y = 0
        self.parent.protocol("WM_DELETE_WINDOW", self.exit)
        self.gui()

        self.controls = tk.PanedWindow(self.parent, orient=tk.HORIZONTAL)
        self.controls.pack(expand=True, fill='both')
        self.colors_control = "X"
        self.spot = self.screen.create_oval(
            self.x-self.radius, self.y-self.radius,
            self.x+self.radius, self.y+self.radius,
            fill=self.colors[self.colors_control], outline="black", tags="spot"

        )
        self.width_canvas = int(self.screen.cget("width"))
        self.height_canvas = int(self.screen.cget("height"))

    def exit(self):
        sure = tk.messagebox.askokcancel("Quit", "Are you sure you want to exit?",
                                         parent=self.parent)
        if sure == True:
            self.parent.destroy()

    def create(self):
        self.win = tk.Toplevel(self.parent)
        self.screen_toplevel = tk.Canvas(self.win, bg=self.bg,
                                         width=self.width, height=self.height)
        self.screen_toplevel.configure(relief="flat")
        self.screen_toplevel.pack(expand=True, fill="both", padx=10, pady=20)
        self.create_grid_toplevel(8)
        x_values = [point[1] for point in self.signals['X']]
        y_values = [point[1] for point in self.signals['Y']]
        xy = [[x_values[i], y_values[i]] for i in np.arange(len(x_values))]
        print(xy)
        # x= 
        self.plot_signal_toplevel(
            signal=[x_values, y_values], color="blue")


    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def gui(self):
        print("Generator.gui()")
        self.mode_xy = tk.Button(self.parent, text="X-Y")
        self.mode_xy.pack()
        self.screen = tk.Canvas(self.parent, bg=self.bg,
                                width=self.width, height=self.height)
        self.screen.configure(relief="flat")

        self.screen.pack(expand=True, fill="both", padx=10, pady=20)

    def new_file(self):
        pass

    def update(self, subject, isanimate=False):
        if subject.signal:
            signals_list = []
            for key, value in self.signals.items():
                signals_list.append(value)

            self.plot_signal(signal=subject.signal, color="yellow")
            

    def plot_signal(self, name="X", signal=[], color={}):
        color = self.colors
        print("Generator.plot_signal()")
        print(len(self.signals))
        for key, value in self.signals.items():
            if signal and len(signal) > 1:
                w, h = self.width, self.height
                if self.screen.find_withtag(key):
                    self.screen.delete(key)
                plots = [(x*w, (h/self.units)*y+h/2) for (x, y) in value]
                self.screen.create_line(
                    plots, fill=color[key], smooth=1, width=3, tags=name,
                )

    def animate_spot(self, canvas, signal, i=0):
        width, height = canvas.winfo_width(), canvas.winfo_height()
        m_sec = 20
        if i == len(signal):
            i = 0

        x, y = signal[i][0]*width, height/self.units*(signal[i][1])+height/2
        canvas.coords(self.spot, x, y, x+self.radius, y+self.radius)
        after_id = self.screen.after(
            m_sec, self.animate_spot, canvas, signal, i+1)
        return after_id

    def plot_signal_toplevel(self, name="X", signal=[], color="red"):
        print("Generator.plot_signal()")
        if signal and len(signal) > 1:
            w, h = self.width, self.height
            if self.screen_toplevel.find_withtag(name):
                self.screen_toplevel.delete(name)
            plots = [(x*w, (h/self.units)*y+h/2) for x, y in signal]
            self.screen_toplevel.create_line(
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

    def create_grid_toplevel(self, tiles=2):
        print("Generator.create_grid()")
        if self.screen_toplevel.find_withtag("grid"):
            self.screen_toplevel.delete("grid")
        self.units = tiles
        tile_x = self.width/tiles
        for t in range(1, tiles+1):
            x = t*tile_x
            self.screen_toplevel.create_line(x, 0, x, self.height, tags="grid")
            self.screen_toplevel.create_line(
                x, self.height/2-10, x, self.height/2+10, width=3, tags="grid")
        tile_y = self.height/tiles
        for t in range(1, tiles+1):
            y = t*tile_y
            self.screen_toplevel.create_line(0, y, self.width, y, tags="grid")
            self.screen_toplevel.create_line(
                self.width/2-10, y, self.width/2+10, y, width=3, tags="grid")

    def resize(self, event):
        print("Generator.resize()")
        self.width, self.height = event.width, event.height
        print("width,height", self.width, self.height)
        # self.screen.config(width=self.width, height=self.height)
        self.create_grid(8)
        self.plot_signal()

    def layout(self):
        print("Generator.layout()")


if __name__ == "__main__":
    root = tk.Tk()
    model = Generator()
    view = View(root)
    view.create_grid(8)
    view.layout()
    # model.attach(view)
    model.generate()
    root.mainloop()
