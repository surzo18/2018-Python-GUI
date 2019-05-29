from tkinter import * 

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.fr = Frame(master)
        self.header = Label(self.fr, text="Konec") 
        self.fr.pack()
        self.header.pack(fill="BOTH",)

myApp = App()
myApp.master.title("Q Rovnice") 
myApp.mainloop()