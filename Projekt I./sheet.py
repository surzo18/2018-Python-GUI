from tkinter import * 

class App(Frame):
#Window manažeru
    def __init__(self, master):
        Frame.__init__(self, master=None)
        self.fr = Frame(master)
        self.bu = Button(self.fr, text="Konec", command=self.fr.quit) 
        self.fr.master.title("Button1")
        self.fr.pack()
        self.bu.pack()
        self.bua = Button(master, text="Tlacitko1", command=self.fr.quit) 
        self.bub = Button(master, text="Tlacitko2", command=self.fr.quit) 
        self.buc = Button(master, text="Tlacitko3", command=self.fr.quit) 
        self.bud = Button(master, text="Tlacitko4", command=self.fr.quit)
        self.bua.pack(fill=BOTH, expand=1)        
        self.bub.pack() 
        self.buc.pack()
        self.bud.pack()
        self.bu = Button(master, text="Konec", command=self.quit) 
        self.bu.pack()
        
# create the application 
root = Tk()
myapp = App(root)
# here are method calls to the window manager class 
root.title("My Application") 
root.maxsize(1000, 400)
root.minsize(500, 200)
# start the program 
myapp.mainloop()