from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def signup():
    firstname = e_firstname.get()
    lastname = e_lastname.get()
    age = e_age.get()
    gender = e_gender.get()
    city = e_city.get()
    address = e_address.get()
    username = e_username.get()
    email = e_email.get()
    password = e_password.get()
    repassword = e_repassword.get()

    if (
            firstname == "" or lastname == "" or age == "" or gender == "" or city == "" or address == "" or username == "" or email == "" or password == "" or repassword == ""):
        messagebox.showinfo("Signup", "All fields are required to fill")
        return True
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", db="login")
        cursor = connection.cursor()
        cursor.execute("select * from loginpage where email='" + e_email.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            (e_email.get() == "")
            messagebox.showinfo("Signup", "You have been saved this email before")
            return True

    if (
            firstname == "" or lastname == "" or age == "" or gender == "" or city == "" or address == "" or username == "" or email == "" or password == "" or repassword == ""):
        messagebox.showinfo("Signup", "All fields are required to fill")

    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", db="login")
        cursor = connection.cursor()
        cursor.execute(
            "insert into loginpage values('" + firstname + "','" + lastname + "','" + age + "','" + gender + "','" + city + "','" + address + "','" + username + "','" + email + "','" + password + "','" + repassword + "')")
        messagebox.showinfo("Signup", "Data has been saved successfully")
        cursor.execute("commit")
        e_firstname.delete(0, 'end')
        e_lastname.delete(0, 'end')
        e_age.delete(0, 'end')
        e_gender.delete(0, 'end')
        e_city.delete(0, 'end')
        e_address.delete(0, 'end')
        e_username.delete(0, 'end')
        e_email.delete(0, 'end')
        e_password.delete(0, 'end')
        e_repassword.delete(0, 'end')
        clear()
        connection.close()

# go previous page
def previous():
    import login
    login

# clear data function
def clear():
    e_firstname.delete(0, END)
    e_lastname.delete(0, END)
    e_age.delete(0, END)
    e_gender.delete(0, END)
    e_city.delete(0, END)
    e_address.delete(0, END)
    e_username.delete(0, END)
    e_email.delete(0, END)
    e_password.delete(0, END)
    e_repassword.delete(0, END)


# start Signup Window
window = Tk()
# app title
window.title("Signup")
# window size
window.maxsize(width=500, height=500)
window.minsize(width=500, height=500)
# heading label
heading = Label(window, text="Signup", font='Courier 20 bold')
heading.place(x=80, y=80)

# form data label
firstname = Label(window, text="First Name :", font='Courier 10 bold')
firstname.place(x=80, y=130)

lastname = Label(window, text="Last Name :", font='Courier 10 bold')
lastname.place(x=80, y=160)

age = Label(window, text="Age :", font='Courier 10 bold')
age.place(x=80, y=190)

Gender = Label(window, text="Gender :", font='Courier 10 bold')
Gender.place(x=80, y=220)

city = Label(window, text="City :", font='Courier 10 bold')
city.place(x=80, y=250)

address = Label(window, text="Address :", font='Courier 10 bold')
address.place(x=80, y=280)

username = Label(window, text="User Name :", font='Courier 10 bold')
username.place(x=80, y=310)

email = Label(window, text="Email :", font='Courier 10 bold')
email.place(x=80, y=340)

password = Label(window, text="Password :", font='Courier 10 bold')
password.place(x=80, y=370)

repassword = Label(window, text="Re-Password:", font='Courier 10 bold')
repassword.place(x=80, y=400)

# Entry Box ------------------------------------------------------------------

e_firstname = StringVar()
e_lastname = StringVar()
e_age = IntVar(window, value='0')
e_gender = StringVar()
e_city = StringVar()
e_address = StringVar()
e_username = StringVar()
e_email = StringVar()
e_password = StringVar()
e_repassword = StringVar()

e_firstname = Entry(window, width=40, textvariable=e_firstname)
e_firstname.place(x=200, y=133)

e_lastname = Entry(window, width=40, textvariable=e_lastname)
e_lastname.place(x=200, y=163)

e_age = Entry(window, width=40, textvariable=e_age)
e_age.place(x=200, y=193)

e_gender = ttk.Combobox(window, width=37, textvariable=e_gender)
e_gender.place(x=200, y=223)
e_gender['values'] = ('Male', 'Female', 'Other')

e_city = Entry(window, width=40, textvariable=e_city)
e_city.place(x=200, y=253)

e_address = Entry(window, width=40, textvariable=e_address)
e_address.place(x=200, y=283)

e_username = Entry(window, width=40, textvariable=e_username)
e_username.place(x=200, y=313)

e_email = Entry(window, width=40, textvariable=e_email)
e_email.place(x=200, y=343)

e_password = Entry(window, width=40, show="*", textvariable=e_password)
e_password.place(x=200, y=373)

e_repassword = Entry(window, width=40, show="*", textvariable=e_repassword)
e_repassword.place(x=200, y=403)

# button login and clear

signup = Button(window, text="Signup", font='Courier 10 bold', command=signup)
signup.place(x=200, y=443)

login = Button(window, text="Clear", font='Courier 10 bold', command=clear)
login.place(x=280, y=443)

log = Button(window, text="Log In", command=previous)
log.place(x=430, y=10)

window.mainloop()
