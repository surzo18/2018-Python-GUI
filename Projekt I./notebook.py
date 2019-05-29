#------------------------------------------------------------------------------#
# Notebook                                                              Nemec  #
#------------------------------------------------------------------------------#

from tkinter import *
from tkinter import Tk, StringVar, ttk


class myApp:
  def __init__(self, master):
    self.nb = ttk.Notebook(master, name='notebook')
    self.nb.enable_traversal()
    
    
    self.p1 = ttk.Frame(self.nb, name='description', padding=6)
    self.p2 = ttk.Frame(self.nb, name='poznamka', padding=6)
    
    self.nb.add(self.p1, text='Description', underline=0, padding=2)
    self.nb.add(self.p2, text='Poznamka', underline=0, padding=2)
    
    self.nb.pack(expand=1, fill=BOTH)
    
    #A1 
    self.la1 = Label(self.p1, text="Prvni okno")
    self.la1.pack()

    #B1
    self.la2 = Label(self.p2, text="Druhe okno")
    self.la2.pack()

root = Tk()
app = myApp(root)
root.mainloop()
root.destroy()
