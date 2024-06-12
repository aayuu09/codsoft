import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    if not length.isdigit() or int(length) < 1:
        messagebox.showerror("Invalid Input", "Please enter a valid length")
        return
    
    length = int(length)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied to Clipboard", "Password has been copied to clipboard")
    else:
        messagebox.showwarning("No Password", "No password to copy")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(0,0)
root.configure(background='#e8cd97')

length_label = tk.Label(root, text="Password Length:",font = 'arial 12 bold')
length_label.pack(pady=10)

length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var,width = 24, font='arial 16')
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password,font = 'arial 12 bold')
generate_button.pack(pady=10)

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, state='readonly',width = 24, font='arial 16')
result_entry.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,font = 'arial 12 bold')
copy_button.pack(pady=10)

root.mainloop()