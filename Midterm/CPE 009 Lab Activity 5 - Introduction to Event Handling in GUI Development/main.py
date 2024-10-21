from tkinter import*
from registration_save_database import AccRegisSys

def main():
    window = Tk()
    AccountRegisSys = AccRegisSys(window)
    window.title(' Account Registration System')
    window.geometry('400x400+10+10')
    window.mainloop()

if __name__ == '__main__':
    main()