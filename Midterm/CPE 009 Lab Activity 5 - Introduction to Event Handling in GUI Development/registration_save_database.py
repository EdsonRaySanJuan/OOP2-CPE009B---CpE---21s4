from tkinter import *
import csv
from tkinter import messagebox

class AccRegisSys():
    def __init__(self, regis):
        # Title
        self.Label1 = Label(regis, fg='Black', text='Account Registration System', font=15)
        self.Label1.place(x=120, y=50)

        # First Name
        self.Label2 = Label(regis, text='First Name: ')
        self.Label2.place(x=50, y=80)
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
        self.Entry4 = Entry(regis, bd=2, show='*')  # Mask password input
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
        self.ButtonSubmit = Button(regis, fg='Black', text='Submit', command=self.submit)
        self.ButtonSubmit.place(x=80, y=320)

        self.ButtonClear = Button(regis, fg='Black', text='Clear', command=self.clear)
        self.ButtonClear.place(x=150, y=320)

        self.ButtonQuit = Button(regis, fg='Black', text='Quit', command=regis.quit)
        self.ButtonQuit.place(x=220, y=320)

        # Handle window close event
        regis.protocol("WM_DELETE_WINDOW", regis.quit)

    def submit(self):
        first_name = self.Entry1.get().strip()
        last_name = self.Entry2.get().strip()
        username = self.Entry3.get().strip()
        password = self.Entry4.get().strip()
        email_address = self.Entry5.get().strip()
        contact_number = self.Entry6.get().strip()

        # Check for empty inputs
        if not first_name or not last_name or not username or not password or not email_address or not contact_number:
            messagebox.showerror("Input Error", "All fields must be filled out.")
        else:
            # Write to CSV
            with open('AccReg.csv', mode='a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([f'First Name: {first_name}'])
                csv_writer.writerow([f'Last Name: {last_name}', ])
                csv_writer.writerow([f'Username: {username}'])
                csv_writer.writerow([f'Password: {password}'])
                csv_writer.writerow([f'Email Address: {email_address}'])
                csv_writer.writerow([f'Contact Number: {contact_number}'])
                # new line
                csv_writer.writerow([])

                # Confirmation dialog
                messagebox.showinfo("Form Submission", "Done! Form has been filled out.")

            # Implement the submit functionality
            print("Form Submitted")

    def clear(self):
        # Clear all entry fields
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)
        self.Entry5.delete(0, END)
        self.Entry6.delete(0, END)

