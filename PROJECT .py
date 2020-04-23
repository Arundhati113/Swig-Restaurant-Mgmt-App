import tkinter
from tkinter import *
import time
import random
import tkinter.messagebox as box

operator = ''
class Swig(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        cont = tkinter.Frame(self)
        tkinter.Tk.wm_title(self, "SWIG")

        cont.pack(side="top", fill="both", expand=True)
        cont.grid_rowconfigure(0, weight=1)
        cont.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage, FourthPage, FifthPage):
            frame = F(cont, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(FirstPage)

    def show_frame(self, cont1):
        frame = self.frames[cont1]
        frame.tkraise()






class FirstPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        Tops = Frame(self, bg="white", width=1600, height=50, relief=SUNKEN)
        Tops.pack(side=TOP)
        lblinfo = Label(Tops, font=('AR CENA', 50, 'bold','underline'), text="Welcome to Swig", fg="steel blue", bd=10, anchor='w')
        lblinfo.grid(row=0, column=0)
        Tops = Frame(self, bg="white", width=1600, height=50, relief=SUNKEN)
        Tops.pack(side=TOP)
        lblinfo = Label(Tops, font=('Arial', 35, 'bold','underline'), text="Login page", fg="steel blue", bd=10, anchor='w')
        lblinfo.grid(row=1, column=1)

        def dialog1():


            username = Entry_Username.get()
            password = Entry_Password.get()
            if (username == 'user' and password == 'abcd#123'):

                controller.show_frame(SecondPage)
            else:
                box.showinfo('info', 'Invalid Login')

        Label_Username=Label(self, text= "Username: ")
        Label_Username.pack()
        Label_Username.place(x=620, y=200)

        Entry_Username=Entry(self, bd= 5)
        Entry_Username.pack()
        Entry_Username.place(x=720, y=200)

        Label_Password  = Label(self, text='Password: ')
        Label_Password.pack(padx=15, pady=6)
        Label_Password.place(x=620, y=300)

        Entry_Password = Entry(self, bd=5,show="*")
        Entry_Password.pack(padx=15, pady=7)
        Entry_Password.place(x=720, y=300)

        Button_Login = Button(self, text='Check Login', command= dialog1 )


        Button_Login.place(relx=0.5, rely=0.5, anchor=CENTER)


class SecondPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        v=tkinter.IntVar()
        v.set(1)

        options = [
            ("Burger king"),
            ("Subway"),
            ("Dominos"),
            ("Pizza hut"),
        ]
        Tops = Frame(self, bg="white", width=1600, height=50, relief=SUNKEN)
        Tops.pack(side=TOP)
        lblinfo = Label(Tops, font=('AR CENA', 50,'bold'), text="Select the name of Restaurant", fg="steel blue", bd=10,
                        anchor='w')
        lblinfo.grid(row=0, column=0)
        def ShowChoice():
            print(v.get())


        for val, opt in enumerate(options):
            tkinter.Radiobutton(
                self,
                text = opt,
                padx = 20,
                variable = v,
                command = ShowChoice,
                value= val).pack(anchor=tkinter.N)

        btnGoToNext = tkinter.Button(self, text = "Select", command = lambda: controller.show_frame(ThirdPage))
        btnGoToNext.pack()

        btnGoToNext.place(relx=0.5, rely=0.5, anchor=S)
class ThirdPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        Tops = Frame(self, bg="white", width=1600, height=50, relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(self, width=900, height=700, relief=SUNKEN)
        f1.pack(side=LEFT)

        f2 = Frame(self, width=400, height=700, relief=SUNKEN)
        f2.pack(side=RIGHT)

        # ------------------TIME--------------
        localtime = time.asctime(time.localtime(time.time()))
        # -----------------INFO TOP------------
        lblinfo = Label(Tops, font=('arial', 30, 'bold'), text="Menu", fg="black", bd=10, anchor='w')
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(Tops, font=('arial', 20,), text=localtime, fg="black", anchor=W)
        lblinfo.grid(row=1, column=0)

        # ---------------Calculator------------------
        ft2 = Frame(f2, width=440, height=450, bd=12, relief="raise")
        ft2.pack(side=TOP)
        fb2 = Frame(f2, width=440, height=300, bd=16, relief="raise")
        fb2.pack(side=BOTTOM)
        Tops.configure(background="black")
        lblReceipt = Label(ft2,  font=('arial', 12, 'bold'), text="Restaurant Receipt", fg="steel blue", bd=2,justify=CENTER)
        lblReceipt.grid(row=0, column=0)
        txtReceipt=Text(fb2, font=('arial',11,'bold'),bd=8,width=40)
        txtReceipt.grid(row=1,column=0)
        def Ref():
            x = random.randint(1,10000)
            randomRef = str(x)
            rand.set(randomRef)
            txtReceipt.delete("1.0", END)
            cof = float(Fries.get())
            colfries = float(Largefries.get())
            cob = float(Burger.get())
            cofi = float(Filet.get())
            cochee = float(Cheese_burger.get())
            codr = float(Drinks.get())

            costoffries = cof * 25
            costoflargefries = colfries * 40
            costofburger = cob * 35
            costoffilet = cofi * 50
            costofcheeseburger = cochee * 50
            costofdrinks = codr * 35



            costofmeal =  str('Rs.  %.2f' % (
            costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
            PayTax = (
            (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) * 0.33)
            Totalcost = (
            costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)
            Ser_Charge = (
            (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) / 99)
            Service =  str('Rs.  %.2f' % Ser_Charge)
            OverAllCost = str("Rs. %.2f" % (PayTax + Totalcost + Ser_Charge))
            PaidTax =  str('Rs.  %.2f' % PayTax)

            Service_Charge.set(Service)
            cost.set(costofmeal)
            Tax.set(PaidTax)

            Total.set(OverAllCost)

        # def qexit():
            # root.destroy()


        def reset():
            rand.set("")
            Fries.set("")
            Largefries.set("")
            Burger.set("")
            Filet.set("")

            Total.set("")
            Service_Charge.set("")
            Drinks.set("")
            Tax.set("")
            cost.set("")
            Cheese_burger.set("")


        # ---------------------------------------------------------------------------------------
        rand = StringVar()
        Fries = StringVar()

        Largefries = StringVar()
        Burger = StringVar()
        Filet = StringVar()

        Total = StringVar()
        Service_Charge = StringVar()
        Drinks = StringVar()
        Tax = StringVar()
        cost = StringVar()
        Cheese_burger = StringVar()
        Receipt=StringVar()
        DateOfOrder=StringVar()
        lblreference = Label(f1, font=('arial', 16, 'bold'), text="Order No.", fg="steel blue", bd=10, anchor='w')
        lblreference.grid(row=0, column=0)
        txtreference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg="powder blue",
                             justify='right')
        txtreference.grid(row=0, column=1)

        lblfries = Label(f1, font=('arial', 16, 'bold'), text="Fries Meal", fg="steel blue", bd=10, anchor='w')
        lblfries.grid(row=1, column=0)
        txtfries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtfries.grid(row=1, column=1)

        lblLargefries = Label(f1, font=('arial', 16, 'bold'), text="Lunch Meal", fg="steel blue", bd=10, anchor='w')
        lblLargefries.grid(row=2, column=0)
        txtLargefries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Largefries, bd=6, insertwidth=4,
                              bg="powder blue", justify='right')
        txtLargefries.grid(row=2, column=1)

        lblburger = Label(f1, font=('arial', 16, 'bold'), text="Burger Meal", fg="steel blue", bd=10, anchor='w')
        lblburger.grid(row=3, column=0)
        txtburger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="powder blue",
                          justify='right')
        txtburger.grid(row=3, column=1)

        lblFilet = Label(f1, font=('arial', 16, 'bold'), text="Pizza Meal", fg="steel blue", bd=10, anchor='w')
        lblFilet.grid(row=4, column=0)
        txtFilet = Entry(f1, font=('arial', 16, 'bold'), textvariable=Filet, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtFilet.grid(row=4, column=1)

        lblCheese_burger = Label(f1, font=('arial', 16, 'bold'), text="Cheese burger", fg="steel blue", bd=10,
                                 anchor='w')
        lblCheese_burger.grid(row=5, column=0)
        txtCheese_burger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cheese_burger, bd=6, insertwidth=4,
                                 bg="powder blue", justify='right')
        txtCheese_burger.grid(row=5, column=1)

        # --------------------------------------------------------------------------------------
        lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", fg="steel blue", bd=10, anchor='w')
        lblDrinks.grid(row=0, column=2)
        txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="powder blue",
                          justify='right')
        txtDrinks.grid(row=0, column=3)

        lblcost = Label(f1, font=('arial', 16, 'bold'), text="cost", fg="steel blue", bd=10, anchor='w')
        lblcost.grid(row=1, column=2)
        txtcost = Entry(f1, font=('arial', 16, 'bold'), textvariable=cost, bd=6, insertwidth=4, bg="powder blue",
                        justify='right')
        txtcost.grid(row=1, column=3)

        lblService_Charge = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", fg="steel blue", bd=10,
                                  anchor='w')
        lblService_Charge.grid(row=2, column=2)
        txtService_Charge = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4,
                                  bg="powder blue", justify='right')
        txtService_Charge.grid(row=2, column=3)

        lblTax = Label(f1, font=('arial', 16, 'bold'), text="Tax", fg="steel blue", bd=10, anchor='w')
        lblTax.grid(row=3, column=2)
        txtTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="powder blue",
                       justify='right')
        txtTax.grid(row=3, column=3)


        lblTotal = Label(f1, font=('arial', 16, 'bold'), text="Total", fg="steel blue", bd=10, anchor='w')
        lblTotal.grid(row=4, column=2)
        txtTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtTotal.grid(row=4, column=3)
        DateOfOrder.set(time.strftime("%d/%m/%y"))

        def Receipt():
           txtReceipt.delete("1.0",END)
           x=random.randint(100898,192479)
           randomRef=str(x)

           txtReceipt.insert(END, "Date:\t\t" + str(DateOfOrder.get()))
           txtReceipt.insert(END, "Order no:\t" + str(rand.get()))
           txtReceipt.insert(END,"\t\tFries\t\t\t"+str(Fries.get()))



           txtReceipt.insert(END, "\t\tLunch Meal\t\t\t" + str(Largefries.get()))

           txtReceipt.insert(END, "\t\tBurger Meal\t\t\t" + str(Burger.get()))

           txtReceipt.insert(END, "\t\tPizza Meal\t\t\t" + str(Filet.get()))

           txtReceipt.insert(END, "\t\tCheese Burger\t\t\t" + str(Cheese_burger.get()))

           txtReceipt.insert(END,"\t\tDrinks\t\t\t"+str(Drinks.get()))

           txtReceipt.insert(END, "\t\tCost\t\t\t" + str(cost.get()))
           txtReceipt.insert(END, "\t\tService Charge\t\t\t" + str(Service_Charge.get()))

           txtReceipt.insert(END, "\t\tTax Paid\t\t\t" + str(Tax.get()))
           txtReceipt.insert(END, "\t\tTotal cost:\t\t\t" + str(Total.get()))


        # -----------------------------------------buttons------------------------------------------
        lblTotal = Label(f1, text="---------------------", fg="white")
        lblTotal.grid(row=6, columnspan=3)

        btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('arial', 16, 'bold'), width=10, text="TOTAL",
                          bg="powder blue", command=Ref)
        btnTotal.grid(row=7, column=1)


        btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('arial', 16, 'bold'), width=10, text="RESET",
                          bg="powder blue", command=reset)
        btnreset.grid(row=7, column=2)

        btnreceipt = Button(fb2, padx=16, pady=8, bd=10, fg="black", font=('arial', 16, 'bold'), width=10, text="RECEIPT",
                          bg="powder blue", command=Receipt)
        btnreceipt.grid(row=7, column=2)

        # btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('arial', 16, 'bold'), width=10, text="EXIT",
        #                  bg="powder blue", command=qexit)
        # btnexit.grid(row=7, column=3)

        btnFourthPage = Button(self, text="Next Page", command= lambda: controller.show_frame(FourthPage) )
        btnFourthPage.pack(side=TOP)
        def price():
            roo = Tk()
            roo.geometry("600x220+0+0")
            roo.title("Price List")
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="ITEM", fg="black", bd=5)
            lblinfo.grid(row=0, column=0)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="_____________", fg="white", anchor=W)
            lblinfo.grid(row=0, column=2)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="PRICE", fg="black", anchor=W)
            lblinfo.grid(row=0, column=3)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=0)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="25", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=3)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=0)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="40", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=3)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
            lblinfo.grid(row=3, column=0)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="35", fg="steel blue", anchor=W)
            lblinfo.grid(row=3, column=3)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
            lblinfo.grid(row=4, column=0)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="50", fg="steel blue", anchor=W)
            lblinfo.grid(row=4, column=3)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
            lblinfo.grid(row=5, column=0)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="30", fg="steel blue", anchor=W)
            lblinfo.grid(row=5, column=3)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=0)
            lblinfo = Label(roo, font=('arial', 15, 'bold'), text="35", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=3)

            roo.mainloop()

        btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('arial', 16, 'bold'), width=10, text="PRICE",
                          bg="powder blue", command=price)
        btnprice.grid(row=7, column=0)

class FourthPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        Tops = Frame(self, bg="white", width=1600, height=50, relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(self, width=900, height=700, relief=SUNKEN)
        f1.pack(side=LEFT)

        f2 = Frame(self, width=400, height=700, relief=SUNKEN)
        f2.pack(side=RIGHT)

        # -----------------INFO TOP------------
        lblinfo = Label(Tops, font=('AR CENA', 50, 'bold'), text="Customer Details", fg="steel blue", bd=10, anchor='w')
        lblinfo.grid(row=0, column=0)

        def Ref():
            x = random.randint(12980, 50876)
            randomRef = str(x)
            rand.set(randomRef)

            con = float(Name.get())
            coa = float(Address.get())
            colri = float(Phoneno.get())



        def reset():
            rand.set("")
            Name.set("")
            Address.set("")
            Phoneno.set("")

        rand = StringVar()
        Name = StringVar()
        Address = StringVar()
        Phoneno = StringVar()

        lblname = Label(f1, font=('arial', 16, 'bold'), text="Name.", fg="steel blue", bd=10, anchor='w')
        lblname.grid(row=0, column=0)
        txtname = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg="powder blue",
                             justify='right')
        txtname.grid(row=0, column=1)

        lbladdress = Label(f1, font=('arial', 16, 'bold'), text="Address", fg="steel blue", bd=10, anchor='w')
        lbladdress.grid(row=1, column=0)
        txtaddress = Entry(f1, font=('arial', 16, 'bold'), textvariable=Name, bd=6, insertwidth=4, bg="powder blue",
                           justify='right')
        txtaddress.grid(row=1, column=1)

        lblphone = Label(f1, font=('arial', 16, 'bold'), text="Phone no", fg="steel blue", bd=10, anchor='w')
        lblphone.grid(row=2, column=0)
        txtphone = Entry(f1, font=('arial', 16, 'bold'), textvariable=Phoneno, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtphone.grid(row=2, column=1)




        # -----------------------------------------buttons------------------------------------------
        lblTotal = Label(f1, text="---------------------", fg="white")
        lblTotal.grid(row=6, columnspan=3)

        btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('arial', 16, 'bold'), width=10, text="RESET",
                          bg="powder blue", command=reset)
        btnreset.grid(row=7, column=2)

        btnFifthPage =Button(self, text = "Next page", command = lambda : controller.show_frame(FifthPage))
        btnFifthPage.pack()



class FifthPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        v = tkinter.IntVar()
        v.set(1)  # initializing the choice, i.e. Python

        options = [
            ("COD"),
            ("Debit card"),
            ("Credit card"),
            ("Net banking"),

        ]

        def ShowChoice():
            print(v.get())

        Tops = Frame(self, bg="white", width=1600, height=50, relief=SUNKEN)
        Tops.pack(side=TOP)
        lblinfo = Label(Tops, font=('AR CENA', 50, 'bold'), text="Choose your mode of Payment", fg="steel blue", bd=10, anchor='w')
        lblinfo.grid(row=0, column=0)



        for val, options in enumerate(options):
            tkinter.Radiobutton(self,
                           text=options,
                           padx=20,
                           variable=v,
                           command=ShowChoice,
                           value=val).pack(anchor=tkinter.CENTER)



        def helloCallBack():

            box.showinfo("info","THANK YOU FOR ORDERING!!")
        btnFifthPage =Button(self, text = "Done", command = helloCallBack)
        btnFifthPage.pack()

        btnFifthPage.place(relx=0.5, rely=0.5, anchor=CENTER)

app = Swig()
app.mainloop()