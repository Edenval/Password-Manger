from tkinter import * #imports all classes and constants
import math
import csv
from tkinter import messagebox #module of code, not imported with tkinter *
import pyperclip
import json
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
    website1 = web_entry.get()
    email1 = email_entry.get()
    password1 = password_entry.get()


    new_data = {
        website1: {
            "email": email1,
            "password": password1
        }
    }
    #messagebox.showinfo(title="Confirmation", message="Password has been added")
    if len(website1) == 0 or len(password1) == 0:
        messagebox.askokcancel(title="Empty fields", message="Please fill up all fields")
    else:
        #"C:\\Users\\Eden\\PycharmProjects\\pythonProject12\\passmanager\\1.json"
        try:
            with open("1.json", "r") as f:
                data = json.load(f)


        except FileNotFoundError:
            with open("1.json", "w") as f:
                json.dump(new_data, f, indent=4)


        else:
            data.update(new_data)
            with open("1.json", "w") as f:
                json.dump(data, f, indent=4)

                print(data)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- PASS SEARCH ------------------------------- #
def find_password():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
  

    try:
         with open("1.json", "r") as f:
            data = json.load(f)
            print(data)
            dataemail = data[website]["email"]
            print(dataemail)
            datapass = data[website]["password"]
            print(dataemail + datapass)
            messagebox.askokcancel(title="Details", message=f"Website: {web_entry.get()}\nEmail: {dataemail}\nPassword: {datapass}")
            pyperclip.copy(datapass)

    except FileNotFoundError:
        if len(web_entry.get()) == 0:
            messagebox.askokcancel(title="Empty fields", message="Please fill up all fields")
        else:
            messagebox.showinfo(title="No data found", message=f"No data file found")
    except KeyError:
        if len(web_entry.get()) == 0:
            messagebox.askokcancel(title="Empty fields", message="Please fill up all fields")
        else:
            print("sd")
            messagebox.showinfo(title="No data found", message=f"No website data found")

    # else:
    #     dataemail = data[email]["email"]
    #     datapass = data1[password]["password"]
    #     print(dataemail + datapass)
    #     messagebox.askokcancel(title="Details",
    #                            message=f"Website: {web_entry.get()}\nEmail: {dataemail}\nPassword: {datapass}")
    #     pyperclip.copy(datapass)

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

web_entry = Entry(width=34) #ENTRY
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=1)
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

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1, columnspan=1)

window.mainloop()