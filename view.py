# coding: utf-8
from generator import Generator
from observer import Observer
from math import pi, sin, radians
import sys
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
        self.radius = 10
        self.x = 0
        self.y = 0

        self.gui()


        self.controls = tk.PanedWindow(self.parent, orient=tk.HORIZONTAL)
        self.controls.pack(expand=True, fill='both')

        self.spot = self.screen.create_oval(
            self.x-self.radius, self.y-self.radius,
            self.x+self.radius, self.y+self.radius,
            fill="red", outline="black", tags="spot"

        )
        self.width_canvas = int(self.screen.cget("width"))
        self.height_canvas = int(self.screen.cget("height"))

    def create(self):
        self.win = tk.Toplevel(self.parent)
        self.screen_toplevel = tk.Canvas(self.win, bg=self.bg,
                                         width=self.width, height=self.height)
        self.screen_toplevel.configure(relief="flat")
        self.screen_toplevel.pack(expand=True, fill="both", padx=10, pady=20)
        self.create_grid_toplevel(8)
        self.plot_signal_toplevel(signal=self.signal_x, color="blue")
        self.plot_signal_toplevel(signal=self.signal_y, color="red")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def gui(self):
        print("Generator.gui()")
        # self.menubar = tk.Menu(self.parent)
        # self.parent.config(menu=self.menubar)

        # self.file_menu = tk.Menu(self.menubar, tearoff=0)
        # self.menubar.add_cascade(label="File", menu=self.file_menu)

        # self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        # self.menubar.add_cascade(label="Edit", menu=self.edit_menu)

        self.screen = tk.Canvas(self.parent, bg=self.bg,
                                width=self.width, height=self.height)
        self.screen.configure(relief="flat")
        self.screen.pack(expand=True, fill="both", padx=10, pady=20)

       
        # # right controls

        # self.model_var = tk.IntVar()
        # self.model_var.set(10)
        # self.signal_x = tk.Radiobutton(
        #     self.frame_harmonics, text="modèle X",
        #     value=10,
        #     variable=self.model_var
        # )
        # self.signal_y = tk.Radiobutton(
        #     self.frame_harmonics, text="modèle Y",
        #     value=20,
        #     variable=self.model_var
        # )
        # self.signal_xy = tk.Radiobutton(
        #     self.frame_harmonics, text="modèle X-Y",
        #     value=30,
        #     variable=self.model_var
        # )
        # self.signal_type = self.model_var
        # print(self.model_var)

    def new_file(self):
        pass

    def update(self, subject, isanimate=False):
        print("Generator.update()")
        print("Update signal", self.get_name())
        if subject.signal:

            self.plot_signal(signal=subject.signal)
            if (isanimate):
                self.plot_signal(subject.point, "animation", color="blue")

    def plot_signal(self, name="X", signal=[], color="red", isanimate=False):
        print("Generator.plot_signal()")
        if signal and len(signal) > 1:
            w, h = self.width, self.height
            if self.screen.find_withtag(name):
                self.screen.delete(name)
            plots = [(x*w, (h/self.units)*y+h/2) for (x, y) in signal]
            self.screen.create_line(
                plots, fill=color, smooth=1, width=3, tags=name,
            )
        elif signal and isanimate:
            # print("in plotsignal for animation")
            self.screen.delete(name)
            x = signal[0]*self.width
            y = self.height/2*(signal[1]+1)
            pointSize = 5
            self.screen.create_oval(
                x-pointSize, y-pointSize, x+pointSize, y+pointSize, fill=color, tags=name)
        return

    def animate_spot(self, canvas, signal, i=0):
        width, height = canvas.winfo_width(), canvas.winfo_height()
        m_sec = 20
        if i == len(signal):
            i = 0

        x, y = signal[i][0]*width, height/3*(signal[i][1]+1)
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
            plots = [(x*w, (h/self.units)*y+h/2) for (x, y) in signal]
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
        # self.header.pack(expand=True, fill="both", padx=10, pady=20)

        # self.title.grid(row=0, column=0, sticky="ew", padx=10)
        # self.clock.grid(row=0, column=1, sticky="ew")
        # self.divider.grid(row=0, column=2, sticky="ew")

        # self.divider2.grid(row=0, column=6, sticky="ew")

        # self.frame.pack(expand=True, fill="both", padx=5, pady=5)
        # self.frame_right.grid(row=0, column=1)

        # self.frame_left.grid(row=0, column=0)
        # self.scaleA.grid(row=0, column=0)
        # self.scaleF.grid(row=1, column=0)
        # self.scaleP.grid(row=2, column=0)
        # self.scaleHarmic.grid(row=3, column=0)
        # self.scale_sample.grid(row=4, column=0)
        # self.frame_bottom.grid(row=0, column=1)
        # self.frame_harmonics.pack(expand=True, fill="both", padx=10, pady=20)
        # self.pair_harmonic.grid(row=0, column=0, sticky="ew")
        # self.impair_harmonic.grid(row=0, column=1, sticky="ew")
        # self.all_harmonic.grid(row=0, column=2)

        # self.frame_model.pack(expand=True, fill="both", padx=10, pady=20)
        # self.signal_x.grid(row=0, column=7, sticky="ew")
        # self.signal_y.grid(row=0, column=8, sticky="ew")
        # self.signal_xy.grid(row=0, column=9, sticky="ew")
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
