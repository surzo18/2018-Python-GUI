# -*- coding: utf-8 -*-

from tkinter import *
import tix
import MultiListbox as table


data = [
       ["Petr", "Bílý","045214/1512","17. Listopadu", 15, "Ostrava", 70800,"poznamka"],
       ["Jana", "Zelený","901121/7238","Vozovna", 54, "Poruba", 78511,""],
       ["Karel", "Modrý","800524/5417","Porubská", 7, "Praha", 11150,""],
       ["Martin", "Stříbrný","790407/3652","Sokolovská", 247, "Brno", 54788,"nic"]]


class App(object):
    def __init__(self, master):
        self.row = IntVar()
        self.row = None
        self.jmeno = StringVar()
        self.prijmeni = StringVar()
        self.rc = StringVar()
        self.ulice = StringVar()
        self.cp = StringVar()
        self.mesto = StringVar()
        self.psc = StringVar()


        self.mlb = table.MultiListbox(master, (('Jméno', 20), ('Příjmení', 20), ('Rodné číslo', 12)))
        for i in range(len(data)):
            self.mlb.insert(END, (data[i][0], data[i][1],data[i][2]))
        self.mlb.pack(expand=YES,fill=BOTH, padx=10, pady=10)
        self.mlb.subscribe( lambda row: self.edit( row ) )

      
    def edit(self, row):
        self.row=row
        print row
             

root = Tix.Tk()
root.wm_title("Formulář")
app = App(root)
root.mainloop()

