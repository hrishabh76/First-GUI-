import tkinter as tk
from tkinter import messagebox
import sqlite3

def setup_database():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

def save_data(name, email):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def submit_data():
    name = entry_name.get()
    email = entry_email.get()
    if name and email:
        save_data(name, email)
        messagebox.showinfo("Success", "Data saved successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both name and email")

root = tk.Tk()
root.title("User Data Entry")

label_name = tk.Label(root, text="Name")
label_name.pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

label_email = tk.Label(root, text="Email")
label_email.pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.pack(pady=20)

setup_database()

root.mainloop()
