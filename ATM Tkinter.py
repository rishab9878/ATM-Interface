import tkinter as tk       # python 3
import time

current_balance=10000


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.shared_data={'Balance':tk.IntVar()}


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Homepage , Withdraw, Deposit, Balance, Exit):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#660066')
        self.controller = controller
        self.controller.title('RRNP Bank')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,
                                  tk.PhotoImage(file='C:/Users/NEHA/Desktop/Fresh/venv/atm-machine.png'))
        headingLabel1 = tk.Label(self,
                                 text="Welcome to RRNP ATM",
                                 font=('orbitron', 45, 'bold'),
                                 foreground='white',
                                 background='#660066')
        headingLabel1.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#660066')
        space_label.pack()
        pin_label = tk.Label(self,
                             text='Enter Your Pin',
                             font=('Orbitron',13,),
                             bg='#660066',
                             fg='white')
        pin_label.pack()
        my_pin=tk.StringVar()
        pin_entry_box=tk.Entry(self,
                               textvariable=my_pin,
                               font=('Orbitron',12),
                               width=22)
        pin_entry_box.focus_set()
        pin_entry_box.pack(ipady=7)
        def handle_focus_in(_):
            pin_entry_box.configure(fg='black',show='*')
        pin_entry_box.bind('<FocusIn>',handle_focus_in)
        def check_pin():
            if my_pin.get()=='2004':
                controller.show_frame('Homepage')
            else:
                incorrect_pin_label['text']='Incorrect Pin'

        enter_button=tk.Button(self,
                               text='Enter',
                               command=check_pin,
                               relief='raised',
                               borderwidth=3,
                               width=40,
                               height=1)
        enter_button.pack(pady=10)

        incorrect_pin_label=tk.Label(self,
                                     text='',
                                     font=('Orbitron',13),
                                     fg='white',
                                     bg='#660066',
                                     anchor='n')
        incorrect_pin_label.pack(fill='both',expand=True)

        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        visa_photo=tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo
        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)


        time_label=tk.Label(bottom_frame,font=('Orbitron',12))
        time_label.pack(side='right')
        tick()


class Homepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#660066')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text="RRNP ATM",
                                 font=('orbitron', 45, 'bold'),
                                 foreground='white',
                                 background='#660066')
        heading_label.pack(pady=25)

        main_menu_label=tk.Label(self,
                                 text='Main Menu',
                                 font=('Orbitron',13),
                                 fg='white',
                                 bg='#660066')
        main_menu_label.pack()

        selection_label=tk.Label(self,
                                 text='Please Choose a Option',
                                 font=('Orbitron',13),
                                 fg='white',
                                 bg='#660066',
                                 anchor='w')
        selection_label.pack(fill='x')

        button_frame=tk.Label(self,
                              bg='#660066')
        button_frame.pack(fill='both',expand=True)
        def withdraw():
            controller.show_frame('Withdraw')

        withdraw_button=tk.Button(button_frame,
                                  text='Withdraw',
                                  command=withdraw,
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        withdraw_button.grid(row=0, column=0, pady=5)

        def Deposit():
            controller.show_frame('Deposit')

        Deposit_button = tk.Button(button_frame,
                                    text='Deposit',
                                    command=Deposit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        Deposit_button.grid(row=1, column=0, pady=5)

        def Balance():
            controller.show_frame('Balance')

        Balance_button = tk.Button(button_frame,
                                    text='Balance',
                                    command=Balance,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        Balance_button.grid(row=2, column=0, pady=5)

        def exit():
            controller.show_frame('Exit')

        exit_button = tk.Button(button_frame,
                                    text='Exit',
                                    command=exit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        exit_button.grid(row=3, column=0, pady=5)



        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Orbitron', 12))
        time_label.pack(side='right')
        tick()




class Withdraw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#660066')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text="RRNP ATM",
                                 font=('orbitron', 45, 'bold'),
                                 foreground='white',
                                 background='#660066')
        heading_label.pack(pady=25)

        choose_amount_label = tk.Label(self,
                                   text='Please Enter the Amount',
                                   font=('Orbitron', 13),
                                   fg='white',
                                   bg='#660066')
        choose_amount_label.pack()

        button_frame=tk.Frame(self,
                              bg='#660066')
        button_frame.pack(fill='both',expand=True)

        def withdraw(amount):
            global current_balance
            current_balance-=amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('Homepage')
        hundred_button=tk.Button(button_frame,
                                 text='100',
                                 command=lambda: withdraw(100),
                                 relief='raised',
                                 borderwidth=3,
                                 width=50,
                                 height=4)
        hundred_button.grid(row=0, column=0, padx=50, pady=5)


        two_hundred_button=tk.Button(button_frame,
                                 text='200',
                                 command=lambda: withdraw(200),
                                 relief='raised',
                                 borderwidth=3,
                                 width=50,
                                 height=4)
        two_hundred_button.grid(row=1, column=0, padx=50, pady=5)

        five_hundred_button = tk.Button(button_frame,
                                       text='500',
                                       command=lambda: withdraw(500),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=4)
        five_hundred_button.grid(row=0, column=1,padx=450, pady=5)

        two_thousand_button = tk.Button(button_frame,
                                       text='2000',
                                       command=lambda: withdraw(2000),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=4)
        two_thousand_button.grid(row=1, column=1,padx=450 , pady=5)

        cash=tk.StringVar()
        #other_amount_entry = tk.Entry(button_frame,
         #                             textvariable='cash',
          #                            width=59,
           #                           justify='right')
        #other_amount_entry.grid(row=3,column=1, pady=5, ipady=30)
       


        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Orbitron', 12))
        time_label.pack(side='right')
        tick()

class Deposit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#660066')
        self.controller = controller

        headingLabel1 = tk.Label(self,
                                 text="RRNP ATM",
                                 font=('orbitron', 45, 'bold'),
                                 foreground='white',
                                 background='#660066')
        headingLabel1.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#660066')
        space_label.pack()
        amount_label = tk.Label(self,
                             text='Enter Amount to be Deposited',
                             font=('Orbitron',13,),
                             bg='#660066',
                             fg='white')
        amount_label.pack()

        cash = tk.StringVar()
        deposit_entry=tk.Entry(self,
                               textvariable=cash,
                               font=('Orbiton',12),
                               width=22)
        deposit_entry.pack(pady=7)

        def deposit_cash():
            global current_balance
            current_balance+=int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('Homepage')
            cash.set('')

        enter_button=tk.Button(self,
                               text='Enter',
                               command=deposit_cash,
                               relief='raised',
                               borderwidth=3,
                               width=40,
                               height=3)
        enter_button.pack(pady=10)


        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Orbitron', 12))
        time_label.pack(side='right')
        tick()





class Balance(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#660066')
        self.controller = controller

        headingLabel1 = tk.Label(self,
                                 text="RRNP ATM",
                                 font=('orbitron', 45, 'bold'),
                                 foreground='white',
                                 background='#660066')
        headingLabel1.pack(pady=25)
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label = tk.Label(self,
                                 textvariable=controller.shared_data['Balance'],
                                 font=('Orbitron',13),
                                 fg='white',
                                 bg='#660066',
                                 anchor='w')
        balance_label.pack()

        button_frame=tk.Frame(self,bg='#660066')
        button_frame.pack(fill='x',expand=True)

        def menu():
            controller.show_frame('Homepage')

        menu_button=tk.Button(self,
                                  text='menu',
                                  command=menu,
                                  relief='raised',
                                  borderwidth=3,
                                  width=50)
        menu_button.pack(pady=5)





        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Orbitron', 12))
        time_label.pack(side='right')
        tick()

class Exit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#660066')
        self.controller = controller

        headingLabel1 = tk.Label(self,
                                 text="RRNP ATM",
                                 font=('orbitron', 45, 'bold'),
                                 foreground='white',
                                 background='#660066')
        headingLabel1.pack(pady=25)

        headingLabel2 = tk.Label(self,
                                 text="Thank You For Using RRNP ATM",
                                 font=('orbitron', 45, 'bold'),
                                 foreground='white',
                                 background='#660066',
                                 height=6)
        headingLabel2.pack()




        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        def tick():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('Orbitron', 12))
        time_label.pack(side='right')
        tick()




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()