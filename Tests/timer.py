# coding: utf-8
import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 :
    import tkinter as tk
    from tkinter import filedialog
else :
    print("Your python version is : ",major,minor)
    print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

# https://riptutorial.com/tkinter/example/22870/-after--

class Timer:
    def __init__(self,parent):
        self.seconds=0
        self.label=tk.Label(parent,text="0 s",font="Arial 30",width=10)
        self.label.pack()
        self.label.after(1000, self.refresh_label)

    def refresh_label(self):
        self.seconds += 1
        self.label.configure(text="%i s" % self.seconds)
        self.label.after(1000, self.refresh_label)

#    def refresh_label(self,seconds=0):
#         self.label.configure(text="%i s" % seconds)
#         self.label.after(1000, self.refresh_label,seconds+1)

if __name__ == "__main__":
    mw=tk.Tk()
    timer=Timer(mw)
    mw.mainloop()

