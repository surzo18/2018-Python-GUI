from tkinter import *
from tkinter import Tk, StringVar, ttk

class myApp(Frame):
  def __init__(self, master):
    self.fr = Frame(master)
    
    self.inputs = Frame()

    self.inputA = Label(self.fr, text="Strana a")
    self.A = Entry(self.fr)
    self.inputB = Label(self.fr, text="Strana b")
    self.B = Entry(self.fr)    
    self.inputC = Label(self.fr, text="Strana c")
    self.C = Entry(self.fr)
    
    self.count =Button(self.fr, text="Vypočítaj")
    self.delete =Button(self.fr, text="Zmazať")
    self.end =Button(self.fr, text="Konec")

    self.label = Label(self.fr, text="Vysledok:")

    self.fr.pack(expand=1)
    
    self.inputA.pack(side="bottom")
    self.A.pack(side="bottom")
    
    self.inputB.pack(side="left")
    self.B.pack(side="left")

    self.inputC.pack(side="left")
    self.C.pack(side="left")

    self.count.pack(side="left")
    self.delete.pack(side="left")
    self.end.pack(side="left")

    self.label.pack(side="left")

root = Tk()
app = myApp(root)
root.mainloop()
