from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD SEARCH -------------------------------- #
def search_password():
    try:
        website = input_website.get()
        with open ("data.json",mode="r") as file_data:
            data = json.load(file_data)
            try:
                website_email = data[website]["email"]
                website_password = data[website]["password"]
                messagebox.showinfo(message=f"Website:  {website}\nEmail:  {website_email}\nPassword:  {website_password}")
            except KeyError:
                messagebox.showwarning(title="Not found Website",
                                       message=f"{website} does not exist in our database")
    except FileNotFoundError:
        messagebox.showwarning(title="Zero Datas",
                               message="There isn't any type of data")

    input_password.delete(0, END)
    input_website.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    input_password.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_password = [random.choice(letters) for c in range(nr_letters)]
    password_list.extend(letters_password)

    symbols_password = [random.choice(symbols) for c in range(nr_symbols)]
    password_list.extend(symbols_password)

    numbers_password = [random.choice(numbers) for c in range(nr_numbers)]
    password_list.extend(numbers_password)

    random.shuffle(password_list)
    password_str = ''.join(password_list)

    input_password.insert(0,password_str)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = input_website.get()
    email = input_username.get()
    password = input_password.get()
    new_data = {website:{"email":email,
                         "password":password}}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Fill all the informations", message="You should fill ALL the informations")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                #Reading the old data
                data = json.load(data_file)
                #Updating the old data with a new data
                data.update(new_data)

            with open("data.json",mode="w") as data_file:
                #Saving update
                json.dump(new_data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)


        input_password.delete(0, END)
        input_website.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

# WINDOW
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# CANVAS
password_canvas = Canvas(width=200, height=200)
my_pass_img = PhotoImage(file="logo.png")
password_canvas.create_image(100, 100, image=my_pass_img)
password_canvas.grid(column=1, row=0)

# LABEL
label_website = Label(text="Website")
label_website.grid(column=0, row=1)


label_username = Label(text="Email/Username")
label_username.grid(column=0, row=2)

label_password = Label(text="Password")
label_password.grid(column=0,row=3)

# INPUT
input_website = Entry(window,width=35+10)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_username = Entry(window,width=35+10)
input_username.grid(column=1, row=2,columnspan=2)
input_username.insert(0,"myemail@gmail.com")

input_password = Entry(window,width=35+10)
input_password.grid(column=1, row=3,columnspan=2)

# BUTTON
button_search = Button(text="Search",width=10, command=search_password)
button_search.grid(row=1, column=2)

button_password = Button(text="Generate Password", width=15, command=generate_password)
button_password.grid(row=3, column=2)

button_add = Button(text="Add", width=30+9, command=add_password)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()