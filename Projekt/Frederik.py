

import MultiListbox as table
from tkinter import *
from tkinter import tix
from tkinter import messagebox


data = [
       ["Petr", "Challenger"],
       ["Jana", "Bronz"],
       ["Karel", "Platina"],
       ["Martin", "Silver"]]

resolution=[
    ["720 × 480","480p"],
    ["1280 × 720","720p"],
    ["1920 × 1080","1080p"],
    ["3840 × 2160","2160p"]
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
        self.helpmenu.add_command(label="About")

        root.config(menu=self.menu)

        
        

        #NOTEBOOK

        self.note=tix.NoteBook(root)
        self.note.add("page1", label="Options")
        self.note.add("page2", label="Friends")
        self.note.add("page3", label="Game")

        self.p1=self.note.subwidget_list["page1"]
        self.p2=self.note.subwidget_list["page2"]
        self.p3=self.note.subwidget_list["page3"]

        self.note.pack(expand=1, fill=BOTH)


        self.bigFrame=Frame(self.p1)
        self.bigFrame.pack(fill=BOTH, expand=1,side=TOP)

        #doubleFrame2
        self.doubleFrame2=Frame(self.bigFrame)
        self.doubleFrame2.pack(padx=5, pady=5, fill=BOTH, expand=1,side=TOP)
        

        #page1
        self.screenF=LabelFrame(self.doubleFrame2, text="Screen")
        self.screenF.pack(padx=5, pady=5,fill=BOTH,expand=1, side=LEFT)

        self.resF=LabelFrame(self.doubleFrame2, text="Resolution")
        self.resF.pack(padx=5,pady=5,fill=BOTH,side=RIGHT,expand=1)


    #resolution

        self.mlb1 = table.MultiListbox(self.resF, (('Resolution', 20), ('Type', 20)))
        for i in range(len(resolution)):
            self.mlb1.insert(END, (resolution[i][0], resolution[i][1]))
        self.mlb1.pack(expand=YES,fill=BOTH, padx=10, pady=10)
        self.mlb1.subscribe( lambda row: self.edit( row ) )
        


    #screen
        self.AA=StringVar()

        self.AntiA = Label(self.screenF, text='Anti Aliasing :')
        self.AntiA.grid(row=0,column=0)

        self.x2=Radiobutton(self.screenF, text="2X", variable=self.AA, value="2X")
        self.x2.grid(row=1,column=0)

        self.x4=Radiobutton(self.screenF, text="4X", variable=self.AA, value="4X")
        self.x4.grid(row=1,column=1)

        self.x8=Radiobutton(self.screenF, text="8X", variable=self.AA, value="8X")
        self.x8.grid(row=1,column=2)

        self.x16=Radiobutton(self.screenF, text="16X", variable=self.AA, value="16X")
        self.x16.grid(row=1,column=3)

        self.tmp = IntVar() 
        self.lab=Label(self.screenF, text="Volumetric Lightening")
        self.lab.grid(row=2, column=0)
        self.c = Checkbutton(self.screenF, variable=self.tmp) 
        self.c.grid(row=2, column=2)

        self.tmp1=IntVar()
        self.lab1=Label(self.screenF, text="Dynamic Shadows")
        self.lab1.grid(row=3,column=0)
        self.c = Checkbutton(self.screenF, variable=self.tmp1) 
        self.c.grid(row=3,column=2)

        self.lab2=Label(self.screenF, text="Field of view")
        self.lab2.grid(row=4,column=0)
        self.w = Scale(self.screenF, from_=90, to=130, orient=HORIZONTAL)
        self.w.grid(row=4,column=2)



      
    #doubleframe
        self.doubleFrame=Frame(self.bigFrame)
        self.doubleFrame.pack(padx=5, pady=5, fill=BOTH, expand=1, side=BOTTOM)


  #movement
        self.frame4=LabelFrame(self.doubleFrame, text="Movement")
        self.frame4.pack(padx=5, pady=5, fill=BOTH, expand=1,side=RIGHT)

        self.movef = Label(self.frame4, text='Move Forward :')
        self.movef.grid(row=0, column=0, padx=4, pady=4)
        self.movefE = Entry(self.frame4)
        self.movefE.grid(row=0, column=1, padx=4, pady=4)

        self.mover = Label(self.frame4, text='Move Right :')
        self.mover.grid(row=1, column=0, padx=4, pady=4)
        self.moverE = Entry(self.frame4)
        self.moverE.grid(row=1, column=1, padx=4, pady=4)

        self.movel = Label(self.frame4, text='Move Left :')
        self.movel.grid(row=2, column=0, padx=4, pady=4)
        self.movelE = Entry(self.frame4)
        self.movelE.grid(row=2, column=1, padx=4, pady=4)

        self.moveb = Label(self.frame4, text='Move Back :')
        self.moveb.grid(row=3, column=0, padx=4, pady=4)
        self.movebE = Entry(self.frame4)
        self.movebE.grid(row=3, column=1, padx=4, pady=4)

        self.jump = Label(self.frame4, text='Jump :')
        self.jump.grid(row=4, column=0, padx=4, pady=4)
        self.jumpE = Entry(self.frame4)
        self.jumpE.grid(row=4, column=1, padx=4, pady=4)

        self.crouch = Label(self.frame4, text='Crouch :')
        self.crouch.grid(row=4, column=0, padx=4, pady=4)
        self.crouchE = Entry(self.frame4)
        self.crouchE.grid(row=4, column=1, padx=4, pady=4)






        #abilities
        self.frame42=LabelFrame(self.doubleFrame, text="Weapon Abilities")
        self.frame42.pack(padx=5, pady=5, fill=BOTH, expand=1, side=LEFT)

        self.tacAb = Label(self.frame42, text='Tactical Ability :')
        self.tacAb.grid(row=0,  padx=4, pady=4)
        self.tacAbE = Entry(self.frame42)
        self.tacAbE.grid(row=0, column=1, padx=4, pady=4)

        self.ultAb = Label(self.frame42, text='Ultimate Ability :')
        self.ultAb.grid(row=1, column=0, padx=4, pady=4)
        self.ultAbE = Entry(self.frame42)
        self.ultAbE.grid(row=1, column=1, padx=4, pady=4)

        self.zoomb = Label(self.frame42, text='Zoom :')
        self.zoomb.grid(row=2, column=0, padx=4, pady=4)
        self.zoomE = Entry(self.frame42)
        self.zoomE.grid(row=2, column=1, padx=4, pady=4)

        self.shoot = Label(self.frame42, text='Shoot :')
        self.shoot.grid(row=3, column=0, padx=4, pady=4)
        self.shootE = Entry(self.frame42)
        self.shootE.grid(row=3, column=1, padx=4, pady=4)

        self.steady = Label(self.frame42, text='Steady :')
        self.steady.grid(row=4, column=0, padx=4, pady=4)
        self.steadyE = Entry(self.frame42)
        self.steadyE.grid(row=4, column=1, padx=4, pady=4)

        


        #save
        self.buttonFrame= Frame(self.p1)
        self.buttonFrame.pack(padx=5, pady=5, expand=1, fill=BOTH)


        self.buttonsframe=Frame(self.buttonFrame)
        self.buttonsframe.pack()
        self.cancelB = Button(self.buttonsframe,text="Koniec",command=self.exit)
        self.cancelB.grid(row=0,column=0)

        self.saveB = Button(self.buttonsframe,text="Ulozit",command=self.save)
        self.saveB.grid(row=0,column=2)




        #page2
        self.row = IntVar() 
        self.row = None
        self.name = StringVar()
        self.level= StringVar()


        self.mlb = table.MultiListbox(self.p2, (('Nick', 20), ('Level', 20)))
        for i in range(len(data)):
            self.mlb.insert(END, (data[i][0], data[i][1]))
        self.mlb.pack(expand=YES,fill=BOTH, padx=10, pady=10)
        self.mlb.subscribe( lambda row: self.edit( row ) )


        self.nb=tix.NoteBook(self.p2)
        self.nb.add("page1", label="Pridať")
        self.nb.add("page2", label="Chat")
        self.p11=self.nb.subwidget_list["page1"]
        self.p22=self.nb.subwidget_list["page2"]
        self.nb.pack(fill="both",expand=1,padx=4,pady=4,ipadx=4,ipady=4)

        self.tab1= Frame(self.p11)
        self.tab1.pack(fill="both",expand=1)

        self.nick=Label(self.tab1, text="Nick ")
        self.nick.grid(row=0)
        self.nicke=Entry(self.tab1)
        self.nicke.grid(row=0,column=1)

    #page2,2
        self.send = Button(self.p22,text="Send")
        self.send.grid(row=0,column=0 , sticky=W+E)
        input_text_area = Text(self.p22)
        input_text_area.grid(row=1, column=0, sticky=W+E)
        input_text_area.configure(background='#4D4D4D')
        


    #save
        self.newBu = Button(self.tab1,text="Novy zaznam",command=self.new)
        self.newBu.grid(row=0,column=3)




    #page3
        self.page3Frame=Frame(self.p3)
        self.page3Frame.pack()

        self.startB=Button(self.page3Frame, text="Start Game", command=self.hello)
        self.startB.pack()




    def hello(self):
        messagebox.showinfo("GAME IS RUNNING", "You started the game!")
        

    def exit(self):
        root.destroy()

    def save(self):
        data[self.row][0]=self.nicke.get()
        data[self.row][1]="platina"


    def new(self):
        data.insert(self.row,["",""])
        self.mlb.insert(END, [data[self.row][0],[data[self.row][1]]])
        self.edit(self.row)

      
    def edit(self, row):
        self.row=row
        self.jmeno = data[self.row][0]
        self.level=data[self.row][1]
        print (row)



        
root = tix.Tk()
root.wm_title("MyGame")
root.geometry("640x520")
app = App(root)
root.mainloop()