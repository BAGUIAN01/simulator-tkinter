from tkinter  import Tk,Label,Button

class MainWindow :
    def __init__(self,parent) :
        self.parent=parent
        self.gui()
        self.actions_binding()

    def gui(self) :
        self.hello=Label(self.parent, text="Hello World !",fg="blue")
        self.btn=Button(self.parent, text="1", fg="red")

    def actions_binding(self) :
        nb_button=self.btn.cget("text")
        print("actions_binding(self)",nb_button)

        self.btn.bind("<Button-1>",self.on_keypad_action_1(nb_button))
        self.btn.bind("<Button-1>",self.on_keypad_action_2)
        self.btn.bind("<Button-1>",lambda event,nb_button=nb_button : self.on_keypad_action_3(event,nb_button))

    def on_keypad_action_1(self,nb_button) :
        print("on_keypad_action_1(self,nb_button) :",nb_button)

    def on_keypad_action_2(self,event) :
        print("on_keypad_action(self,event)",event)
        nb_button=event.widget.cget("text")
        print("button : ",nb_button)
        nb_button=event.widget.configure(text="9")

    def on_keypad_action_3(self,event,nb_button) :
        print("on_keypad_action(self,event,nb_button)",nb_button)
        print("(x,y) in button :",event.x,event.x)
        print("(x,y) on screen",event.x_root,event.x_root)


    def layout(self) :
        self.hello.pack()
        self.btn.pack()

if __name__ =="__main__" :
    root=Tk()
    mw=MainWindow(root)
    mw.layout()
    root.mainloop()
