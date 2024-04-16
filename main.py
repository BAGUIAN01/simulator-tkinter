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


class Generator:
    def __init__(self, parent, bg="white", width=600, height=300):
        self.parent = parent
        self.bg = bg
        self.width, self.height = width, height
        self.name = "X"
        self.signal = []
        self.m, self.f, self.p = 1.0, 2.0, 0.0
        self.harmonics = 1
        self.samples = 100
        self.units = 1
        self.gui()
        self.actions_binding()
    # properties getter/setter

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_signal(self):
        return self.signal

    def set_signal(self, signal):
        self.signal = signal

    def get_magnitude(self):
        pass

    def set_magnitude(self, magnitude):
        pass

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

    def actions_binding(self):
        print("Generator.actions_binding()")
        self.screen.bind("<Configure>", self.resize)
        self.scaleA.bind("<B1-Motion>", self.on_magnitude_action)
    # callbacks (on_<name>_action(...) )

    def on_magnitude_action(self, event):
        print("Generator.on_magnitude_action()")
        if self.m != self.var_mag.get():
            self.m = self.var_mag.get()
            self.generate()
            self.update()

    def vibration(self, t):
        # Warning : take care of degrees_to_radians conversion on phase (self.p)
        # if you get degree from your slider, use radians() function from math module to convert
        m, f, p = self.m, self.f, self.p
        harmo = int(self.harmonics)
        sum = 0
        for h in range(1, harmo+1):
            sum = sum + (m/h)*sin(2*pi*(f*h)*t)-p
        return sum

    def generate(self):
        print("Generator.generate()")
        del self.signal[0:]
        samples = int(self.samples)
        for t in range(samples+1):
            self.signal.append([t/samples, self.vibration(t/samples)])
        return self.signal

    def update(self):
        print("Generator.update()")
        print("Update signal", self.get_name())
        if self.signal:
            self.plot_signal()

    def plot_signal(self, name="X", color="red"):
        print("Generator.plot_signal()")
        if self.signal and len(self.signal) > 1:
            w, h = self.width, self.height
            if self.screen.find_withtag(name):
                self.screen.delete(name)
            plots = [(x*w, (h/self.units)*y+h/2) for (x, y) in self.signal]
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
        self.scaleA.pack()


if __name__ == "__main__":
    root = tk.Tk()
    mw = Generator(root)
    mw.create_grid(8)
    mw.layout()
    mw.generate()
    mw.update()
    root.mainloop()
