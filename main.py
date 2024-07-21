from generator import *
from tkinter import *
from tkinter import messagebox
import json


def search():
    web = website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        usr_name = data[web]["username"]
        paswrd = data[web]["password"]
    except KeyError:
        if len(web):
            messagebox.showerror("Error", f"{web} not found!")
        else:
            messagebox.showerror("Error", f"Enter a website name!")
    except FileNotFoundError:
        messagebox.showerror("Error", "File does not exist!")
    else:
        messagebox.showinfo("Info", f"Username: {usr_name}\nPassword: {paswrd}")


def generate():
    paswrd = generate_password()
    password.delete(0, END)
    password.insert(0, paswrd)


# save data into file
def add_data():
    web = website.get()
    name = username.get()
    paswrd = password.get()

    if not paswrd or not web or not name:
        messagebox.showerror(title="Error", message="Complete all the information!")
        return

    new_data = {
        web: {
            "username": name,
            "password": paswrd,
        }
    }
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        if web in data:
            update_data = messagebox.askyesno("Update data",
                                              "You already have an account for this website.Do you want to update it?")
            if not update_data:
                return
    except FileNotFoundError:
        is_ok = messagebox.askokcancel(title=web,
                                       message=f"Do you want to save this data?\nEmail/username: {name}\nPassword: {paswrd}?")
        if is_ok:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        # clear the entries after saving data
        website.delete(0, END)
        username.delete(0, END)
        password.delete(0, END)


window = Tk()
window.title("Password manager")
window.configure(padx=20, pady=20)
lock_image = PhotoImage(file="logo.png")

# Canvas
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

username_label = Label(text="Username")
username_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website = Entry(width=24)
website.grid(row=1, column=1)
website.focus()

username = Entry(width=35)
username.grid(row=2, column=1, columnspan=2)

password = Entry(width=24)
password.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate", width=6, command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add data", width=33, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
