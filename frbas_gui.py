from tkinter import *
from functools import partial
import frbas_db

student = ['Shreya','Siddhi','Manjiri','Aastha','Somesh']


def validateLogin(username, password):
    tkWindow.destroy()
    x = username.get()
    if x in student:
        stud_login(x)


def stud_login(x):
    frbas_db.read(x)


if __name__ == '__main__':

    tkWindow = Tk()
    tkWindow.geometry('300x180')
    tkWindow.title('Attendance Tracker')

    usernameLabel = Label(tkWindow, text="User Name").place(x=30, y=30)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username, ).place(x=100, y=30)

    passwordLabel = Label(tkWindow, text="Password").place(x=30, y=80)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x=100, y=80)

    validateLogin = partial(validateLogin, username, password)

    # login button
    loginButton = Button(tkWindow, text="Login", command=validateLogin, activeforeground="white",
                         activebackground="black").place(x=120, y=120)

    tkWindow.mainloop()
