from tkinter import * #imports all classes and constants
import math
import csv
from tkinter import messagebox #module of code, not imported with tkinter *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
import random
def generate_password():
    #global password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    popo = web_entry.get()
    emailprint = email_entry.get()
    passprint = password_entry.get()


    #messagebox.showinfo(title="Confirmation", message="Password has been added")
    if len(popo) == 0 or len(passprint) == 0:
        print(len(popo))
        messagebox.askokcancel(title="Empty fields", message="Please fill up all fields")
    #THE ASKOKCANCEL RECEIVES A BOOL TRUE/FALSE UPON METHOD CALL OK OR CANCEL
    else:
        is_ok = messagebox.askokcancel(title=popo, message=f"These are the details entered: \nWebsite: {popo} \nEmail: {emailprint} \nPassword: {passprint}")
        if is_ok:
            with open("password_manage.txt", mode="a") as file:
                file.write(f"{web_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40) #background is standard attribute widget


canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img) #x and y position
canvas.grid(column=1, row=0)

#Website
web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

web_entry = Entry(width=53) #ENTRY
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)
popo = web_entry.get()
#email/username
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_entry = Entry(width=53) #ENTRY
email_entry.insert(0, "@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)



#password
password = Label(text="Password: ")
password.grid(column=0, row=3)

password_entry = Entry(width=34) #ENTRY
password_entry.grid(row=3, column=1)

#buttons
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()