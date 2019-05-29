# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------#
# Pouziti Combobox                                                      Nemec  #
#------------------------------------------------------------------------------#
from tkinter import *
from tkinter import Tk, StringVar, ttk


class myApp:

  def fce(self, var):
    self.la.configure(text=var.widget.get())
    
  def __init__(self, parent):
    self.parent=parent
    self.la = Label(self.parent, text="Combobox", foreground="red")
    self.la.pack()
    self.prom = StringVar(self.parent)
    
    self.box_value = StringVar()
    self.box = ttk.Combobox(self.parent, textvariable=self.box_value, state='readonly')
    self.box.bind("<<ComboboxSelected>>", self.fce)
    self.box.pack()
    self.box['values'] = ('A', 'B', 'C')
    self.box.current(0)



if __name__ == '__main__':
    root = Tk()
    app = myApp(root)
    root.mainloop()

#------------------------------------------------------------------------------#



