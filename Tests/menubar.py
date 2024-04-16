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
    def __init__(self,parent=None):
        tk.Frame.__init__(self, borderwidth=2)
        if parent :
            self.parent=parent
            menu = tk.Menu(parent)
            parent.config(menu=menu)
            fileMenu = tk.Menu(menu)
            fileMenu.add_command(label="Save",command=self.save)
            fileMenu.add_command(label="Exit", command=self.close_app)
            menu.add_cascade(label="File", menu=fileMenu)
 
            fileMenu = tk.Menu(menu)
            fileMenu.add_command(label="About Us ...",command=self.about_us)
            menu.add_cascade(label="Help", menu=fileMenu)

    def save(self):
        formats=[('Texte','*.py'),('Portable Network Graphics','*.png')]
        filename=filedialog.asksaveasfilename(parent=self,filetypes=formats,title="Save...")
        if len(filename) > 0:
            print("Sauvegarde en cours dans %s" % filename)

    def close_app(self):
        exit()

    def about_us(self):
        print("about_us %s" % "Nom-Prenom")
        
if __name__ == "__main__" :
    mw = tk.Tk()
    app = Menubar(mw)
    mw.wm_title("Tkinter : Menubar")
    mw.mainloop()

