## https://infoforall.fr/python/python-act140.html
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import random

class Pacman :
    def __init__(self,parent,name="pacman",size=150,color="yellow"):
        self.parent=parent
        self.name=name
        width,height=int(self.parent.cget("width")),int(self.parent.cget("height"))
        position=random.randint(0,width//2),random.randint(0,height//2)
        self.speed_x,self.speed_y=10,0
        self.animation_active,self.stop_animation = False, False
        x,y=position
        # x,y=15,15
        self.pacman_id = self.parent.create_arc(x,y,x+size,y+size,fill=color,start=15,extent=330)

    def animate(self):
        # self.animation_active=True
        mod_angle = 0
        liste_coord = self.parent.coords(self.pacman_id)
        print("liste_coord",liste_coord)

        if liste_coord[2]>600 :   # right x limit 
            self.speed_x = -10
        elif liste_coord[0]<0 :   # left x limit 
            self.speed_x = 10
        if (self.speed_x <0) :
            mod_angle = 180
        if (self.parent.itemcget(self.pacman_id, 'start') == '15.0' or self.parent.itemcget(self.pacman_id, 'start') == '195.0') :
            self.parent.itemconfig(self.pacman_id, start=30+mod_angle, extent=300)
        else:
            self.parent.itemconfig(self.pacman_id, start=15+mod_angle, extent=330)
        self.parent.move(self.pacman_id,self.speed_x,0)
        if self.stop_animation == False :
            self.parent.master.after(100,self.animate) 
        else:
            self.stop_animation = False
            # self.animation_active = False

    def turn_right(self):
        self.stop_animation = False
        self.speed_x=10
        self.speed_y=0
        mod_angle=0
        self.parent.itemconfig(self.pacman_id, start=30+mod_angle, extent=300)

    def turn_left(self):
        self.stop_animation = False
        self.speed_x = -10
        self.speed_y = 0
        mod_angle=180
        self.parent.itemconfig(self.pacman_id, start=30+mod_angle, extent=300)

    def starting_point(self):
        self.speed_x = 0
        self.speed_y = 0
        self.stop()
        self.parent.coords(self.pacman_id,50,50,150,150)

    def stop(self):
        self.stop_animation = True

# ----------------------------------------------------------------
# Corps du programme
# ----------------------------------------------------------------

root=Tk()
root.title("Pacman")
root.geometry("600x400")
view=Canvas(root,width=500,height=200,bg='ivory', bd=0, highlightthickness=0)
model=Pacman(view,size=100,color="red")
controls=Frame(root)
animation_panel=LabelFrame(controls,text="Animation",bg='#777777')
animation_panel.pack(side="left")
Button(animation_panel, text="Move", fg="yellow", bg="black",command=model.animate).pack(side="left")
Button(animation_panel, text="Stop", fg="yellow", bg="red",command=model.stop).pack(side="left")
control_panel=LabelFrame(controls,text="Control",bg='#777777')
control_panel.pack(side="right")
Button(control_panel, text="=>", fg="yellow", bg="black",command=model.turn_right).pack(side="right")
Button(control_panel, text="<=", fg="yellow", bg="black",command=model.turn_left).pack(side="left")
model=Pacman(view,size=50)
view.pack(fill="both",expand=True)
controls.pack(fill="x",expand=True)
        # frame=tk.LabelFrame(self.parent,text="Harmonics")
        # self.radio_var=tk.IntVar()
        # btn=tk.Radiobutton(frame,text="All", variable=self.radio_var,value=1,command=self.cb_activate_button)
        # btn.select()
        # btn.pack(anchor ="w")
        # btn=tk.Radiobutton(frame,text="Odd", variable=self.radio_var,value=2,command=self.cb_activate_button)
        # btn.pack(anchor ="w")
        # frame.pack()
    # def cb_activate_button(self):
    #     print("You selected the option " + str(self.radio_var.get()))
    #     self.harmo_odd_even=self.radio_var.get()
root.mainloop()
