# coding: utf-8
from view import View
from generator import Generator
from math import pi, sin, radians
import sys
import math
import json
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
    signal_type = 20
    def __init__(self, model, model_y, view, mode):
        self.mode = mode
        self.model_y = model_y
        self.model_x = model
        self.model = None
        self.view = view
        self.name = "control"
        self.actions_binding()

    def actions_binding(self):

        self.view.screen.bind("<Configure>", self.view.resize)
        self.view.scaleA.bind("<B1-Motion>", self.on_magnitude_action)
        self.view.scaleF.bind("<B1-Motion>", self.on_frequence_action)
        self.view.scaleP.bind("<B1-Motion>", self.on_phasis_action)
        self.view.scale_sample.bind("<B1-Motion>", self.on_sample_action)
        self.view.scaleHarmic.bind("<B1-Motion>", self.on_harmonic_action)
        self.view.pair_harmonic.bind(
            "<Button-1>", self.on_pairharmonic_action)
        self.view.impair_harmonic.bind(
            "<Button-1>", self.on_impairharmonic_action)
        self.view.all_harmonic.bind(
            "<Button-1>", self.on_allharmonic_action)
        self.view.signal_x.bind(
            "<Button-1>", self.on_signal_x_action)
        self.view.signal_y.bind(
            "<Button-1>", self.on_signal_y_action)
        self.view.signal_xy.bind(
            "<Button-1>", self.on_signal_xy_action)
        self.view.file_menu.add_command(label="Open",
                                        command=self.open_file)

        self.view.file_menu.add_command(label="Save",
                                        command=self.save_file)
        self.view.file_menu.add_separator()
        self.view.file_menu.add_command(label="Exit",
                                        command=self.exit)

        self.view.edit_menu.add_command(label="About Us",
                                        command=self.about_us)
        self.view.edit_menu.add_command(label="About Tk",
                                        command=self.about_tk)
        self.view.edit_menu.add_command(label="About Python ",
                                        command=self.about_python)

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

        if self.view.harmonic_type_var.get() == 1:
            self.model.pair = True
            self.model.impair = False
            self.model.generate()
        else:
            pass

    def on_impairharmonic_action(self, event):

        if self.view.harmonic_type_var.get() == 2:

            self.model.pair = False
            self.model.impair = True
            self.model.generate()
        else:
            pass

    def on_allharmonic_action(self, event):

        if self.view.harmonic_type_var.get() == 3:
            print(self.model.name)

            self.model.pair = True
            self.model.impair = True
            self.model.generate()
        else:
            pass

    def on_sample_action(self, event):
        self.model.samples = self.view.n_sample.get()
        self.model.generate()

    def open_file(self):
        formats = [("Json", "*.json")]
        filename = filedialog.askopenfilename(
            parent=self.view.parent, filetypes=formats, title="Open..."
        )
        if len(filename) > 0:
            file = open(filename, "r")
            signal_params = json.load(file)
            file.close()
            self.view.var_mag.set(signal_params["mag"])
            self.view.var_freq.set(signal_params["freq"])
            self.view.var_p.set(signal_params["pha"])
            self.view.var_harmonic.set(signal_params["har"])
            self.model.pair = signal_params["harPair"]
            self.model.impair = signal_params["harOdd"]
            if self.model.pair and self.model.impair:
                self.view.harmonic_type_var.set(3)
            elif self.model.pair and not self.model.impair:
                self.view.harmonic_type_var.set(1)
            else:
                self.view.harmonic_type_var.set(2)
            self.model.m = self.view.var_mag.get()
            self.model.f = self.view.var_freq.get()
            self.model.p = self.view.var_p.get()
            self.model.harmonics = self.view.var_harmonic.get()
            self.model.generate()

    def save_file(self):
        formats = [("Json", "*.json")]
        filename = filedialog.asksaveasfilename(
            parent=self.view.parent, filetypes=formats, title="Save..."
        )
        if len(filename) > 0:
            dictionnary = {
                "mag": str(self.view.var_mag.get()),
                "freq": str(self.view.var_freq.get()),
                "pha": str(self.view.var_p.get()),
                "har": str(self.view.var_harmonic.get()),
                "harPair": self.model.pair,
                "harOdd": self.model.impair,
                "samples": str(self.model.samples),

            }
            json.dump(dictionnary, open(filename, "w"))

    def close_message_box(self):
        result_askquestion = tk.messagebox.askyesno(
            "Exit", "Are you sure you want to exit?", icon="warning"
        )
        if result_askquestion == "yes":
            print("See you soon!")
            self.close_app()
        else:
            print("Exit cancelled.")

    def exit(self):
        sure = tk.messagebox.askyesno("Exit", "Are you sure you want to exit?",
                                      parent=self.view.parent)
        if sure == True:
            self.view.parent.destroy()

    def about_us(self):
        print("about_us")
        tk.messagebox.showinfo(
            title="About us",
            message="BAGUIAN Harouna\
                HUYNH Ashley",
        )

    def about_tk(self):
        print("about_tk %s" % "Informations TkInter")
        tk.messagebox.showinfo(
            title="About tk",
            message="tkinter, je n'aime pas trop",
        )

    def about_python(self):
        print("about_py %s" % "Informations Python")
        tk.messagebox.showinfo(
            title="About py",
            message="Développé avec :\n\nVisual Studio Code v1.75.1\nPython v3.10.4\n",
        )

    def on_signal_x_action(self, event):
        print(self.view.model_var.get())
        self.signal_type = self.view.model_var.get()
        self.set_model()

    def on_signal_y_action(self, event):
        print(self.view.model_var.get())
        self.signal_type = self.view.model_var.get()
        self.set_model()
        
        

    def on_signal_xy_action(self, event):
        print(self.view.model_var.get())
        self.signal_type = self.view.model_var.get()
        self.set_model()
    
    def set_model(self):
        if self.signal_type == 10:
            self.model = self.model_x
            self.model.generate()
        elif self.signal_type == 20:
            self.model = self.model_y
            self.model.generate()
        elif self.signal_type==30:
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
