from tkinter import * 
from tkinter import Tk, StringVar, ttk

class App(Frame):
#Window manažeru
    def __init__(self, master):
        #Vytvorený hlavný frame
        self.fr = Frame(master)
        self.fr.pack(fill=BOTH)

        #Vytvorené menšie framy jeden horny a jeden dolný vo vnútry veľkého
        ##################
        #     Horný      #
        #     Header     #
        ##################
        #     Dolné      #
        #     Body       #
        ##################
        self.header = Frame(self.fr, relief=GROOVE)
        self.body   = Frame(self.fr, bg="black")
        self.header.pack(fill=BOTH,expand=1, side="top")
        self.body.pack(fill=BOTH,expand=1,side="top")

        #Horné tlačítka
        self.title = Label(self.header, text="Redakcny System", relief=GROOVE)
        self.login = Button(self.header, text="Login", command=self.fr.quit) 
        self.logout = Button(self.header, text="Logout", command=self.fr.quit) 
        self.title.pack(side=LEFT)
        self.login.pack(side=RIGHT, padx=4)
        self.logout.pack(side=RIGHT)

        #Spodné Vľavo
        self.left = Frame(self.body)
        self.body.pack(fill=Y,expand=1,side="left")

        #Spodné Vpravo
        self.right = Frame(self.body)
        self.body.pack(fill=Y,expand=1,side="left")

#Beh programu
if __name__ == '__main__':
    root = Tk()
    app = App(root)

#Nastaví titulok framu
root.title("Redaction System")

#Nastaví maxSize a minSize
root.maxsize(1000, 400)
root.minsize(500, 200)

#Zapne smyčku MENU
root.mainloop()




