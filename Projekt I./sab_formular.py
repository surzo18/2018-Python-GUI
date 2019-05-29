# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import tix
import MultiListbox as table

data = [
       ["Petr", "Bílý", "045214/1512", "17. Listopadu", 15, "Ostrava", 70800, "poznamka"],
       ["Jana", "Zelený", "901121/7238", "Vozovna", 54, "Poruba", 78511, ""],
       ["Karel", "Modrý", "800524/5417", "Porubská", 7, "Praha", 11150, ""],
       ["Martin", "Stříbrný", "790407/3652", "Sokolovská", 247, "Brno", 54788, "nic"]]


class App(object):

    def select(self, row):
        self.row = row
        # delete entries
        self.clearData()
        # insert to entries
        self.jmenoEntry.insert(0, data[row][0])
        self.prijmeniEntry.insert(0, data[row][1])
        self.rodneCisloEntry.insert(0, data[row][2])
        self.uliceEntry.insert(0, data[row][3])
        self.mestoEntry.insert(0, data[row][5])
        self.pscEntry.insert(0, data[row][6])
        self.cpEntry.insert(0, data[row][4])
        self.poznamkaEntry.insert('1.0', data[row][7])

    def clearData(self):
        self.jmenoEntry.delete(0, END)
        self.prijmeniEntry.delete(0, END)
        self.rodneCisloEntry.delete(0, END)
        self.uliceEntry.delete(0, END)
        self.mestoEntry.delete(0, END)
        self.pscEntry.delete(0, END)
        self.cpEntry.delete(0, END)
        self.poznamkaEntry.delete('1.0', END)

    def clear(self):
        self.multiListBox.selection_clear(self.multiListBox.curselection())
        self.clearData()

    def newRecord(self):
        jmeno = self.jmenoEntry.get()
        prijmeni = self.prijmeniEntry.get()
        rodneCislo = self.rodneCisloEntry.get()
        ulice = self.uliceEntry.get()
        mesto = self.mestoEntry.get()
        psc = self.pscEntry.get()
        cp = self.cpEntry.get()
        poznamka = self.poznamkaEntry.get('1.0', END)
        user = [jmeno, prijmeni, rodneCislo, ulice, cp, mesto, psc, poznamka]
        data.append(user)
        self.multiListBox.insert(END, (user[0], user[1], user[2]))

    def saveRecord(self):
        jmeno = self.jmenoEntry.get()
        prijmeni = self.prijmeniEntry.get()
        rodneCislo = self.rodneCisloEntry.get()
        ulice = self.uliceEntry.get()
        mesto = self.mestoEntry.get()
        psc = self.pscEntry.get()
        cp = self.cpEntry.get()
        poznamka = self.poznamkaEntry.get('1.0', END)
        user = [jmeno, prijmeni, rodneCislo, ulice, cp, mesto, psc, poznamka]
        selectedIndex = self.multiListBox.curselection()[0]
        del data[selectedIndex]
        data.insert(selectedIndex, user)
        self.multiListBox.delete(0, END)
        for i in range(len(data)):
            self.multiListBox.insert(END, (data[i][0], data[i][1], data[i][2]))

    def closeWindow(self):
        self.window.destroy()

    def showDetails(self):

        index = self.multiListBox.curselection()[0]
        self.window = Toplevel(root)
        self.window.grab_set()
        self.window.transient(self.master)

        # Informace Label Frame
        informaceLabelFrame = LabelFrame(self.window, text="Informace")
        informaceLabelFrame.pack(fill=BOTH, side=TOP, padx=10, pady=10)

        self.userPhoto = PhotoImage(file="img.png")
        cnv = Canvas(informaceLabelFrame, width=100, height=100)
        cnv.create_image(50, 50, image=self.userPhoto)
        cnv.grid(column=1, row=1, rowspan=4)

        informaceJmeno = Label(informaceLabelFrame, text="Jméno:")
        informaceJmeno.grid(column=2, row=1, sticky=E)
        informacePrijmeni = Label(informaceLabelFrame, text="Příjmení:")
        informacePrijmeni.grid(column=2, row=2, sticky=E)
        informaceRodneCislo = Label(informaceLabelFrame, text="Rodné číslo:")
        informaceRodneCislo.grid(column=2, row=3, sticky=E)
        informaceAdresa = Label(informaceLabelFrame, text="Adresa:")
        informaceAdresa.grid(column=2, row=4, sticky=E)

        jmeno = data[index][0]
        prijmeni = data[index][1]
        rodneCislo = data[index][2]
        adresa = data[index][3] + ", " + str(data[index][4]) + ", " + data[index][5] + ", " + str(data[index][6])

        infoUserJmeno = Label(informaceLabelFrame, text=jmeno)
        infoUserPrijmeni = Label(informaceLabelFrame, text=prijmeni)
        infoUserRodneCislo = Label(informaceLabelFrame, text=rodneCislo)
        infoUserAdresa = Label(informaceLabelFrame, text=adresa)
        infoUserJmeno.grid(column=3, row=1, sticky=W, padx=10)
        infoUserPrijmeni.grid(column=3, row=2, sticky=W, padx=10)
        infoUserRodneCislo.grid(column=3, row=3, sticky=W, padx=10)
        infoUserAdresa.grid(column=3, row=4, sticky=W, padx=10)

        mapaLabelFrame = LabelFrame(self.window, text="Mapa")
        mapaLabelFrame.pack(fill=BOTH, side=TOP, padx=10, pady=10, expand=TRUE)

        innerFrame = Frame(mapaLabelFrame)
        innerFrame.pack(fill=BOTH, side=TOP)

        self.mapaImage = PhotoImage(file="mapa.png")
        cnvMapa = Canvas(innerFrame, width=500, height=500)
        cnvMapa.create_image(250, 250, image=self.mapaImage)
        cnvMapa.pack(side=LEFT, fill=BOTH, expand=TRUE)
        sliderY = Scale(innerFrame, from_=0, to=100, orient=VERTICAL, showvalue=0)
        sliderY.pack(fill=Y, side=RIGHT)
        sliderX = Scale(mapaLabelFrame, from_=0, to=100, orient=HORIZONTAL, showvalue=0)
        sliderX.pack(side=BOTTOM, fill=X)

        closeButton = Button(self.window, text="Zavřít", command=self.closeWindow, width=10)
        closeButton.pack(side=BOTTOM, pady=10)

    def __init__(self, master):
        self.master = master
        # Define variables
        self.row = IntVar()
        self.row = None
        self.jmeno = StringVar()
        self.prijmeni = StringVar()
        self.rc = StringVar()
        self.ulice = StringVar()
        self.cp = StringVar()
        self.mesto = StringVar()
        self.psc = StringVar()

        # Multi List Box
        self.multiListBox = table.MultiListbox(master, (('Jméno', 20), ('Příjmení', 20), ('Rodné číslo', 12)))
        # Insert data
        for i in range(len(data)):
            self.multiListBox.insert(END, (data[i][0], data[i][1], data[i][2]))

        self.multiListBox.pack(expand=YES, fill=BOTH, padx=10, pady=10)
        # Subscribe -> on click call edit on clicked row
        self.multiListBox.subscribe(lambda row: self.select(row))

        # Osobni udaje
        self.osobniUdajeFrame = Frame(master)
        self.osobniUdajeFrame.pack(padx=10, pady=20, side=TOP)
        # Jmeno
        self.jmenoLabel = Label(self.osobniUdajeFrame, text="Jméno:")
        self.jmenoLabel.grid(row=1, column=1)
        self.jmenoEntry = Entry(self.osobniUdajeFrame, width=20)
        self.jmenoEntry.grid(row=1, column=2)
        # Prijmeni
        self.prijmeniLabel = Label(self.osobniUdajeFrame, text="Příjmení:")
        self.prijmeniLabel.grid(row=2, column=1)
        self.prijmeniEntry = Entry(self.osobniUdajeFrame, width=20)
        self.prijmeniEntry.grid(row=2, column=2)
        # Rodne cislo
        self.rodneCisloLabel = Label(self.osobniUdajeFrame, text="Rodné číslo:")
        self.rodneCisloLabel.grid(row=3, column=1)
        self.rodneCisloEntry = Entry(self.osobniUdajeFrame, width=13)
        self.rodneCisloEntry.grid(row=3, column=2, sticky=W)

        # Note Book
        self.noteBook = tix.NoteBook(master)
        self.noteBook.add("adresaPage", label="Adresa")
        self.noteBook.add("poznamkaPage", label="Poznámka")
        # Adresa subwidgets
        self.adresaPage = self.noteBook.subwidget_list["adresaPage"]
        # Poznamka subwidgets
        self.poznamkaPage = self.noteBook.subwidget_list["poznamkaPage"]

        self.noteBook.pack(fill=BOTH, side=TOP)

        # ADRESA
        self.adresaLabelFrame = LabelFrame(self.adresaPage, text="Adresa")
        self.adresaLabelFrame.pack(fill=BOTH, side=TOP)

        self.adresaFrame = Frame(self.adresaLabelFrame, padx=10, pady=10)
        self.adresaFrame.pack(side=TOP, expand=1)

        self.uliceLabel = Label(self.adresaFrame, text="Ulice: ", padx=4, pady=4)
        self.uliceLabel.grid(row=1, column=1)
        self.mestoLabel = Label(self.adresaFrame, text="Město: ", padx=4, pady=4)
        self.mestoLabel.grid(row=2, column=1)
        self.pscLabel = Label(self.adresaFrame, text="PSČ: ", padx=4, pady=4)
        self.pscLabel.grid(row=3, column=1)
        self.cpLabel = Label(self.adresaFrame, text="č.p.", padx=10, pady=4)
        self.cpLabel.grid(row=1, column=3)

        self.uliceEntry = Entry(self.adresaFrame, width=15)
        self.uliceEntry.grid(row=1, column=2, sticky=W)
        self.mestoEntry = Entry(self.adresaFrame, width=20)
        self.mestoEntry.grid(row=2, column=2, sticky=W)
        self.pscEntry = Entry(self.adresaFrame, width=10)
        self.pscEntry.grid(row=3, column=2, sticky=W)
        self.cpEntry = Entry(self.adresaFrame, width=8)
        self.cpEntry.grid(row=1, column=4)

        # POZNAMKA
        self.poznamkaLabelFrame = LabelFrame(self.poznamkaPage, text="Poznámka")
        self.poznamkaLabelFrame.pack(fill=BOTH, expand=1, side=TOP)

        self.poznamkaEntry = Text(self.poznamkaLabelFrame, height=10)
        self.poznamkaEntry.pack()

        # Tlacitka
        self.buttonsFrame = Frame(master)
        self.buttonsFrame.pack(padx=10, pady=20)

        self.cancelButton = Button(self.buttonsFrame, text="Cancel", width=15, command=self.clear)
        self.cancelButton.pack(pady=10, side=LEFT)

        self.newRecordButton = Button(self.buttonsFrame, text="Nový záznam", width=15, command=self.newRecord)
        self.newRecordButton.pack(pady=10, side=LEFT)

        self.saveRecordButton = Button(self.buttonsFrame, text="Uložit záznam", width=15, command=self.saveRecord)
        self.saveRecordButton.pack(pady=10, side=LEFT)

        self.showDetailsButton = Button(self.buttonsFrame, text="Zobrazit detaily", width=15, command=self.showDetails)
        self.showDetailsButton.pack(pady=10, side=LEFT)

root = Tk()
root.wm_title("Formulář")
app = App(root)
root.mainloop()

