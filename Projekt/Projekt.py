import MultiListbox as table
from tkinter import *
from tkinter import tix
from tkinter import messagebox

resolution=[
    ["Ján Novotný","novotný@gmail.com"],
    ["Marek Šutý","neuvedený"],
    ["Jacob Wild","wild@gmail.com"],
    ["Roman Šlacha","neuvedený"]
]

articles=[
    
    ["Toto je článok číslo 1","Marek Šutý","12/03/16","Zverejnený"],
    ["Toto je článok číslo 2","Jacob Wild","12/04/16","Čakajúci"],
    ["Náhodný nadpis","Marek Šutý","12/03/18","Zverejnený"],
    ["Videli ste Avangers END GAME?","Roman Šlachaý","12/03/18","Zrušený"]
]

class App(object):

    def __init__(self,root, *args, **kwargs,):
        # menu
        self.menu = Menu(root)
        
        self.filemenu = Menu(self.menu, tearoff=0)
        self.showmenu = Menu(self.menu, tearoff=0)
        self.settingmenu = Menu(self.menu, tearoff=0)
        self.helpmenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.menu.add_cascade(label="Display", menu=self.showmenu)
        self.menu.add_cascade(label="Options", menu=self.settingmenu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        
        self.filemenu.add_command(label="Login") 
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Import")
        self.filemenu.add_command(label="Export")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit")

        self.showmenu.add_command(label="Full screen")
        self.showmenu.add_command(label="Edit")
        self.showmenu.add_command(label="Tools")
        self.showmenu.add_command(label="Navigation")


        self.settingmenu.add_command(label="Toolbars")
        self.settingmenu.add_separator()
        self.settingmenu.add_command(label="Server")

        self.helpmenu.add_command(label="Find Action")
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="About", command=self.about)

        
        root.config(menu=self.menu)
        
        
        #NOTEBOOK

        self.note=tix.NoteBook(root)
        self.note.add("page1", label="Main")
        self.note.add("page2", label="Výpis")
        self.note.add("page3", label="Pridať")        

        self.p1=self.note.subwidget_list["page1"]
        self.p2=self.note.subwidget_list["page2"]
        self.p3=self.note.subwidget_list["page3"]
        
        self.note.pack(expand=1, fill=BOTH)
        
        self.bigFrame=Frame(self.p1, bg="Black")
        self.bigFrame.pack(fill=BOTH, expand=1,side=TOP)
        
        #doubleFrame2
        self.doubleFrame2=Frame(self.bigFrame)
        self.doubleFrame2.pack(padx=5, pady=5, fill=BOTH, expand=1,side=TOP)
        
        
        
        
         #page1
        self.profileF=LabelFrame(self.doubleFrame2, text="Profil")
        self.profileF.pack(padx=5, pady=5,fill=BOTH,expand=True, side=TOP)
        
        
        #Image
        self.image = Frame(self.profileF,bg="Gray",width=120, height=140).grid(row=0,column=0,columnspan=1,rowspan=3,padx=15,pady=(20,10))
           
        #ProfilePopis
        self.name=Label(self.profileF,text="Meno:",fg="red").grid(row=0,column=2,padx=8, pady=6,sticky=E);
        self.name=Label(self.profileF,text="Email:",fg="red").grid(row=1,column=2,padx=8, pady=6, sticky=E);
        self.name=Label(self.profileF,text="Dátum Narodenia:",fg="red").grid(row=2,column=2,padx=7, pady=6, sticky=E);
        self.name=Label(self.profileF,text="Pozícia:",fg="red").grid(row=3,column=2,padx=7, pady=6, sticky=E);
        
                
        self.name=Label(self.profileF,text="Jožko", font = ('Comic Sans MS',11)).grid(row=0,column=3,padx=8, pady=6, sticky=W);
        self.name=Label(self.profileF,text="jozef@gmail.com", font = ('Comic Sans MS',11)).grid(row=1,column=3,padx=8, pady=6, sticky=W);
        self.name=Label(self.profileF,text="12.apríla.1995", font = ('Comic Sans MS',11)).grid(row=2,column=3,padx=8, pady=6, sticky=W);
        self.name=Label(self.profileF,text="Redaktor", font = ('Comic Sans MS',11)).grid(row=3,column=3,padx=8, pady=6, sticky=W);
        
        self.name=Label(self.profileF,text="Priezvisko:",fg="red").grid(row=0,column=4,padx=8, pady=6, sticky=E);
        self.name=Label(self.profileF,text="Stav:",fg="red").grid(row=1,column=4,padx=8, pady=6, sticky=E);
        self.name=Label(self.profileF,text="Vedúci",fg="red").grid(row=2,column=4,padx=7, pady=6, sticky=E);
        self.name=Label(self.profileF,text="Počet článkov:",fg="red").grid(row=3,column=4,padx=7, pady=6, sticky=E);
        
        self.name=Label(self.profileF,text="Mrkvička", font = ('Comic Sans MS',11)).grid(row=0,column=5,padx=8, pady=6, sticky=W);
        self.name=Label(self.profileF,text="Online",fg="green", font = ('Comic Sans MS',11)).grid(row=1,column=5,padx=8, pady=6, sticky=W);
        self.name=Label(self.profileF,text="Milan Tichý", font = ('Comic Sans MS',11)).grid(row=2,column=5,padx=8, pady=6, sticky=W);  
        self.name=Label(self.profileF,text="122", font = ('Comic Sans MS',11)).grid(row=3,column=5,padx=8, pady=6, sticky=W);
        
        
        
        self.infoF=LabelFrame(self.doubleFrame2, text="Info")
        self.infoF.pack(padx=5,pady=5,fill=BOTH,side=BOTTOM,expand=1)
        
              #info
        self.onlineF=LabelFrame(self.infoF, text="Online Admini")
        self.onlineF.pack(padx=5, pady=5,fill=BOTH,expand=1, side=LEFT)
        
           #resolution

        self.mlb1 = table.MultiListbox(self.onlineF, (('Nick', 10), ('Mail', 20),))
        for i in range(len(resolution)):
            self.mlb1.insert(END, (resolution[i][0], resolution[i][1]))
        self.mlb1.pack(expand=YES,fill=BOTH, padx=10, pady=10)

        
        self.prehladF=LabelFrame(self.infoF, text="Celkový Prehlad")
        self.prehladF.pack(padx=5, pady=5,fill=BOTH,expand=1, side=RIGHT)
        
        self.visitedTimes=Label(self.prehladF,text="Návštevy tento mesiac: ",fg="gray22").grid(row=0,column=0, sticky=E,padx=8, pady=6)
        self.visitedTimes=Label(self.prehladF,text="Návštevy celkovo: ",fg="gray22").grid(row=1,column=0, sticky=E,padx=8, pady=6)
        self.visitedTimes=Label(self.prehladF,text="Počet článkov celkovo: ",fg="gray22").grid(row=2,column=0, sticky=E,padx=8, pady=6)
        self.visitedTimes=Label(self.prehladF,text="Počet likov celkovo: ",fg="gray22").grid(row=3,column=0, sticky=E,padx=8, pady=6)
        self.visitedTimes=Label(self.prehladF,text="Počet dislike celkovo: ",fg="gray22").grid(row=4,column=0, sticky=E,padx=8, pady=6)
        
        self.visitedTimes=Label(self.prehladF,text="2358", font = ('Comic Sans MS',10)).grid(row=0,column=1, sticky=W,padx=8, pady=6)
        self.visitedTimes=Label(self.prehladF,text="25 890", font = ('Comic Sans MS',10)).grid(row=1,column=1, sticky=W,padx=8, pady=6)
        self.visitedTimes=Label(self.prehladF,text="149", font = ('Comic Sans MS',10)).grid(row=2,column=1, sticky=W,padx=8, pady=6)
        self.visitedTimes=Label(self.prehladF,text="2222", font = ('Comic Sans MS',10)).grid(row=3,column=1, sticky=W,padx=8, pady=6)
        self.visitedTimes=Label(self.prehladF,text="411", font = ('Comic Sans MS',10)).grid(row=4,column=1, sticky=W,padx=8, pady=6)

