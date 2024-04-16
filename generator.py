# coding: utf-8
from observer import Subject
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


class Generator(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.signal = []
        self.m, self.f, self.p = 1.0, 2.0, 0.0
        self.harmonics = 1
        self.samples = 100
        self.units = 1
        self.name = "model"

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
        self.notify()
        return self.signal


if __name__ == "__main__":
    model = Generator()
    print(model)
   

