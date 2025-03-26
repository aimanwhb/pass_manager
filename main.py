from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    letter_password = [choice(letters) for _ in range(randint(8, 10))]
    symbol_password = [choice(symbols) for _ in range(randint(2, 4))]
    number_password = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_password + symbol_password + number_password
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    messagebox.showinfo(title="Info", message="Password has been copied to clipboard")

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():

    website_value = website_entry.get()
    email_username_value = email_username_entry.get()
    password_value = password_entry.get()

    if website_value  == "" and password_value == "": 
        messagebox.showerror(title= "Warning", message="Webiste and Password are missing")
    elif website_value  == "":
        messagebox.showerror(title= "Warning", message="Webiste is missing")
    elif password_value == "":
        messagebox.showerror(title="Warning", message="Password is missing")
    else:
        is_ok = messagebox.askokcancel(title= "Confirmation", message= f"These are the details entered: \n\n"
                                                                       f"Website: {website_value} \n"
                                                                       f"Email/Username: {email_username_value} \n"
                                                                       f"Password: {password_value} \n\n"
                                                                       f"Save this pasword?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website_value}  |  {email_username_value}  |  {password_value}\n")

            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100 , image= logo_image)
canvas.grid(column=1 , row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0 , row=1, sticky="W")
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0 , row=2, sticky="W")
password_label = Label(text="Password:")
password_label.grid(column=0 , row=3, sticky="W")

#entry
website_entry = Entry()
website_entry.grid(column=1 , row=1, columnspan= 2, sticky="EW")
website_entry.focus()
email_username_entry = Entry()
email_username_entry.grid(column=1 , row=2, columnspan= 2, sticky="EW")
email_username_entry.insert(0, "urmail@gmail.com")
password_entry = Entry()
password_entry.grid(column=1 , row=3, columnspan= 2, sticky="EW")

#button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2 , row=3, sticky="EW")
add_button = Button(text="Add", command= add)
add_button.grid(column=1 , row=4, columnspan= 2, sticky="EW")

window.mainloop()