from tkinter import*

class AccRegisSys():
    def __init__ (self, regis):

        # Title
        self.Label1 = Label(regis, fg='Black', text='Account Registration System', font=15)
        self.Label1.place(x=120, y=50)

        # First Name
        self.Label2 = Label(regis, text = 'First Name: ')
        self.Label2.place(x = 50, y = 80)
        self.Entry1 = Entry(regis, bd=2)
        self.Entry1.place(x=150, y=80)

         # Last Name
        self.Label3 = Label(regis, text='Last Name: ')
        self.Label3.place(x=50, y=120)
        self.Entry2 = Entry(regis, bd=2)
        self.Entry2.place(x=150, y=120)

        # Username
        self.Label4 = Label(regis, text='Username: ')
        self.Label4.place(x=50, y=160)
        self.Entry3 = Entry(regis, bd=2)
        self.Entry3.place(x=150, y=160)

        # Password
        self.Label5 = Label(regis, text='Password: ')
        self.Label5.place(x=50, y=200)
        self.Entry4 = Entry(regis, bd=2, show='*') # # Mask password input
        self.Entry4.place(x=150, y=200)

        # Email Address
        self.Label6 = Label(regis, text='Email Address: ')
        self.Label6.place(x=50, y=240)
        self.Entry5 = Entry(regis, bd=2)
        self.Entry5.place(x=150, y=240)

        # Contact Number
        self.Label7 = Label(regis, text='Contact Number: ')
        self.Label7.place(x=50, y=280)
        self.Entry6 = Entry(regis, bd=2)
        self.Entry6.place(x=150, y=280)

        # Buttons for Submit and Clear
        self.Button1 = Button(regis, fg='Black',text='Submit', command=self.submit)
        self.Button1.place(x=80, y=320)

        self.Button1 = Button(regis, fg='Black', text='Clear', command=self.clear)
        self.Button1.place(x=150, y=320)

    #Command for buttons
        def first_name(self):
            self.Entry7.delete(0, 'end')

        def last_name(self):
            self.Entry7.delete(0, 'end')
            lastname = str(self.Entry2.get())

        def username(self):
            self.Entry7.delete(0, 'end')
            username = str(self.Entry3.get())

        def password(self):
            self.Entry7.delete(0, 'end')
            password = str(self.Entry4.get())
            for i, label in enumerate(labels):
                self.create_label_and_entry(label, 70 + i * 40, show="*" if label == "Password" else None)

        def create_label_and_entry(self, text, y, show=None):
            tk.Label(self.regis, text=text).place(x=50, y=y)
            entry = tk.Entry(self.regis, show=show)
            entry.place(x=200, y=y)
            self.entries.append(entry)  # Store entry for clearing

        def email_address(self):
            self.Entry7.delete(0, 'end')
            emailaddress = str(self.Entry5.get())

        def contact_number(self):
            self.Entry7.delete(0, 'end')
            contactnumber = str(self.Entry6.get())

    def submit(self):
        # Implement the submit functionality
        print("Form Submitted")

    def clear(self):
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)
        self.Entry5.delete(0, END)
        self.Entry6.delete(0, END)