#-------------------------------------------------------------
# page2 
        self.bigFrame=Frame(self.p2, bg="Black")
        self.bigFrame.pack(fill=BOTH, expand=1,side=TOP)
        
        self.filterF = LabelFrame(self.bigFrame, text="Výpis článkov / Filter")
        self.filterF.pack(padx=5, pady=5,fill=BOTH,expand=True, side=TOP)
        
        self.row1 = Frame(self.filterF)
        self.row1.pack(side=TOP,anchor=E)
        
        self.podrobnosti = Button(self.row1,text="Zobraz Podrobnosti", font = ('Comic Sans MS',10),command=self.showProperties)
        self.podrobnosti.pack(side=RIGHT,padx=10)
        
        self.podrobnosti = Button(self.row1,text="Zmeniť stav", font = ('Comic Sans MS',10),command=self.changeState)
        self.podrobnosti.pack(side=RIGHT,padx=10)

        self.mlb1 = table.MultiListbox(self.filterF, (('Titulok', 40), ('Autor', 20),('Dátum', 20),('Stav', 10)))
        for i in range(len(resolution)):
            self.mlb1.insert(END, (articles[i][0], articles[i][1],articles[i][2], articles[i][3]))
        self.mlb1.pack(expand=YES,fill=BOTH, padx=10, pady=10)
        
        self.filter = Frame(self.filterF)
        self.filter.pack(fill=BOTH,side=BOTTOM,padx=10,pady=15)
        
        self.search = Entry(self.filter,width=30)
        self.search.pack(side=LEFT)
        
        self.autor = Button(self.filter,text="Autor",width=(12),command=self.autor)
        self.autor.pack(side=LEFT,padx=(12,0))

        self.autor = Button(self.filter,text="Dátum",width=12,command=self.date)
        self.autor.pack(side=LEFT,padx=(12,0))

        self.autor = Button(self.filter,text="Stav",width=12,fg="green",command=self.state)
        self.autor.pack(side=LEFT,padx=(12,0))

        self.autor = Button(self.filter,text="Vyhľadat",width=12,fg="red",command=self.searchInputh)
        self.autor.pack(side=LEFT,padx=(12,0))
        
