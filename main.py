# coding: utf-8
import io
from PIL import Image,  ImageGrab
import json
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


def menubar(view, model):

    menubar = tk.Menu(view.parent)
    view.parent.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)

    edit_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=edit_menu)

    file_menu.add_command(label="Open",
                          command=open_file)

    file_menu.add_command(label="Save",
                          command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Save Png",
                          command=save_png)

    file_menu.add_separator()
    file_menu.add_command(label="Exit",
                          command=exit)

    edit_menu.add_command(label="About Us",
                          command=about_us)
    edit_menu.add_command(label="About Tk",
                          command=about_tk)
    edit_menu.add_command(label="About Python ",
                          command=about_python)


def save_png():
    formats = [("*.png", "*.jpg")]
    filename = filedialog.asksaveasfilename(
        parent=view.parent, filetypes=formats, title="Saving..."
    )
    if not filename.endswith(".png") and not filename.endswith(".jpg"):
        filename += ".png"
    x = view.parent.winfo_rootx() + view.screen.winfo_x()
    y = view.parent.winfo_rooty() + view.screen.winfo_y()

    bbox = view.screen.bbox("all")
    x1, y1, x2, y2 = bbox

    width = x2 - x1
    height = y2 - y1

    x_left = x + x1
    y_top = y + y1
    x_right = x + x2
    y_bottom = y + y2
    ImageGrab.grab().crop((x_left, y_top, x_right, y_bottom)).save(filename)


def open_file():
    formats = [("Json", "*.json")]
    filename = filedialog.askopenfilename(
        parent=view.parent, filetypes=formats, title="Open..."
    )
    if len(filename) > 0:
        file = open(filename, "r")
        signal_params = json.load(file)
        file.close()
        control_x.var_mag.set(signal_params["mag"])
        control_x.var_freq.set(signal_params["freq"])
        control_x.var_p.set(signal_params["pha"])
        control_x.var_harmonic.set(signal_params["har"])
        model_x.pair = signal_params["harPair"]
        model_x.impair = signal_params["harOdd"]
        if model_x.pair and model_x.impair:
            control_x.harmonic_type_var.set(3)
        elif model_x.pair and not model_x.impair:
            control_x.harmonic_type_var.set(1)
        else:
            control_x.harmonic_type_var.set(2)
        model_x.m = control_x.var_mag.get()
        model_x.f = control_x.var_freq.get()
        model_x.p = control_x.var_p.get()
        model_x.harmonics = control_x.var_harmonic.get()
        model_x.generate()


def save_file():
    formats = [("Json", "*.json")]
    filename = filedialog.asksaveasfilename(
        parent=view.parent, filetypes=formats, title="Save..."
    )
    if len(filename) > 0:
        dictionnary = {
            "mag": str(control_x.var_mag.get()),
            "freq": str(control_x.var_freq.get()),
            "pha": str(control_x.var_p.get()),
            "har": str(control_x.var_harmonic.get()),
            "harPair": model_x.pair,
            "harOdd": model_x.impair,
            "samples": str(model_x.samples),

        }
        json.dump(dictionnary, open(filename, "w"))


def close_message_box():
    result_askquestion = tk.messagebox.askyesno(
        "Exit", "Are you sure you want to exit?", icon="warning"
    )
    if result_askquestion == "yes":
        print("See you soon!")
        view.parent.destroy()
    else:
        print("Exit cancelled.")


def exit():
    sure = tk.messagebox.askyesno("Exit", "Are you sure you want to exit?",
                                  parent=view.parent)
    if sure == True:
        view.parent.destroy()


def about_us():
    print("about_us")
    tk.messagebox.showinfo(
        title="About us",
        message="BAGUIAN Harouna\
            HUYNH Ashley",
    )


def about_tk():
    print("about_tk %s" % "Informations TkInter")
    tk.messagebox.showinfo(
        title="About tk",
        message="tkinter, je n'aime pas trop",
    )


def about_python():
    print("about_py %s" % "Informations Python")
    tk.messagebox.showinfo(
        title="About py",
        message="Développé avec vs code",
    )


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background="black")
    root.title("Simulateur")
    # root.option_readfile("oscillo.opt")

    view = View(root)

    model_x = Generator()
    model_y = Generator()
    view.create_grid(8)
    # view.layout()

    model_x.attach(view)
    model_x.generate()
    model_y.attach(view)
    model_y.generate()

    control_x = Controller(model=model_x, view=view)
    menubar(view, model_x)
    control_y = Controller(model=model_y, view=view)
    # control.layout()
    root.mainloop()
