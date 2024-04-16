# -*- coding: utf-8 -*-
import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 and minor==6 :
    import tkinter as tk
    from tkinter import filedialog
else :
    import tkinter as tk
    from tkinter import filedialog 

class Menubar(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self,parent=None,borderwidth=2)
        self.parent=parent
        self.gui()

    def gui(self) : 
        self.menubar=tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        menu_file=tk.Menu(self.menubar)
        menu_file.add_command(label="Save", command=lambda item="Save" : self.file_actions(item))
        menu_file.add_command(label="Exit", command=lambda : self.file_actions("Exit"))
        self.menubar.add_cascade(label="File", menu=menu_file)
            
        menu_help = tk.Menu(self.menubar)
        menu_help.add_command(label="About Us ...",command=self.about_us)
        self.menubar.add_cascade(label="Help", menu=menu_help)

    def file_actions(self,item):
        print("Menubar.file_actions()")
        if  item=="Save" :
            print(item)
            self.action_save()
        elif item=="Exit" :
            print(item)
            self.parent.destroy()
        else :
            print(item)
    def action_save(self) :
        print("Menubar.action_save()")

    # def action_save(self) :
    #     for generator in self.parent.get_generators().values() :
    #          print("name : ",generator.get_name())
    #          print("Magnitude : ",generator.get_magnitude())
    #          print("Frequence : ",generator.get_frequency())
    #     return

    def about_us(self):
        print("Menubar.about_us()")

  
if __name__ == "__main__" :
    mw = tk.Tk()
    app = Menubar(mw)
    mw.wm_title("Tkinter : Menubar")
    mw.mainloop()

