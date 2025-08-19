import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_var.get())

    characters = string.ascii_letters
    if digits_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)


# Copy to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x350")
root.config(bg="#222831")

# Title
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#222831", fg="white")
title_label.pack(pady=10)

# Password Length
length_frame = tk.Frame(root, bg="#222831")
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#222831", fg="white").pack(side="left", padx=5)
length_var = tk.StringVar(value="12")
length_entry = tk.Entry(length_frame, textvariable=length_var, width=5, font=("Arial", 12))
length_entry.pack(side="left")

# Options
options_frame = tk.Frame(root, bg="#222831")
options_frame.pack(pady=10)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Include Digits (0-9)", variable=digits_var, bg="#222831", fg="white", font=("Arial", 11), selectcolor="#393E46").pack(anchor="w")
tk.Checkbutton(options_frame, text="Include Special Characters", variable=special_var, bg="#222831", fg="white", font=("Arial", 11), selectcolor="#393E46").pack(anchor="w")

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#00ADB5", fg="white", width=20, command=generate_password)
generate_btn.pack(pady=10)

# Password Display
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, justify="center")
password_entry.pack(pady=10)

# Copy Button
copy_btn = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="#EEEEEE", fg="#222831", command=copy_to_clipboard)
copy_btn.pack(pady=5)

# Run App
root.mainloop()
