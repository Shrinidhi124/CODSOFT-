import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=f"Generated Password: {password}")

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_label.cget("text").split(": ")[1])
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and place widgets
tk.Label(window, text="Enter the desired length of your password:").pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(window, text="")
password_label.pack(pady=10)

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
window.mainloop()
