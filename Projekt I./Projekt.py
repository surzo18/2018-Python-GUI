from tkinter import *
from tkinter.font import *
import MultiListbox as table
import functools



movies = [
       ["Captain Marvel", "Sci-fi","124",("1","2","3"),("14:30","18:30","20:30"),0],
       ["Avengers Endgame", "Sci-fi","140",("2","4","5"),("16:30","15:30","21:00"),1],
       ["Wonder Park", "Comedy","80",("1","2","5"),("14:30","20:30","22:30"),2],
       ["Us", "Horror","100",("3","1","2"),("15:00","17:30","20:00"),3],
       ["Gloria", "Drama","102",("4","1","2"),("15:30","16:30","19:30"),4],
       ["Alita", "Action","122",("1","5","4"),("12:30","14:30","17:00"),5]
       
       ]

drinks = [
    ["CocaCola", "1,5€"],
    ["Monster", "1€"],
    ["Beer", "1,2€"]
     

    ]


meals = [
    ["Nachos", "2,5€"],
    ["Crispers", "1,2€"],
    ["Popcorn", "2€"]
    
    
    ]

class myProject:

    def __init__(self, root):
        
        self.row = IntVar()
        self.row = None
        
        self.day=1
        self.movie=1
        self.food=1
        self.movieOrder=[(5,)]
        self.foodOrder=[]
        self.actualSeats=[5,6]

        self.menubar = Menu(root)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Soubor", menu=self.filemenu)
        #self.filemenu.add_command(label="Refresh", command=self.refreshMovies)
        self.filemenu.add_command(label="Quit", command=self.exit )

        self.editmenu = Menu(self.menubar, tearoff=0)
       # self.menubar.add_cascade(label="Nastaveni", menu=self.editmenu)
       # self.editmenu.add_command(label="Nic")

        self.nb=NoteBook(root)
        root.config(menu=self.menubar)

        
        self.nb.add("page1", label="Movies")
        self.nb.add("page2", label="Food")
        self.nb.add("page3", label="Cart")
        self.p1=self.nb.subwidget_list["page1"]
        self.p2=self.nb.subwidget_list["page2"]
        self.p3=self.nb.subwidget_list["page3"]
        self.nb.pack(fill="both",expand=1,padx=4,pady=4,ipadx=4,ipady=4)

    


        root.title('EasyCinema')

        self.font = Font(size=10, weight="normal")
    
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        

        #Page 1 - Movie order


        self.days = Frame(self.p1, relief=GROOVE)
        self.days.grid(row=0, column=0,columnspan=2)
        
        

        self.btn1 = Button(self.days, text="Day1\n25.3.",command=lambda : self.changeDay(1),width=5, height=2, font=self.font  )
        self.btn1.grid(row=1, column=1,sticky=W+E+N+S, padx=2, pady=2)
        
        
        self.btn2 = Button(self.days, text="Day2\n26.3.",command=lambda : self.changeDay(2),width=5, height=2, font=self.font)
        self.btn2.grid(row=1, column=2, sticky=W+E+N+S, padx=2, pady=2)
        

        self.btn3 = Button(self.days, text="Day3\n27.3.",command=lambda : self.changeDay(3),width=5, height=2, font=self.font  )
        self.btn3.grid(row=1, column=3,sticky=W+E+N+S, padx=2, pady=2)
        

        self.btn4 = Button(self.days, text="Day4\n28.3.",command=lambda : self.changeDay(4),width=5, height=2, font=self.font  )
        self.btn4.grid(row=1, column=4, sticky=W+E+N+S, padx=2, pady=2)

        self.btn5 = Button(self.days, text="Day5\n29.3.",command=lambda : self.changeDay(5),width=5, height=2, font=self.font  )
        self.btn5.grid(row=1, column=5, sticky=W+E+N+S, padx=2, pady=2)

        

        self.movies_group = LabelFrame(self.p1, text="Movies", padx=5, pady=5)
        self.movies_group.grid(row=1,column=0)

        Label(self.movies_group, text="Name", anchor="w").grid(row=0, column=0, sticky="ew")
        Label(self.movies_group, text="Genre", anchor="w").grid(row=0, column=1, sticky="ew")
        Label(self.movies_group, text="Length", anchor="w").grid(row=0, column=2, sticky="ew")
        
        self.movies()

        self.movie_detail = LabelFrame(self.p1, text="Movie detail", padx=5, pady=5)
        self.movie_detail.grid(row=1,column=3)
        self.show_movieDetail()
        
        

 
        #Page2 - Food order
        


        self.drink = Frame(self.p2,relief=GROOVE)
        self.drink.grid(row=0,column=0)
        Label(self.drink, text="Drinks", anchor="w").grid(row=0, column=1, sticky="ew")
        self.show_drinks()

        self.eat = Frame(self.p2,relief=GROOVE)
        self.eat.grid(row=0,column=1)
        Label(self.eat, text="Meals", anchor="w").grid(row=0, column=1, sticky="ew")
        self.show_meals()

        self.food_detail = LabelFrame(self.p2, text="Food detail", padx=5, pady=5)
        self.food_detail.grid(row=0,column=2)
        
        self.show_foodDetail(self.food)

        #Page3 - Cart

        self.mcar = LabelFrame(self.p3,relief=GROOVE,text="Movie cart")
        self.mcar.grid(row=0,column=0)

        Label(self.mcar, text="Captain Marvel 16:30 22,24", anchor="w",width=30).grid(row=1, column=0, sticky="ew")
        
        self.fcar = LabelFrame(self.p3,relief=GROOVE,text="Food cart")
        self.fcar.grid(row=0,column=2)
        Label(self.fcar, text="Coca Cola L 2x", anchor="w",width=30).grid(row=0, column=2, sticky="ew")
        Label(self.fcar, text="Popcorn M 1x", anchor="w",width=30).grid(row=1, column=2, sticky="ew")
        Label(self.fcar, text="Nachos S 1x", anchor="w",width=30).grid(row=2, column=2, sticky="ew")


        self.bcar=Frame(self.p3,relief=GROOVE)
        self.bcar.grid(row=0,column=1)

        co=Button(self.bcar,text="OK",background='green')
        co.grid(row=0,column=0)
        ca=Button(self.bcar,text="KO",background='red')
        ca.grid(row=1,column=0)
        
        






    def changeDay(self,x):
        self.day=x
        print (self.day)
        self.movies()
        

    def changeMovie(self,movie):
        self.movie=movie
        print(self.movie)
        self.show_movieDetail()

    def movies(self):
        x=self.day
        row = 1
        for i in range(len(movies)):
           if str(x) in movies[i][3]:
            name_label = Label(self.movies_group, text=movies[i][0], anchor="w")
            genre_label = Label(self.movies_group, text=movies[i][1], anchor="w")
            length_label = Label(self.movies_group, text=movies[i][2], anchor="w")
            active_cb = Button(self.movies_group,command =functools.partial(self.changeMovie,movies[i][5]),text="Select")
  
            print(self.movie)

            name_label.grid(row=row, column=0, sticky="ew")
            genre_label.grid(row=row, column=1, sticky="ew")
            length_label.grid(row=row, column=2, sticky="ew")
            active_cb.grid(row=row, column=3, sticky="ew")


            row += 1
    

    def show_drinks(self):
        row = 1
        for i in range(len(drinks)):
            name_label = Label(self.drink, text=drinks[i][0], anchor="w")
            price_label = Label(self.drink, text=drinks[i][1], anchor="w")
            drink_button = Button(self.drink, text="Select" )

            name_label.grid(row=row, column=0, sticky="ew")
            price_label.grid(row=row, column=1, sticky="ew")
            drink_button.grid(row=row, column=3, sticky="ew")

            row += 1

    def show_meals(self):
        row = 1
        for i in range(len(meals)):
            name_label = Label(self.eat, text=meals[i][0], anchor="w")
            price_label = Label(self.eat, text=meals[i][1], anchor="w")
            meal_button = Button(self.eat, text="Select" )

            name_label.grid(row=row, column=0, sticky="ew")
            price_label.grid(row=row, column=1, sticky="ew")
            meal_button.grid(row=row, column=3, sticky="ew")


            row += 1


    def show_foodDetail(self,food):
        Label(self.food_detail, text="Name:  ", anchor="w").grid(row=0, column=0, sticky="ew")
        Label(self.food_detail, text=drinks[food][0], anchor="w").grid(row=0, column=1, sticky="ew")

        Label(self.food_detail, text="Size:  ", anchor="w").grid(row=1, column=0, sticky="ew")
        scale=Scale(master=self.food_detail, from_=1, to=3,resolution=1, orient=HORIZONTAL).grid(row=1, column=1, sticky="ew")
       
        Label(self.food_detail, text="Quantity:  ", anchor="w").grid(row=2, column=0, sticky="ew")
        entry=Entry(self.food_detail)
        entry.grid(row=2,column=1)

        foodOK=Button(self.food_detail,text="OK",background='green')
        foodOK.grid(row=3,column=1)
        
    def show_movieDetail(self):

        movie=self.movie
        Label(self.movie_detail, text="Name: ", anchor="w").grid(row=0, column=0, sticky="ew")
        Label(self.movie_detail, text=movies[movie][0], anchor="w").grid(row=0, column=1, sticky="ew")

        Label(self.movie_detail, text="Playing: ", anchor="w").grid(row=1, column=0, sticky="ew")

        row =1
        for time in movies[movie][4]:
            
            a=Button(self.movie_detail, text=time,width=5, height=2, font=self.font,command=functools.partial(self.buyTickets,time))
            a.grid(row=row,column=1)
            row+=1



    def buyTickets(self,time):
        self.order = Toplevel(root)
        self.order.title('Buying tickets')

        self.header = Frame( self.order, relief=GROOVE,padx=15)
        self.header.grid(row=0, column=0,columnspan=8)

        for movie in movies:
            if movie[5]==self.movie:
                 name=movie[0]

        Label( self.order, text="Name: "+name+"  Day: "+str(self.day)+" Time: "+time, anchor="w").grid(row=0, column=0, sticky="ew")

        self.cinema = Frame( self.order, relief=GROOVE)
        self.cinema.grid(row=2, column=0)
        
        column=0
        row=2
        for item in list(range(1, 31)):
            button=Checkbutton(self.cinema, text=str(item),command=functools.partial(self.addTicket,item))
            button.grid(row=row,column=column)
            column+=1
            if column==7:
                column=0
                row+=1

        self.seat_detail = LabelFrame( self.order, text="Reserved seats", padx=5, pady=5)
        self.seat_detail.grid(row=0,column=1)

        self.seat_buttons=Frame( self.order,relief=GROOVE)
        self.seat_buttons.grid(row=2,column=1)

        Button(self.seat_buttons,text="Confirm",background='green',command=self.confirmOrder,width=10).grid(row=0,column=0)
        Button(self.seat_buttons,text=" Cancel ",background='red',command=self.cancelOrder,width=10).grid(row=1,column=0)

        self.show_seats()
        
        
        
    def addTicket(self,ticket):
        self.actualSeats.append(ticket)
        print(ticket)

    def confirmOrder(self):

        self.movieOrder.append(self.actualSeats)
        self.order.destroy()

    def cancelOrder(self):
        self.order.destroy()
        self.actualSeats=[]

    def show_seats(self):
        row=0
        for seat in self.actualSeats:
            
            Label(self.seat_detail, text=seat,anchor="w").grid(row=row, column=0, sticky="ew")
            row+=1

    def refreshMovies(self):
        self.movies()
        self.show_movie_detail()


    def exit(self):
        root.destroy()



root = Tk()
app = myProject(root)



root.mainloop() 

