from tkinter import*

class MyWindow():
    def __init__(self, win):
        # common widgets

        # Base
        self.Label1 = Label(win, fg='Red', text='Calculator', font=15)
        self.Label1.place(x=150, y=50)

        # Entry 1
        self.Label2 = Label(win, text='Number 1: ')
        self.Label2.place(x=50, y=80)
        self.Entry1 = Entry(win, bd=2)
        self.Entry1.place(x=150, y=80)

        # Entry 2
        self.Label3 = Label(win, text='Number 2: ')
        self.Label3.place(x=50, y=120)
        self.Entry2 = Entry(win, bd=2)
        self.Entry2.place(x=150, y=120)

        # Print Result
        self.Label4 = Label(win, text='Result')
        self.Label4.place(x=50, y=160)
        self.Entry3 = Entry(win, bd=2)
        self.Entry3.place(x=150, y=160)

        # Buttons
        self.Button1 = Button(win, fg='Black',text='Add', command=self.add)
        self.Button1.place(x=80, y=200)
        self.Button1.bind('<Button-1>', self.add) # Alternative syntax

        self.Button1 = Button(win, fg='Black', text='Sub', command=self.sub)
        self.Button1.place(x=150, y=200)

        self.Button1 = Button(win, fg='Black', text='Mul', command=self.mul)
        self.Button1.place(x=220, y=200)

        self.Button1 = Button(win, fg='Black', text='Div', command=self.div)
        self.Button1.place(x=290, y=200)

        self.Button1 = Button(win, fg='Black',text='Clear',height='1',width='20', command=self.clear)
        self.Button1.place(x=130, y=240)

    # Command for buttons
    def add(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def mul(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        if num2 !=0:
            result = num1 / num2
        else:
            result = "Error"
        self.Entry3.insert(END, str(result))

    def clear(self):
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.Entry3.delete(0, END)

window = Tk()
MyWin = MyWindow(window)
window.title('Standard Calculator')
                # w  h  left top
window.geometry('400x300+10+10')
window.configure(bg='Pink')
window.mainloop()