#page3
        self.bigFrame=Frame(self.p3, bg="Black")
        self.bigFrame.pack(fill=BOTH, expand=1,side=TOP)
        
        self.addF = LabelFrame(self.bigFrame, text="Pridaj článok")
        self.addF.pack(padx=5, pady=5,fill=BOTH,expand=True, side=TOP)
        
        self.row1 = Frame(self.addF)
        self.row1.pack(side=TOP,fill=X)
        
        self.title = Label(self.row1,text="Titulok: ")
        self.title.pack(side=LEFT,anchor=W)
    
        self.titleInput = Entry(self.row1)
        self.titleInput.pack(side=LEFT,expand=1,fill=BOTH,padx=15)
        
        self.row2 = Frame(self.addF)
        self.row2.pack(side=TOP,fill=X,pady=10)
        
        self.categorie = Label(self.row2,text="Kategórie: Nevybrané ")
        self.categorie.pack(anchor=W,side=LEFT,padx=10);
    
        self.categorie = Button(self.row2,text="Vyber Kategórie",command=self.category)
        self.categorie.pack(anchor=W,side=LEFT,padx=10)
           
        self.imgImport = Button(self.row2,text="Import Image",command=self.importImage)
        self.imgImport.pack(anchor=W,side=RIGHT,padx=10)
        
        self.categorie = Label(self.row2,text="/img/novýObrázok1 ")
        self.categorie.pack(anchor=W,side=RIGHT,padx=10)
        
        self.row3 = Frame(self.addF)
        self.row3.pack(side=TOP,fill=X,pady=10)
        
        self.textHeader = Label(self.row3,text="Text článku:")
        self.textHeader.pack(anchor=W,side=LEFT)
                

        self.textHeader = Button(self.row3,text="Moore",command=self.styleFonte)
        self.textHeader.pack(anchor=W,side=RIGHT,padx=(0,5), pady=5)
                
        self.textHeader = Button(self.row3,text="Font",command=self.styleFonte)
        self.textHeader.pack(anchor=W,side=RIGHT,padx=(0,5), pady=5)
        
        self.textHeader = Button(self.row3,text="U",command=self.styleFonte)
        self.textHeader.pack(anchor=W,side=RIGHT,padx=(0,5), pady=5)

        self.textHeader = Button(self.row3,text="I",command=self.styleFonte)
        self.textHeader.pack(anchor=W,side=RIGHT,padx=(0,5), pady=5)
       
        self.textHeader = Button(self.row3,text="B",command=self.styleFonte)
        self.textHeader.pack(anchor=W,side=RIGHT,padx=(0,5), pady=5)
       
        self.text= Text(self.addF,height=10)
        self.text.pack(side=TOP,fill=X,padx=8,pady=8)

        self.row4 = Frame(self.addF)
        self.row4.pack(side=TOP,fill=X,pady=10)
        
         
        self.extraOptions = LabelFrame(self.row4, text="Extra Options")
        self.extraOptions.pack(padx=5, pady=5,fill=BOTH,expand=True, side=LEFT)
        
        self.var1 = IntVar()
        self.lab1=Label(self.extraOptions, text="Ukáž autorov")
        self.c1 = Checkbutton(self.extraOptions, variable=self.var1)
        
        self.c1.pack(padx=5, pady=5,side=LEFT)      
        self.lab1.pack(padx=5, pady=5,side=LEFT)
 
        self.var2 = IntVar()
        self.lab2=Label(self.extraOptions, text="Povoľ Komentáre")
        self.c2 = Checkbutton(self.extraOptions, variable=self.var2)
      
        self.c2.pack(padx=5, pady=5,side=LEFT)   
        self.lab2.pack(padx=5, pady=5,side=LEFT)
   

        
        self.extraOptions = Frame(self.row4)
        self.extraOptions.pack(padx=5, pady=5,fill=BOTH,expand=True, side=RIGHT)
        
        self.row1=Frame(self.extraOptions)
        self.row1.pack(side=TOP)
        
        self.dateLabel = Label(self.row1,text="Publikovať: ")
        self.dateLabel.pack(side=LEFT)
        
        v = StringVar(root, value='dd/yy/mm ss/mm/hh')
        self.dd = Entry(self.row1,textvariable=v)
        self.dd.pack(side=LEFT,padx=15)    
        
        self.row2=Frame(self.extraOptions)
        self.row2.pack(side=TOP,anchor=SE)
        
        self.nahlad = Button(self.row2,text="Náhľad",command=self.nahlad)
        self.nahlad.pack(anchor=E,side=RIGHT,padx=(0,15), pady=10)
        
        self.publikovat = Button(self.row2,text="Publikovať",command=self.public)
        self.publikovat.pack(anchor=E,side=RIGHT,padx=(0,15), pady=10)
        
    def about(self):
        messagebox.showinfo("Redakčný systém","Tento program napísal MIN0110")
                
    def changeState(self):
        messagebox.showinfo("Akcia","Tabulka na zmenu stavu")
                
    def showProperties(self):
        messagebox.showinfo("Akcia","Podrobnosti a náhľad o článku")
                
    def autor(self):
        messagebox.showinfo("Akcia","Výber Autorov pre filter")
        
    def date(self):
        messagebox.showinfo("Akcia","Výber datumu pre filter")                
    
    def state(self):
        messagebox.showinfo("Akcia","Výber state pre filter")
        
    def searchInputh(self):
        messagebox.showinfo("Akcia","Vyhľadávam...")

    def category(self):
        messagebox.showinfo("Akcia","Výber kategórie")
        
    def importImage(self):
        messagebox.showinfo("Akcia","Importujem obrázok")                
    
    def styleFonte(self):
        messagebox.showinfo("Akcia","Uplatňujem štýl na písmo")
        
    def public(self):
        messagebox.showinfo("Akcia","Publikujem")                
   
    def nahlad(self):
        messagebox.showinfo("Akcia","náhľad príspevku")
        
    
root = tix.Tk()
root.wm_title("Redakčný Systém")
root.geometry("640x520")
app = App(root)
root.mainloop()