import tkinter as tk
class Menubar(tk.Frame):
    
    def __init__(self, model, view, parent=None):
        tk.Frame.__init__(self, borderwidth=2)
        self.parent = parent
        self.view = view
        self.model = model
        
    