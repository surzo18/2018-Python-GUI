from tkinter import *
from tkinter import tix
import MultiListbox as table
from tkinter import ttk  
from tkinter import messagebox
balik = [
       ["Doporučený list", "dl"],
       ["Poistený list", "pl"],
       ["Úradná zásielka", "uz"],
       ["balíček", "bč"],
       ["balík", "bk"],
       ["expres kuriér", "ek"],
       ["ems zásielka", "ez"],
       
       
       ]
class App(object):
    def __init__(self, master):
        root.title('Slovenská pošta')
        self.cena = 1.5
        self.menubar= Menu(master)
        self.filemenu= Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="About", command=self.about)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit", command=master.quit)
        self.menubar.add_cascade(label="Súbor", menu=self.filemenu)
        self.editmenu= Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Zmeň veľkosť", command=self.about)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        master.title("Menu1")
        master.config(menu=self.menubar)
        
        self.menoV = StringVar()
        self.priezviskoV = StringVar()
        self.pscV = StringVar()
        self.ulicaV = StringVar()
        self.statV = StringVar()
        self.mestoV = StringVar()
        
        self.menoVP = StringVar()
        self.priezviskoVP = StringVar()
        self.pscVP = StringVar()
        self.ulicaVP = StringVar()
        self.statVP = StringVar()
        self.mestoVP = StringVar()
      
        self.nb = ttk.Notebook(master)
        self.mframe = Frame(self.nb)
        self.mframe2 = Frame(self.nb)
        self.nb.add(self.mframe, text="Odosieľateľ")
        self.nb.add(self.mframe2, text="Príjmateľ")
        self.nb.pack(expand=1, fill=BOTH)
        
        
        ##odosielateľ
        self.editframe=LabelFrame(self.mframe, text="Editácia údajov odosielateľa")
        self.editframe.pack(padx=5, pady=5,fill=BOTH,expand=1, side=LEFT)

        self.savedframe=LabelFrame(self.mframe, text="Uložené údaje odosielateľa")
        self.savedframe.pack(padx=5,pady=5,fill=BOTH,side=RIGHT,expand=1)
        
        self.meno = Label(self.editframe, text='Meno :')
        self.meno.grid(row=0, column=0, padx=4, pady=4)
        self.menoE = Entry(self.editframe)
        self.menoE.grid(row=0, column=1, padx=4, pady=4)
        
        self.priezvisko = Label(self.editframe, text='Priezvisko :')
        self.priezvisko.grid(row=2, column=0, padx=4, pady=4)
        self.priezviskoE = Entry(self.editframe)
        self.priezviskoE.grid(row=2, column=1, padx=4, pady=4)
        
        self.ulica = Label(self.editframe, text='Ulica :')
        self.ulica.grid(row=4, column=0, padx=4, pady=4)
        self.ulicaE = Entry(self.editframe)
        self.ulicaE.grid(row=4, column=1, padx=4, pady=4)
        
        self.psc = Label(self.editframe, text='PSČ :')
        self.psc.grid(row=4, column=3, padx=4, pady=4)
        self.pscE = Entry(self.editframe)
        self.pscE.grid(row=4, column=4, padx=4, pady=4)
        
        self.mesto = Label(self.editframe, text="Mesto :")
        self.mesto.grid(row=6, column=0,padx=4, pady=4)
        self.mestoE = Entry(self.editframe)
        self.mestoE.grid(row=6, column=1, padx=4, pady=4)
        
        self.stat = Label(self.editframe, text="Štát :")
        self.stat.grid(row=8, column=0,padx=4, pady=4)
        self.statE = Entry(self.editframe)
        self.statE.grid(row=8, column=1, padx=4, pady=4)
        
        self.saveB = Button(self.editframe,text="Uložiť: ",command=self.save)
        self.saveB.grid(row=10,column=0)
        
        self.meno2 = Label(self.savedframe, text='Meno :')
        self.meno2.grid(row=0, column=0, padx=4, pady=4)
        self.priezvisko2 = Label(self.savedframe, text='Priezvisko :')
        self.priezvisko2.grid(row=2, column=0, padx=4, pady=4)
        self.ulica2 = Label(self.savedframe, text='Ulica :')
        self.ulica2.grid(row=4, column=0, padx=4, pady=4)
        self.psc2 = Label(self.savedframe, text='PSČ :')
        self.psc2.grid(row=4, column=2, padx=4, pady=4)
        self.mesto2 = Label(self.savedframe, text='Mesto :')
        self.mesto2.grid(row=6, column=0, padx=4, pady=4)
        self.stat2 = Label(self.savedframe, text="Štát :")
        self.stat2.grid(row=8, column=0, padx=4, pady=4)
        
        ## frame2
        
         ##odosielateľ
        self.editframeP=LabelFrame(self.mframe2, text="Editácia údajov Príjmateľa")
        self.editframeP.pack(padx=5, pady=5,fill=BOTH,expand=1, side=LEFT)

        self.savedframeP=LabelFrame(self.mframe2, text="Uložené údaje Príjmateľa")
        self.savedframeP.pack(padx=5,pady=5,fill=BOTH,side=RIGHT,expand=1)
        
        self.menoP = Label(self.editframeP, text='Meno :')
        self.menoP.grid(row=0, column=0, padx=4, pady=4)
        self.menoEP= Entry(self.editframeP)
        self.menoEP.grid(row=0, column=1, padx=4, pady=4)
        
        self.priezviskoP = Label(self.editframeP, text='Priezvisko :')
        self.priezviskoP.grid(row=2, column=0, padx=4, pady=4)
        self.priezviskoEP = Entry(self.editframeP)
        self.priezviskoEP.grid(row=2, column=1, padx=4, pady=4)
        
        self.ulicaP = Label(self.editframeP, text='Ulica :')
        self.ulicaP.grid(row=4, column=0, padx=4, pady=4)
        self.ulicaEP = Entry(self.editframeP)
        self.ulicaEP.grid(row=4, column=1, padx=4, pady=4)
        
        self.pscP = Label(self.editframeP, text='PSČ :')
        self.pscP.grid(row=4, column=3, padx=4, pady=4)
        self.pscEP = Entry(self.editframeP)
        self.pscEP.grid(row=4, column=4, padx=4, pady=4)
        
        self.mestoP = Label(self.editframeP, text="Mesto :")
        self.mestoP.grid(row=6, column=0,padx=4, pady=4)
        self.mestoEP = Entry(self.editframeP)
        self.mestoEP.grid(row=6, column=1, padx=4, pady=4)
        
        self.statP = Label(self.editframeP, text="Štát :")
        self.statP.grid(row=8, column=0,padx=4, pady=4)
        self.statEP = Entry(self.editframeP)
        self.statEP.grid(row=8, column=1, padx=4, pady=4)
        
        self.saveBP = Button(self.editframeP,text="Uložiť: ",command=self.saveP)
        self.saveBP.grid(row=10,column=0)
        
        self.meno2P = Label(self.savedframeP, text='Meno :')
        self.meno2P.grid(row=0, column=0, padx=4, pady=4)
        self.priezvisko2P = Label(self.savedframeP, text='Priezvisko :')
        self.priezvisko2P.grid(row=2, column=0, padx=4, pady=4)
        self.ulica2P = Label(self.savedframeP, text='Ulica :')
        self.ulica2P.grid(row=4, column=0, padx=4, pady=4)
        self.psc2P = Label(self.savedframeP, text='PSČ :')
        self.psc2P.grid(row=4, column=2, padx=4, pady=4)
        self.mesto2P = Label(self.savedframeP, text='Mesto :')
        self.mesto2P.grid(row=6, column=0, padx=4, pady=4)
        self.stat2P = Label(self.savedframeP, text="Štát :")
        self.stat2P.grid(row=8, column=0, padx=4, pady=4)
        
        ##
        self.sluzby=LabelFrame(master, text="Dodatočné služby")
        self.sluzby.pack(padx=5, pady=5,fill=BOTH,expand=1, side=TOP)
        
        self.var1 = IntVar()
        self.lab1=Label(self.sluzby, text="1. trieda").grid(row=0, column=0)
        self.c1 = Checkbutton(self.sluzby, variable=self.var1).grid(row=0, column=2)
        
        self.var2 = IntVar()
        self.lab2=Label(self.sluzby, text="Doručenka").grid(row=2, column=0)
        self.c2 = Checkbutton(self.sluzby, variable=self.var2).grid(row=2, column=2)
        
        self.var3 = IntVar()
        self.lab3=Label(self.sluzby, text="Nevrátiť").grid(row=4, column=0)
        self.c3 = Checkbutton(self.sluzby, variable=self.var3) .grid(row=4, column=2)
         
        self.var4 = IntVar()
        self.lab4=Label(self.sluzby, text="Nedoposielať").grid(row=6, column=0)
        self.c4 = Checkbutton(self.sluzby, variable=self.var4).grid(row=6, column=2)
         
        self.var5 = IntVar()
        self.lab5=Label(self.sluzby, text="Neukladať")
        self.lab5.grid(row=8, column=0)
        self.c5 = Checkbutton(self.sluzby, variable=self.var5).grid(row=8, column=2)
        
        self.var6 = IntVar()
        self.lab6=Label(self.sluzby, text="Do vlastných rúk").grid(row=0, column=4)
        self.c6 = Checkbutton(self.sluzby, variable=self.var6).grid(row=0, column=6)
         
        self.var7 = IntVar()
        self.lab7=Label(self.sluzby, text="Slepecká zásielka").grid(row=2, column=4)
        self.c7 = Checkbutton(self.sluzby, variable=self.var7).grid(row=2, column=6)
        
        self.prepocitat= Button(self.sluzby,text="Prepočítať: ",command=self.price)
        self.prepocitat.grid(row=10,column=0)
        
        self.mlb1 = table.MultiListbox(master, (('Produkt', 20), ('kód', 20)))
        for i in range(len(balik)):
            self.mlb1.insert(END, (balik[i][0], balik[i][1]))
        self.mlb1.pack(expand=YES,fill=BOTH, padx=10, pady=10)
        self.mlb1.subscribe( lambda row: self.savechoice( row ) )
        
        self.finalframe=LabelFrame(master, text="Finálna suma za dobierku")
        self.finalframe.pack(padx=5, pady=5,fill=BOTH,expand=1, side=RIGHT)
        self.priceL=Label(self.finalframe, text="Výsledná suma je: ").grid(row=2, column=0)  
        self.aktualizuj = Button(self.finalframe,text="Zisti aktuálnu cenu", command=self.aktualizacia).grid(row=2, column=2)                    
    
        
        self.nb2 = ttk.Notebook(master)
        self.bframe = Frame(self.nb2)
        self.infoframe = Frame(self.nb2)
        self.dframe = Frame(self.nb2)
        self.nb2.add(self.bframe, text="Balík")
        self.nb2.add(self.dframe, text="Dobierka")
        self.nb2.add(self.infoframe, text="Poznámka")
        self.nb2.pack(expand=1, fill=BOTH)
        
        self.balab1=Label(self.bframe, text="Hmotnosť:").grid(row=0, column=0)
        self.balab2=Label(self.bframe, text="Šírka:").grid(row=2, column=0)
        self.balab1=Label(self.bframe, text="Výška:").grid(row=4, column=0)
        self.balab1=Label(self.bframe, text="Dĺžka:").grid(row=6, column=0)
        self.lab1E = Entry(self.bframe).grid(row=0, column=1, padx=4, pady=4)
        self.lab2E = Entry(self.bframe).grid(row=2, column=1, padx=4, pady=4)
        self.lab3E = Entry(self.bframe).grid(row=4, column=1, padx=4, pady=4)
        self.lab4E = Entry(self.bframe).grid(row=6, column=1, padx=4, pady=4)
        self.jednotka1=Label(self.bframe, text="kg").grid(row=0, column=2)
        self.jednotka2=Label(self.bframe, text="cm").grid(row=2, column=2)
        self.jednotka3=Label(self.bframe, text="cm").grid(row=4, column=2)
        self.jednotka4=Label(self.bframe, text="cm").grid(row=6, column=2)
        
        self.AA=StringVar()
        self.x2=Radiobutton(self.dframe, text="Na adresu", variable=self.AA, value="Adresa").grid(row=0,column=0)
        self.x2=Radiobutton(self.dframe, text="Na účet", variable=self.AA, value="Ucet").grid(row=0,column=1)

        self.lab1D=Label(self.dframe, text="IBAN").grid(row=2, column=0)
        self.lab1D=Label(self.dframe, text="Variabilný symbol").grid(row=4, column=0)
        self.lab1D=Label(self.dframe, text="Suma").grid(row=6, column=0)
        self.lab1D = Entry(self.dframe).grid(row=2, column=1, padx=4, pady=4)
        self.lab2D = Entry(self.dframe).grid(row=4, column=1, padx=4, pady=4)
        self.lab3D = Entry(self.dframe).grid(row=6, column=1, padx=4, pady=4)
        
        self.send = Button(self.infoframe,text="Send")
        self.send.grid(row=0,column=0)
        input_text_area = Text(self.infoframe)
        input_text_area.grid(row=1, column=0, sticky=W+E)
        input_text_area.configure(background='#00FFFF')
        
        
    def save(self):
        self.menoV=self.menoE.get()
        self.priezviskoV=self.priezviskoE.get()
        self.ulicaV=self.ulicaE.get()
        self.pscV=self.pscE.get()
        self.mestoV=self.mestoE.get()
        self.statV=self.statE.get()
        print("ulozene!")
        messagebox.showinfo("uložené","Záznam bol uložený!")
        self.meno2L = Label(self.savedframe, text=self.menoV)
        self.meno2L.grid(row=0, column=1, padx=4, pady=4)
        self.priezvisko2L = Label(self.savedframe, text=self.priezviskoV)
        self.priezvisko2L.grid(row=2, column=1, padx=4, pady=4)
        self.ulica2L = Label(self.savedframe, text=self.ulicaV)
        self.ulica2L.grid(row=4, column=1, padx=4, pady=4)
        self.psc2L = Label(self.savedframe, text=self.pscV)
        self.psc2L.grid(row=4, column=3, padx=4, pady=4)
        self.mesto2L = Label(self.savedframe, text=self.mestoV)
        self.mesto2L.grid(row=6, column=1, padx=4, pady=4)
        self.stat2L = Label(self.savedframe, text=self.statV)
        self.stat2L.grid(row=8, column=1, padx=4, pady=4)
        
    def saveP(self):
        self.menoVP=self.menoEP.get()
        self.priezviskoVP=self.priezviskoEP.get()
        self.ulicaVP=self.ulicaEP.get()
        self.pscVP=self.pscEP.get()
        self.mestoVP=self.mestoEP.get()
        self.statVP=self.statEP.get()
        print("ulozene!")
        messagebox.showinfo("uložené","Záznam bol uložený!")
        self.meno2LP = Label(self.savedframeP, text=self.menoVP)
        self.meno2LP.grid(row=0, column=1, padx=4, pady=4)
        self.priezvisko2LP = Label(self.savedframeP, text=self.priezviskoVP)
        self.priezvisko2LP.grid(row=2, column=1, padx=4, pady=4)
        self.ulica2LP = Label(self.savedframeP, text=self.ulicaVP)
        self.ulica2LP.grid(row=4, column=1, padx=4, pady=4)
        self.psc2LP = Label(self.savedframeP, text=self.pscVP)
        self.psc2LP.grid(row=4, column=3, padx=4, pady=4)
        self.mesto2LP = Label(self.savedframeP, text=self.mestoVP)
        self.mesto2LP.grid(row=6, column=1, padx=4, pady=4)
        self.stat2LP = Label(self.savedframeP, text=self.statVP)
        self.stat2LP.grid(row=8, column=1, padx=4, pady=4)
        
        
    def price(self):
        if self.var1.get() == 1:
            self.cena += 0.50
        if self.var2.get() == 1:
            self.cena += 0.20
        if self.var3.get() == 1:
            self.cena += 0.50
        if self.var4.get() == 1:
            self.cena += 0.20
        if self.var5.get() == 1:
            self.cena += 0.50
        if self.var6.get() == 1:
            self.cena += 0.30
        if self.var7.get() == 1:
            self.cena += 0.10
        print(self.cena)
        
    def savechoice(self, row):
        pass
    def aktualizacia(self):
        self.a = Label(self.finalframe, text=self.cena).grid(row=2, column=1)
    def about(self):
        messagebox.showinfo("NADPIS","Tento program napísal JAN0673")

root = tix.Tk()
root.wm_title("pošta")
app = App(root)
root.mainloop()

